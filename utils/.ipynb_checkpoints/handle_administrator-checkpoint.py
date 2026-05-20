import requests
from requests.auth import HTTPBasicAuth
from .constants import UID, URL


def handle_administrator(action, w3_user, w3_password, bluegroup_name, uid):
    # Authentication
    auth = HTTPBasicAuth(w3_user, w3_password)
    headers = {
        "Authorization": f"Basic {auth}",
    }

    # Administrator
    if action == "add-administrator":
        url = f"{URL}?gName={bluegroup_name}&task=Administrators&mebox={uid}&Submit=Add+Administrators&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Add Administrator - Status Code: {response.status_code}")
    else:
        print("The specified action is incorrect.")
