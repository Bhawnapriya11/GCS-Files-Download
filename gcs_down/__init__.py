import os
from google.cloud import storage
global table_id
global bucket_name
import google.auth
from google.oauth2 import service_account 

def download_from_bucket(bucket_name,credentials,folder,ext):
    

#storage_client = storage.Client.from_service_account_json(‘sa-api-access.json’)
    storage_client=storage.Client.from_service_account_json(credentials)
    #credentials = service_account.Credentials.from_service_account_file('sa-api-access.json')
    # The “folder” where the files you want to download are
    #delimiter='/'
    
    bucket=storage_client.get_bucket(bucket_name)
    blobs=bucket.list_blobs() 
    
    if not os.path.exists(folder): 
        os.makedirs(folder)
    
    print(bucket_name,credentials,folder,ext)
    
    if ext=='all':
        for blob in blobs: 
            print(blob.name)
            destination_uri='{}/{}'.format(folder,blob.name) 
            blob.download_to_filename(destination_uri) 
    else:
        newext='.'+ext
        print(newext)
        for blob in blobs:
            name=blob.name
            if name.endswith(newext):
                print(blob.name)
                destination_uri='{}/{}'.format(folder,blob.name) 
                blob.download_to_filename(destination_uri) 
