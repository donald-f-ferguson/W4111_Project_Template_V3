from interactive_app.application.services.mysql_data_service import MySQLDataService


class ArtistMySQLDataService(MySQLDataService):

    def __init__(self, config):
        super().__init__(config)

