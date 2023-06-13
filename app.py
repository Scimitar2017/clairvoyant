from flask import Flask, request, jsonify
from pymongo import MongoClient
from models import Tenant, ProjectMetadata,tenant,metadata

app = Flask(__name__)


#create tenant
@app.route('/tenant', methods=['POST'])
def create_tenant():
    tenant_id = request.json.get('tenant_id')
    tenant = Tenant(id=tenant_id)
    tenant.save()
    return jsonify({
                    'message': 'Success! Tenant created',
                    'response_code': 200
                    })

#create metadata
@app.route('/project_metadata', methods=['POST'])
def create_project_metadata():
    tenant_id = request.json.get('tenant_id')
    local_csv_location = request.json.get('local_csv_location')
    s3_location = request.json.get('s3_location')
    model_evaluation_results = request.json.get('model_evaluation_results')

    curr_tenant = tenant.find_one({'id': tenant_id})

    project_metadata = ProjectMetadata(
                                    tenant=curr_tenant,
                                    local_csv_location=local_csv_location,
                                    s3_location=s3_location,
                                    model_evaluation_results=model_evaluation_results
                                    )
    project_metadata.save()

    return jsonify({
                    'message': 'Project metadata created successfully',
                    'response_code': 200
                    })



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
