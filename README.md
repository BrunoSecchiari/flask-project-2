# BlueGroup Manager

A Flask-based desktop application for managing IBM BlueGroups. It provides a simple GUI to create, update, and manage BlueGroups — including their administrators, owners, and expiration dates — either individually or in bulk via a spreadsheet.

---

## Features

- **BlueGroup management** — Create or update BlueGroups with a name and description.
- **Administrator management** — Add or remove administrators from a BlueGroup.
- **Owner management** — Assign or update the owner of a BlueGroup.
- **Expiration date management** — Set or update the expiration date of a BlueGroup.
- **Batch processing** — Toggle batch mode to process multiple BlueGroups at once from a spreadsheet file.
- **Desktop GUI** — Runs as a standalone desktop window via `flaskwebgui` (no browser required).

---

## Project Structure

```
flask-project-2/
├── main.py                        # Flask application entry point
├── static/                        # Static assets (CSS, JS, images)
├── templates/                     # Jinja2 HTML templates
└── utils/
    ├── get_current_date.py        # Returns the current date
    ├── get_bluegroups.py          # Reads BlueGroup data from a spreadsheet
    ├── handle_administrator.py    # Logic for managing administrators
    ├── handle_bluegroup.py        # Logic for creating/updating BlueGroups
    ├── handle_expiration_date.py  # Logic for managing expiration dates
    ├── handle_owner.py            # Logic for managing owners
    └── to_boolean.py              # Converts form string values to booleans
```

---

## Requirements

- Python 3.8+
- Flask
- flaskwebgui

Install dependencies with:

```bash
pip install -r requirements.txt
```

> If there is no `requirements.txt`, install manually:
> ```bash
> pip install flask flaskwebgui
> ```

---

## Running the Application

```bash
python main.py
```

This launches the app as a desktop window (750×750). To run it in the browser instead, replace the last line in `main.py` with:

```python
app.run(debug=True, port=5555)
```

Then open [http://localhost:5555](http://localhost:5555) in your browser.

---

## Usage

1. Launch the app with `python main.py`.
2. Fill in your **w3 credentials** (email and password) — these are used to authenticate API calls to IBM's BlueGroup service.
3. Choose a tab or section for the operation you want to perform:
   - **BlueGroup** — Create or update a group by name and description.
   - **Administrator** — Add or remove a user (by User ID) as an administrator.
   - **Owner** — Assign a new owner to a group.
   - **Expiration Date** — Set the expiration date (day/month/year) for a group.
4. Enable the **batch toggle** to process all rows from the BlueGroups spreadsheet automatically.

---

## Batch Mode

When the batch toggle is enabled for any operation, the app reads BlueGroup data from a spreadsheet via `get_bluegroups()`. Each row is expected to contain:

| Column index | Content              |
|:------------:|----------------------|
| 0            | Action               |
| 1            | BlueGroup Name       |
| 2            | BlueGroup Description|
| 3            | Expiration Date      |
| 4            | User ID              |

Make sure the spreadsheet is properly configured before running in batch mode.

---

## API Endpoints

| Method | Route               | Description                        |
|--------|---------------------|------------------------------------|
| GET    | `/`                 | Renders the main interface         |
| POST   | `/bluegroup`        | Create or update a BlueGroup       |
| POST   | `/administrator`    | Manage a BlueGroup's administrators|
| POST   | `/owner`            | Update a BlueGroup's owner         |
| POST   | `/expiration_date`  | Set a BlueGroup's expiration date  |

---

## License

This project is not currently licensed. Contact the repository owner for usage permissions.
