import json
import urllib3
import boto3
import uuid

def handler(event, context):
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://jsonplaceholder.typicode.com/todos')
    
    s3 = boto3.resource('s3')
    filename = str(uuid.uuid4()) + '.json'

    s3.Object('dferrel-extracredbucket',filename).put(Body=response.data)

    return {
        'statusCode': response.status,
        'body': response.data
    }