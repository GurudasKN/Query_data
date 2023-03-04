import requests
import json

metadata_server_url = "http://metadata.google.internal/computeMetadata/v1/"

metadata_headers = {"Metadata-Flavor": "Google", "Content-Type": "application/json"}

def get_metadata(metadata_path):
 
    metadata_url = metadata_server_url + metadata_path
    response = requests.get(metadata_url, headers=metadata_headers)
    response.raise_for_status()
    return json.loads(response.content)

instance_name = get_metadata("instance/name")
print(instance_name)

all_metadata = get_metadata("instance/?recursive=true")
print(all_metadata)
