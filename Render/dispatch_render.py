UUID = "b21cb170-91da-496b-89c1-d7ec8259e3ba"
import json
import os
from pprint import pprint
from google.cloud import tasks_v2
from google.cloud import firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "google-authorisation.json"

mydb = firestore.Client()
args = mydb.collection('renders').document(UUID).get().to_dict().get("args")
pprint(args)

client = tasks_v2.CloudTasksClient()

# Values for q-ing
project = 'addlyrics'
queue = 'render-q'
location = 'europe-west1'
url = 'https://render-7cwyob5r6a-ew.a.run.app/render'
payload = json.dumps(args)

# Construct the fully qualified queue name.
parent = client.queue_path(project, location, queue)

# Construct the request body.
task = {
    'http_request': {  # Specify the type of request.
        'http_method': 'POST',
        'url': url,  # The full url path that the task will be sent to.
        'oidc_token': {
            'service_account_email': "tasker@addlyrics.iam.gserviceaccount.com"
        }
    }
}

# The API expects a payload of type bytes.
converted_payload = payload.encode()

# Add the payload to the request.
task['http_request']['body'] = converted_payload
client.create_task(parent=parent, task=task)
quit()
pprint(task)

import requests
from threading import Thread

class response():
    def __init__(self, name):
        self.name = name

def asyncRequest(url, task):
    name = requests.post(url, data=converted_payload)

def create_task(parent, task):
    url = "http://localhost:8080"
    #url = "http://192.168.1.222:5000"
    task['data'] = task['http_request']['body']

    # makeReq = Thread(target=asyncRequest, args=(url + "/render", task['http_request']))
    # makeReq.start()
    asyncRequest(url + "/render", task['http_request'])
    name = "bob"
    return response(name)

create_task(None, task)
