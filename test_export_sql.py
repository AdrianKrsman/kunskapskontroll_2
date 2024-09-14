import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from export_sql import DataExport

@pytest.fixture
def sample_data():
    """ Fixture to create sample data for clean method. """
    data = {
        'Rank': [1, 2, 3],
        'Player': ['Player 1', 'Player 2', 'Player 3'],
        'Points': [5000, 3500, 2000],
        'Change': [0, 2, -3],
        'Country': ['USA', 'GER', 'SRB']
    }
    return pd.DataFrame(data)

@pytest.fixture
def data_export_instance():
    return DataExport()

@patch('sqlite3.connect')
@patch('pandas.DataFrame.to_sql')
def test_export_data(mock_to_sql, mock_connect, sample_data, data_export_instance):
    # Mock the sqlite connection object
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    # Call the export_atp function with sample_data
    data_export_instance.export_atp(sample_data)

    # Assert that the mock connection was called to 'Top_20_ATP'
    mock_connect.assert_called_once_with('Top_20_ATP')

    # Assert that 'to_sql' was called with correct arguments
    mock_to_sql.assert_called_once_with(
        'Top_20_atp', mock_conn.__enter__(), if_exists='append', index=False
    )