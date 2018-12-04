import sys
from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('dns', 'v1', credentials=credentials)

# Identifies the project addressed by this request.
project = 'vndirect-compute' 

# Identifies the managed zone addressed by this request. Can be the managed zone name or id.
managed_zone = 'vndirect-com-vn'  

change_body = {
  "additions": [
    {
      "kind": "dns#resourceRecordSet",
      "name": "{}.vndirect.com.vn.".format(sys.argv[1]),
      "rrdatas": [
        "{}".format(sys.argv[2])
      ],
      "ttl": 300,
      "type": "A"
    }
  ]
}

request = service.changes().create(project=project, managedZone=managed_zone, body=change_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
