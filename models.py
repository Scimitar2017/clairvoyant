from datetime import datetime
from pymongo import MongoClient

client = MongoClient('db', 27017)

db = client['codingtask']

tenant = db['tenant']
metadata = db['metadata']

class Tenant:
    def __init__(self, id, created_at=None):
        self.id = id
        self.created_at = created_at or datetime.utcnow()

    def save(self):
        tenant.insert_one(self.__dict__)



class ProjectMetadata:
    def __init__(self, tenant, local_csv_location, s3_location, model_evaluation_results):
        self.tenant = tenant
        self.local_csv_location = local_csv_location
        self.s3_location = s3_location
        self.model_evaluation_results = model_evaluation_results

    def save(self):
        metadata.insert_one(self.__dict__)
