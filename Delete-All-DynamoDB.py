from curses.ascii import TAB
import boto3
from pprint import pprint


AWS_ACCESS = ""
AWS_SECRET = ""
AWS_REGION = ""
TABLE_NAME = ""
PARTITION_KEY = ""

dynamodb = boto3.resource('dynamodb', AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

scan = table.scan()
pprint(type(scan['Items']))

with table.batch_writer() as batch:
    for each in scan['Items']:
        batch.delete_item(Key={PARTITION_KEY: each[PARTITION_KEY]})
        print("Deleted: " +  each[PARTITION_KEY])
