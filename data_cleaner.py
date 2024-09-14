import pandas as pd
import logging
from datetime import datetime

def clean_data(data):
    """ Cleans data collected from the DataCollector class"""
    logger = logging.getLogger(__name__)
    # Check if data is loaded correctly as pandas df
    if isinstance(data, pd.DataFrame):
        logger.info('Data loaded succesfully')
    else:
        logger.error('Data not loaded')
    # Split the player column into player and country columns
    data[['Player', "Country"]] = data.Player.str.split('(', expand = True)
    data['Country'] = data['Country'].str.replace(')', '')
    data['Country'] = data['Country'].fillna('Not allowed')
    # Transform 'Move' column to integer
    try:
        data['Move'] = data['Move'].astype(int)
        logger.info('Move succesufully converted to integer')
    except ValueError:
        logger.error("Could not convert 'Move' to integer")
    # remove ',' from Points and convert to integer type
    data['Points'] = data['Points'].str.replace(',', '')
    try:
        data['Points'] = data['Points'].astype(int)
        logger.info('Points converted to integer')
    except ValueError:
        logger.error("Could not convert 'Points' to integer")
    # Add a date column with current date
    data['Date'] = datetime.now().strftime('%Y-%m-%d')
    # Change names of column headers and return new df
    data_clean = data.rename(columns={'Move': 'Change', 'No.': 'Rank'})
    return data_clean