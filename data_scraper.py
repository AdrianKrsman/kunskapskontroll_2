from bs4 import BeautifulSoup
import requests
import pandas as pd
import logging

class DataScraper:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def get_data(self, url: str) -> list:
        """ Function to retrive data from wikipedia page. """
        # Make request from url
        response = requests.get(url)
        # Check if request was succesfull
        if response.status_code == 200:
            self.logger.info('Page loaded succesfully')
            soup = BeautifulSoup(response.content, 'html.parser')
        else:
            self.logger.error('Page not loaded correctly')
            return []
        # Find tables on wiki page
        tables = soup.find_all('table', class_='wikitable nowrap defaultcenter col2left')
        return tables
    
    def fix_rankings(self, cell_texts, move_span):
            """ Function to add 'Increase' or 'Decrease' for 'Move' column since it is not automatically gathered from page.  """
            # Check if move_span is defined
            if move_span:
                title = move_span.get('title')
            else:
                cell_texts[3] = 0
            # Set conditions for move column
            if 'Increase' in title:
                cell_texts[3] = cell_texts[3]
                self.logger.info('Increase in ranking')
            elif 'Decrease' in title:
                cell_texts[3] = '-' + cell_texts[3]
                self.logger.info('Decrease in ranking')
            else:
                cell_texts[3] = 0
                self.logger.info('No change in ranking')
            return cell_texts

    def get_atp_data(self) -> pd.DataFrame:
        """Function to get data for ATP rankings. """
        # url for wiki page
        url = 'https://en.wikipedia.org/wiki/Current_tennis_rankings'
        # Define tables with 'get_data()' function
        tables = self.get_data(url)
        if not tables:
            self.logger.error('Could not get data')
            return pd.DataFrame()
        # Create empty lists
        atp_data = []
        atp_columns = []
        for table in tables[:1]:
            # Find rows
            rows = table.find_all('tr')
            # Find headers and append to empty columns list
            header_row = rows[1].find_all('th')
            atp_columns = [header.get_text().strip() for header in header_row]
            # Find the rest of the rows except header
            for row in rows[1:]:
                cols = row.find_all('td')
                # Extract the text in the rows and append to empty data list 
                if len(cols) > 3:
                    cell_texts = [col.get_text().strip() for col in cols]
                    move_span = cols[3].find('span').find('span')
                    data = self.fix_rankings(cell_texts, move_span)
                    atp_data.append(data)
                    self.logger.info('Data appended')
        # Create a Dataframe with columns and rows
        atp_rankings = pd.DataFrame(data = atp_data, columns = atp_columns)
        return atp_rankings
    
    def get_wta_data(self) -> pd.DataFrame:
        """Function to get data for WTA ranking. """
        # url for wiki page
        url = 'https://en.wikipedia.org/wiki/Current_tennis_rankings'
        # Define tables with 'get_data()' function
        tables = self.get_data(url)
        if not tables:
            self.logger.error('Could not get data')
            return pd.DataFrame()
        # Create empty lists
        wta_data = []
        wta_columns = []
        for table in tables[4:5]:
            # Find rows
            rows = table.find_all('tr')
            # Find headers and append to empty columns list
            header_row = rows[1].find_all('th')
            wta_columns = [header.get_text().strip() for header in header_row]
            # Find the rest of the rows except headers
            for row in rows[1:]:
                cols = row.find_all('td')
                # Extract the text in the rows and append to empty data list
                if len(cols) > 3:
                    cell_texts = [col.get_text().strip() for col in cols]
                    move_span = cols[3].find('span').find('span')
                    data = self.fix_rankings(cell_texts, move_span)
                    wta_data.append(data)
        # Create a Dataframe with columns and rows
        wta_rankings = pd.DataFrame(data = wta_data, columns = wta_columns)
        return wta_rankings

