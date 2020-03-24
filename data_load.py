from google.cloud import bigquery, storage

import warnings
warnings.simplefilter('ignore')

# GCP
PROJECT = 'aaa-np-cah'
BQ_DATASET = 'aaa_training'
GCS_BUCKET = 'aaa-training'

    
def download_blob(storage_client, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    bucket = storage_client.bucket(GCS_BUCKET)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print("Blob {} downloaded to {}.".format(source_blob_name, destination_file_name))

def import_data_from_BQ(bigquery_client, table_name):
    # Set table info
    bq_table = BQ_DATASET+'.'+table_name
    
    # Import labeling Data
    select = """
    SELECT
       PassengerId
       , Survived
       , Pclass
       , Name
       , Sex
       , Age
       , SibSp
       , Parch
       , Ticket
       , Fare
       , Cabin
       , Embarked
    FROM 
    """ 
    
    orderBy = """
    ORDER BY PassengerId
    """
    
    data = read_from_bqtable(bigquery_client, select+bq_table+orderBy, bq_table)

    print('Data load complete.')
    
    return data 

def read_from_bqtable(bigquery_client, sql, table_name):     
    # Run a Standard SQL query with the project set explicitly
    print('Importing data from '+table_name)
    imported_data = bigquery_client.query(sql, project=PROJECT).to_dataframe()
    rows, columns = imported_data.shape
    print ('Imported {0} rows, {1} columns'.format(rows, columns))
    return imported_data