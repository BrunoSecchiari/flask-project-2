import pandas
from .constants import DIRECTORY


def get_bluegroups():
    dataframe = pandas.read_excel(
        DIRECTORY / "Input Files" / "BlueGroups.xlsx",
        dtype={
            "Action *": str,
            "Blue Group Name *": str,
            "Blue Group Description": str,
            "User ID *": str,
        },
        parse_dates=["Expiration Date *"],
        sheet_name="BlueGroup",
    )

    return dataframe
