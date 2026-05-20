import os
from .constants import DIRECTORY
from .get_current_date import get_current_date

current_quarter, current_year = get_current_date()[-2:]

def create_output_folder() -> None:
    try:
        # Create a folder for the current year
        current_year_folder = f'{DIRECTORY}\\Output Files\\{current_year}'

        if not os.path.exists(current_year_folder):
            os.mkdir(current_year_folder)
        
        # Create a folder for the current quarter
        current_quarter_folder = f'{DIRECTORY}\\Output Files\\{current_year}\\{current_quarter}Q'

        if not os.path.exists(current_quarter_folder):
            os.mkdir(current_quarter_folder)
    except:
        pass