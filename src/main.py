from sodapy import Socrata
import sys
import argparse
import os
from elasticsearch import Elasticsearch
from datetime import datetime

DATASET_ID = "nc67-uf89"
APP_TOKEN = os.environ.get("APP_TOKEN")
ES_HOST = os.environ.get("ES_HOST")
ES_USERNAME = os.environ.get("ES_USERNAME")
ES_PASSWORD = os.environ.get("ES_PASSWORD")

client = Socrata(
        "data.cityofnewyork.us",
        APP_TOKEN,
    )
row_count = client.get(DATASET_ID, select='COUNT(*)')[0]
num_rows = int(row_count['COUNT'])

parser = argparse.ArgumentParser()

parser.add_argument('--page_size', type=int, default=1000)
parser.add_argument('--num_pages', type=int, default=0)

args = parser.parse_args(sys.argv[1:])

if __name__ == '__main__':
    
    if args.num_pages == 0:
        page_size = args.page_size
        num_pages = num_rows // page_size + 1
    
    else:
        page_size = args.page_size
        num_pages = args.num_pages
    

    mapping = {
        "settings": {
            "number_of_shards": 1
        },
        "mappings": {
                    "properties": {
                    "state": { "type": "text" },
                    "county": { "type": "text" },
                    "violation": { "type": "text" },
                    "fine_amount": { "type": "double" },
                    "penalty_amount": { "type": "double" },
                    "interest_amount": { "type": "double" },
                    "reduction_amount": { "type": "double" },
                    "payment_amount": { "type": "double"},
                    "amount_due": { "type": "double" },
                    }
                }
            }
    
    elastic = Elasticsearch([ES_HOST], http_auth=(ES_USERNAME, ES_PASSWORD))
    
    elastic.indices.create(index='project1', ignore=400, body=mapping)

    
    for i in range(0,num_pages):
        offset = i*page_size
        rows = client.get(DATASET_ID, limit=page_size, offset=offset)
        
        for row in rows:
            try:
                row["issue_date"] = str(row["issue_date"])
                row["issue_date"] = datetime.strptime(
                    row["issue_date"],"%m/%d/%Y")
    
                resp = elastic.index(index='project1'
                , body=row)
                
                print(resp)
    
            except Exception:
                pass
        