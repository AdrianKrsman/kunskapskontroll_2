import pandas as pd
import pytest
from data_cleaner import clean_data

@pytest.fixture
def sample_data():
    """ Fixture to create sample data for clean method. """
    data = {
        'No.': [1, 2, 3],
        'Player': ['Player 1 (USA)', 'Player 2 (GER)', 'Player 3 (SRB)'],
        'Points': ['5,000', '3,500', '2,000'],
        'Move': [0, 2, -3]
    }
    return pd.DataFrame(data)

def test_clean_data(sample_data):
    # get data and apply clean_data method
    cleaned_data = clean_data(sample_data)
    # assert that the dataframe has 6 columns after cleaning
    try:
        assert len(cleaned_data.columns) == 6
    except AssertionError:
        pytest.fail('Expected 6 columns for Dataframe')
        
    # assert that points is of integer type, for both WTA and ATP
    try:
        assert cleaned_data['Points'].apply(lambda x: isinstance(x, int)).all()
    except ValueError:
        pytest.fail("Column 'Points' expected to be integer")



