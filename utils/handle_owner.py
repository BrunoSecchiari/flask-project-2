import requests
from requests.auth import HTTPBasicAuth
from .constants import URL


def handle_owner(action, w3_user, w3_password, bluegroup_name, uid):
    # Authentication
    auth = HTTPBasicAuth(w3_user, w3_password)
    headers = {
        "Authorization": f"Basic {auth}",
    }

    # Owner
    if action == "change-owner":
        url = f"{URL}?gName={bluegroup_name}&task=GoCO&mebox={uid}&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Change Owner - Status Code: {response.status_code}")
    else:
        print("The specified action is incorrect.")
