import sqlite3
import logging

class DataExport():
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def export_atp(self, data):
        """ Export ATP data to sql. """
        try:
            # Create a connection
            with sqlite3.connect('Top_20_ATP') as con:
                # Export data to a SQL lite table, if a table already exists append it to the table.
                data.to_sql('Top_20_atp', con, if_exists = 'append', index = False)
                self.logger.info('ATP Data exported to sql succesfully')
        except sqlite3.Error as e:
            self.logger.error(f'Could not export ATP data: {e}')

    def export_wtp(self, data):
        """Export WTA data to sql. """
        try:
            # Create a connection
            with sqlite3.connect('Top_20_WTP') as con:
                # Export data to a SQL lite table, if a table already exists append it to the table.
                data.to_sql('Top_20_wta', con, if_exists = 'append', index = False)
                self.logger.info('WTA Data exported to sql succesfully')
        except sqlite3.Error as e:
            self.logger.error(f'Could not export WTA data: {e}')