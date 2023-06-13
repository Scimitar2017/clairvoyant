import unittest
from pymongo import MongoClient
import uuid
from app import app

class TestTenant(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['testing']

    def test_create_tenant(self):

        tenant_id = str(uuid.uuid4())
        tenant_data = {'id': tenant_id }

        self.db.tenant.insert_one(tenant_data)

        retrieved_tenant = self.db.tenant.find_one({'id': tenant_id})
        self.assertEqual(retrieved_tenant['id'], tenant_id)

class TestProjectMetadata(unittest.TestCase):
    def setUp(self):

        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['testing']

    def test_create_project_metadata(self):

        tenant_id = str(uuid.uuid4())
        tenant_data = {'id': tenant_id }

        self.db.tenant.insert_one(tenant_data)
        tenant = self.db.tenant.find_one({'id': tenant_id})

        project_metadata_data = {
            'tenant': tenant,
            'local_csv_location': 'path/to/csv',
            's3_location': 's3://bucket/model.pkl',
            'model_evaluation_results': 'Evaluation results'
        }
        self.db.metadata.insert_one(project_metadata_data)

        retrieved_project_metadata = self.db.metadata.find_one({'tenant': tenant})
        self.assertEqual(retrieved_project_metadata['local_csv_location'], 'path/to/csv')
        self.assertEqual(retrieved_project_metadata['s3_location'], 's3://bucket/model.pkl')
        self.assertEqual(retrieved_project_metadata['model_evaluation_results'], 'Evaluation results')

if __name__ == '__main__':
    unittest.main()
