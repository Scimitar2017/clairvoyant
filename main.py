import os
import boto3
import uuid
import requests
from dotenv import load_dotenv
import pickle
from ml_model import ML
from app import app
from models import tenant, metadata
from s3 import S3

# Read environment variables

load_dotenv()
csv_file = os.environ.get('CSV_FILE')
target_column = os.environ.get('TARGET_COLUMN')

ml_component = ML()

#Get model and validation
model,scores = ml_component.create_model(csv_file)

#Save file
model_file = pickle.dumps(model)

#app_url = "http://<container-name>:port"
app_url = "http://ct-app-1:5000"

with app.app_context():

    #create new tenant
    tenant_id = str(uuid.uuid4())

    tenant_data = {
        "tenant_id" : tenant_id
    }
    tenant_resp = requests.post(
        f"{app_url}/tenant",
        json = tenant_data
    )

    #save to s3
    s3_key = f"{tenant_id}_model.pkl"
    s3 = S3(s3_key)
    s3.upload_model(model_file)

    # Create a new project metadata
    project_metadata_data = {
        "tenant_id" : tenant_id,
        "local_csv_location" : csv_file,
        "s3_location" : f's3://{s3.s3_bucket}/{s3_key}',
        "model_evaluation_results": str(scores)
    }

    project_metadata_resp = requests.post(
        f"{app_url}/project_metadata",
        json = project_metadata_data
    )

# check response
    if tenant_resp.status_code == 200:
        fetched_tenant = tenant.find_one({'id': tenant_id})
        print("Tenant:", fetched_tenant)
    else:
        print("Tenant creation failed")


#print records
    if project_metadata_resp.status_code == 200:
        fetched_project_metadata = metadata.find_one({'tenant': fetched_tenant})
        print("Project Metadata:", fetched_project_metadata)
    else:
        print("Project Metadata creation failed")
