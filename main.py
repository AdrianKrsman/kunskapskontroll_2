import logging
from data_scraper import DataScraper
from data_cleaner import clean_data
from export_sql import DataExport

logger = logging.getLogger(__name__)
# Set up configuration for logging
logging.basicConfig(
    filename = 'test_log.log', 
    format = '[%(asctime)s][%(name)s] %(message)s', 
    datefmt = '%Y-%m-%d %H:%M', 
    level=  logging.ERROR)

logger.info('Starting data pipeline...')

def main():
    """ Function to run all modules. """
    scraper = DataScraper()
    exporter = DataExport()
    atp_df = scraper.get_atp_data()
    wta_df = scraper.get_wta_data()
    clean_atp = clean_data(atp_df)
    clean_wta = clean_data(wta_df)
    exporter.export_atp(clean_atp)
    exporter.export_wtp(clean_wta)
    

if __name__ == "__main__":
    main()