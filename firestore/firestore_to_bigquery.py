
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore as gc_firestore
from google.cloud import bigquery

import uuid
import datetime
import random
import os
import base64

# Get environment variables
PRODUCTION = os.getenv('PRODUCTION')

# generate the constants
FILE_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FIREBASE_ADMIN_CREDS = os.path.join(FILE_DIR_PATH, "firebase_admin.json")
BIGQUERY_ADMIN_CREDS = os.path.join(FILE_DIR_PATH, 'iothousemanager-bigquery_key.json')

def firestore_backup_bigquery(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
        event (dict):  The dictionary with data specific to this type of
        event. The `data` field contains the PubsubMessage message. The
        `attributes` field will contain custom attributes if there are any.
        context (google.cloud.functions.Context): The Cloud Functions event
        metadata. The `event_id` field contains the Pub/Sub message ID. The
        `timestamp` field contains the publish time.
    """

    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))

    if PRODUCTION == "True":

        # Use the gcloud default credentials
        # initialize clients
        print("Production dist")
        client = bigquery.Client()
        db = gc_firestore.Client()
        
        
    else:
        # Use a service account
        print("Test dist")
        cred = credentials.Certificate(FIREBASE_ADMIN_CREDS)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        client = bigquery.Client.from_service_account_json(BIGQUERY_ADMIN_CREDS)
        

    # create the firebase and bigtable db reference
    colection_name = db.collection('colection_name')
    table_id = "proyect_name.collection_dataset.table_name"
    bigQuery_table = client.get_table(table_id)  # Make an API request.
    
    rows_to_insert_buffer = list()
    docs_to_errase_buffer = list()
    bath_row_size = 100 # number of rows on each write batch request to bigquery 
    no_of_rows = 0

    docs =  colection_name.limit(500).stream() #limiting the stream response (this limit is in bytes i guess)
    for n, doc in enumerate(docs):

        # read the value of the doc (might be good to save the data to a file (temp))
        current_doc = doc.to_dict()
        print("Document number %i with name: %s" % ( (n+1), doc.id), end='\r')

        # append to the list if the field exist:
        rows_to_insert_buffer.append(
            (
            current_doc["field_1"] if "field_1" in current_doc else None,
            current_doc["field_2"] if "field_2" in current_doc else None,
            current_doc["field_3"] if "field_3" in current_doc else None,
            current_doc["field_4"] if "field_4" in current_doc else None,
            current_doc["field_5"] if "field_5" in current_doc else None,
            )
        )

        # if the document was read append to the errase list
        docs_to_errase_buffer.append(doc.id)
        
        # write to bigquery and delete from firestore on size completed
        if (n+1) % bath_row_size == 0:

            # save the row to the bigquery table
            #print(docs_to_errase_buffer)
            no_of_rows += bath_row_size
            errors = client.insert_rows(bigQuery_table, rows_to_insert_buffer)  # Make an API request.
            if errors == []:
                print(">>> New rows have been added to BigQuery. Number of rows: ", no_of_rows)

                # errase the saved data if no errors were found
                batch = db.batch()
                for index, document_id in enumerate(docs_to_errase_buffer):
                    # generate the documents
                    batch.delete(colection_name.document(document_id))
                batch.commit()
                print(">>> Rows eliminated from firestore")

            else:
                print("--- Error inserting batch to bigquery: ", errors)
                # save back to firestore or to cloud storage

            rows_to_insert_buffer = []
            docs_to_errase_buffer = []
    
    # in case the batch stop  at a batch multiple and still remain some documents to read
    if len(rows_to_insert_buffer) > 0: 
        no_of_rows += len(rows_to_insert_buffer)
        
        # save the remaining rows to bigquery
        errors = client.insert_rows(bigQuery_table, rows_to_insert_buffer)  # Make an API request.
        if errors == []:
            print(">>> New rows have been added to BigQuery. Number of rows: ", no_of_rows)

            # errase the saved data if no errors were found
            batch = db.batch()
            for index, document_id in enumerate(docs_to_errase_buffer):
                # generate the documents
                batch.delete(colection_name.document(document_id))
            batch.commit()
            print(">>> Rows eliminated from firestore")
            
        else:
            print("--- Error inserting batch to bigquery: ", errors)