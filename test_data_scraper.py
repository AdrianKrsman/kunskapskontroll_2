import pytest
import pandas as pd
from data_scraper import DataScraper

def test_data_scraper():
    # use get_data method
    url = 'https://en.wikipedia.org/wiki/Current_tennis_rankings'
    scraper = DataScraper()
    tables = scraper.get_data(url)
    # assert that tables is returned as a list
    try:
        assert isinstance(tables, list)
    except AssertionError:
        pytest.fail('Tables is expected to be a list')
    # Get ATP and WTA tables
    atp_data = scraper.get_atp_data()
    wta_data = scraper.get_wta_data()
    # Assert that they are fetched as pandas Dataframes
    try:
        assert isinstance(atp_data, pd.DataFrame)
    except AssertionError:
        pytest.fail('ATP data expected to be a pandas Dataframe')

    try:
        assert isinstance(wta_data, pd.DataFrame)
    except AssertionError:
        pytest.fail('WTA data expected to be a pandas Dataframe')