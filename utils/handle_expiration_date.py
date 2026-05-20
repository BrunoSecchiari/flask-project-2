import requests
from requests.auth import HTTPBasicAuth
from .constants import URL


def handle_expiration_date(
    action,
    w3_user,
    w3_password,
    bluegroup_name,
    expiration_day,
    expiration_month,
    expiration_year,
):
    # Authentication
    auth = HTTPBasicAuth(w3_user, w3_password)
    headers = {
        "Authorization": f"Basic {auth}",
    }

    if action == "update-expiration-date":
        # Expiration Date
        url = f"{URL}?gName={bluegroup_name}&task=GoCc&Y={expiration_year}&M={expiration_month}&D={expiration_day}&API=1"
        response = requests.get(url, headers=headers, auth=auth)
        print(f"Update Expiration Date - Status Code: {response.status_code}")
    else:
        print("The specified action is incorrect.")
