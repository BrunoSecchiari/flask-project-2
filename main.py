# --- Warnings --- #

import warnings

warnings.filterwarnings("ignore")

# --- Utilities --- #

from utils.get_current_date import get_current_date
from utils.get_bluegroups import get_bluegroups
from utils.handle_administrator import handle_administrator
from utils.handle_bluegroup import handle_bluegroup
from utils.handle_expiration_date import handle_expiration_date
from utils.handle_owner import handle_owner
from utils.to_boolean import to_boolean

# --- Flask --- #

from flask import Flask, make_response, render_template, request, jsonify
from flaskwebgui import FlaskUI

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    current_date = get_current_date()[0].strftime("%m/%d/%Y")
    return render_template("index.html", current_date=current_date)


@app.route("/administrator", methods=["POST"])
def administrator():
    action = request.form.get("action")
    administrator_toggle = request.form.get("administratorToggle")
    bluegroup_name = request.form.get("blueGroupName")
    uid = request.form.get("userId")
    w3_email = request.form.get("w3Email")
    w3_password = request.form.get("w3Password")

    # Parse the value received into a boolean value
    administrator_toggle = to_boolean(administrator_toggle)

    print(f"Action: {action}")
    print(f"BlueGroup Name: {bluegroup_name}")
    print(f"User ID: {uid}")
    print(f"w3 - Email: {w3_email}")
    print(f"w3 - Password: {'*' * len(w3_password)}")

    if action == "administrators" and administrator_toggle:
        dataframe = get_bluegroups()

        for index in dataframe.index:
            current_action = dataframe.iloc[index, 0]
            current_bluegroup_name = dataframe.iloc[index, 1]
            current_uid = dataframe.iloc[index, 4]

            handle_administrator(
                current_action,
                w3_email,
                w3_password,
                current_bluegroup_name,
                current_uid,
            )
    else:
        handle_administrator(action, w3_email, w3_password, bluegroup_name, uid)

    return jsonify({"message": "The owner has been updated successfully!"})


@app.route("/bluegroup", methods=["POST"])
def bluegroup():
    action = request.form.get("action")
    bluegroup_name = request.form.get("blueGroupName")
    bluegroup_description = request.form.get("blueGroupDescription")
    bluegroup_toggle = request.form.get("blueGroupToggle")
    w3_email = request.form.get("w3Email")
    w3_password = request.form.get("w3Password")

    # Parse the value received into a boolean value
    bluegroup_toggle = to_boolean(bluegroup_toggle)

    print(f"Action: {action}")
    print(f"BlueGroup Name: {bluegroup_name}")
    print(f"BlueGroup Description: {bluegroup_description}")
    print(f"BlueGroup Toggle: {bluegroup_toggle}")
    print(f"w3 - Email: {w3_email}")
    print(f"w3 - Password: {'*' * len(w3_password)}")

    if action == "bluegroups" and bluegroup_toggle:
        dataframe = get_bluegroups()

        for index in dataframe.index:
            current_action = dataframe.iloc[index, 0]
            current_bluegroup_name = dataframe.iloc[index, 1]
            current_bluegroup_description = dataframe.iloc[index, 2]

            handle_bluegroup(
                current_action,
                w3_email,
                w3_password,
                current_bluegroup_name,
                current_bluegroup_description,
            )
    else:
        handle_bluegroup(
            action,
            w3_email,
            w3_password,
            bluegroup_name,
            bluegroup_description,
        )

    return jsonify({"message": "The BlueGroup has been assessed successfully!"})


@app.route("/expiration_date", methods=["POST"])
def expiration_date():
    action = request.form.get("action")
    bluegroup_name = request.form.get("blueGroupName")
    expiration_day = request.form.get("expirationDay")
    expiration_month = request.form.get("expirationMonth")
    expiration_year = request.form.get("expirationYear")
    expiration_date_toggle = request.form.get("expirationDateToggle")
    w3_email = request.form.get("w3Email")
    w3_password = request.form.get("w3Password")

    # Parse the value received into a boolean value
    expiration_date_toggle = to_boolean(expiration_date_toggle)

    print(f"Action: {action}")
    print(f"BlueGroup Name: {bluegroup_name}")
    print(f"Expiration Day: {expiration_day}")
    print(f"Expiration Month: {expiration_month}")
    print(f"Expiration Year: {expiration_year}")
    print(f"Expiration Date Toggle: {expiration_date_toggle}")
    print(f"w3 - Email: {w3_email}")
    print(f"w3 - Password: {'*' * len(w3_password)}")

    if action == "expiration-dates" and expiration_date_toggle:
        dataframe = get_bluegroups()

        for index in dataframe.index:
            current_action = dataframe.iloc[index, 0]
            current_bluegroup_name = dataframe.iloc[index, 1]
            current_expiration_date = dataframe.iloc[index, 3]

            handle_expiration_date(
                current_action,
                w3_email,
                w3_password,
                current_bluegroup_name,
                expiration_day=current_expiration_date.day,
                expiration_month=current_expiration_date.month,
                expiration_year=current_expiration_date.year,
            )
    else:
        handle_expiration_date(
            action,
            w3_email,
            w3_password,
            bluegroup_name,
            expiration_day,
            expiration_month,
            expiration_year,
        )

    return jsonify({"message": "The expiration date has been assessed successfully!"})


@app.route("/owner", methods=["POST"])
def owner():
    action = request.form.get("action")
    bluegroup_name = request.form.get("blueGroupName")
    uid = request.form.get("userId")
    owner_toggle = request.form.get("ownerToggle")
    w3_email = request.form.get("w3Email")
    w3_password = request.form.get("w3Password")

    # Parse the value received into a boolean value
    owner_toggle = to_boolean(owner_toggle)

    print(f"Action: {action}")
    print(f"BlueGroup Name: {bluegroup_name}")
    print(f"User ID: {uid}")
    print(f"w3 - Email: {w3_email}")
    print(f"w3 - Password: {'*' * len(w3_password)}")

    if action == "owners" and owner_toggle:
        dataframe = get_bluegroups()

        for index in dataframe.index:
            current_action = dataframe.iloc[index, 0]
            current_bluegroup_name = dataframe.iloc[index, 1]
            current_uid = dataframe.iloc[index, 4]

            handle_owner(
                current_action,
                w3_email,
                w3_password,
                current_bluegroup_name,
                current_uid,
            )
    else:
        handle_owner(action, w3_email, w3_password, bluegroup_name, uid)

    return jsonify({"message": "The owner has been updated successfully!"})


if __name__ == "__main__":
    # app.run(debug=True, port=5555)
    FlaskUI(app=app, server="flask", height=750, width=750).run()
