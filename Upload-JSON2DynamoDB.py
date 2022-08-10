from __future__ import print_function
import json
from msilib.schema import File
import boto3
from pprint import pprint

AWS_ACCESS = ""
AWS_SECRET = ""
AWS_REGION = ""
TABLE_NAME = ""
JSON_FILE = ""

f = open(JSON_FILE)
distros_dict = json.load(f)

items = []
for row in distros_dict:
    pprint((row))


dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION)

table = dynamodb.Table(TABLE_NAME)
mylist = distros_dict
for mydict in mylist:
    boto3.resource('dynamodb')
    pprint(mydict)
    response = table.put_item(Item=mydict)