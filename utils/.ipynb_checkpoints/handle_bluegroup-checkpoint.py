import requests
from requests.auth import HTTPBasicAuth
from .constants import UID, URL
from .get_current_date import get_current_date

current_date = get_current_date()[0]
view_access = "Owner/Admins"


def handle_bluegroup(
    action, w3_user, w3_password, bluegroup_name, bluegroup_description
):
    # Authentication
    # auth = HTTPBasicAuth(w3_user, w3_password)
    auth = HTTPBasicAuth("bsecchia@ar.ibm.com", "mimamasabemuy31")
    headers = {
        "Authorization": f"Basic {auth}",
    }

    # Expiration Date
    expiration_year = current_date.year + 1

    if current_date.month < 10:
        expiration_month = f"0{current_date.month}"
    else:
        expiration_month = current_date.month

    if current_date.day < 10:
        expiration_day = f"0{current_date.day}"
    else:
        expiration_day = current_date.day

    # BlueGroup
    if action == "create-bluegroup":
        # Step 1 - Create BlueGroup
        url = f"{URL}?selectOn={bluegroup_name}&task=GoNew&gDesc={bluegroup_description}&mode=members&vAcc={view_access}&Y={expiration_year}&M={expiration_month}&D={expiration_day}&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Create BlueGroup - Status Code: {response.status_code}")

        # Step 2 - Add Administrator
        uid = UID["ADD_ADMINISTRATOR"]
        url = f"{URL}?gName={bluegroup_name}&task=Administrators&mebox={uid}&Submit=Add+Administrators&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Add Administrator - Status Code: {response.status_code}")

        # Step 3 - Delete Member
        uid = UID["DELETE_MEMBER"]
        url = f"{URL}?gName={bluegroup_name}&task=DelMem&mebox={uid}&Delete=Delete+Checked&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Delete Member - Status Code: {response.status_code}")
    elif action == "delete-bluegroup":
        url = f"{URL}?gName={bluegroup_name}&task=GoDel&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Delete BlueGroup - Status Code: {response.status_code}")
    else:
        print("The specified action is incorrect.")
