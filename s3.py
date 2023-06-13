import boto3

#S3 class to create records
class S3:

    def __init__(self,s3_key):
        self.s3_bucket = 'codingtaskclair'
        self.s3_client = boto3.client(
                            's3',
                             aws_access_key_id="AKIAU4HQJDKXCTBBGCNF",
                             aws_secret_access_key="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",
                             region_name="us-east-2"
                             )
        self.s3_key = s3_key

    def upload_model(self,model):

        self.s3_client.put_object(Body=model, Bucket=self.s3_bucket, Key=self.s3_key)
