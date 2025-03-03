#
# A very simple, naive implementation of the service factory pattern.
# https://www.tutorialspoint.com/design_pattern/factory_pattern.htm
#

# Definitions of the services
#
from interactive_app.application.resources.imdb_resources.artist_resource import Artist, ArtistRsp, ArtistResource
from interactive_app.application.services.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
# from interactive_app.application.resources.got_resources.character_resource import CharacterResource
# from interactive_app.application.resources.got_resources.episodes_resource import EpisodesResource

# from interactive_app.application.services.mongodb_data_service import MongoDBDataService
# from interactive_app.application.resources.episodes.episodes_resource import EpisodeResource

from interactive_app.application.resources.db_book.student_resource import StudentResource

# from resources.classic_models_resource.customers_resource import CustomersResource

# import interactive_app.app_secrets as app_secrets


class ServiceFactory:
    """
    A simple implementation of the service factory pattern.
    (https://www.tutorialspoint.com/design_pattern/factory_pattern.htm)

    The class creates, configures and "wires" together resource implementations.
    """

    def __init__(self):

        # A class implementing a service for accessing relational data in MySQL.
        self.mysql_config = MySQLDataServiceConfig()
        self.data_service = MySQLDataService(self.mysql_config)

        # Configuration and dependencies for the ArtistResource.
        # This is sloppy and should be in a factory specific to the resource.
        #
        artist_context = dict()
        artist_context["data_service"] = self.data_service
        artist_context["key_column"] = "nconst"
        artist_context["database"] = "s25_project_fixed"
        artist_context["collection"] = "name_basics"

        student_context = dict()
        student_context["data_service"] = self.data_service
        student_context["key_column"] = "ID"
        student_context["database"] = "db_book"
        student_context["collection"] = "student"

        # Create the resource.
        # Use dependency injection in a simple form.
        # https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
        #
        self.artist_resource = ArtistResource(artist_context)
        self.student_resource = StudentResource(student_context)

        episodes_context = dict()
        mongo_config = dict()

        # mongo_config['mongodb_url'] = app_secrets.mongodb_url
        """
        self.mongo_data_service = MongoDBDataService(mongo_config)
        episodes_context["data_service"] = self.mongo_data_service
        episodes_context["database"] = "F24_GoT"
        episodes_context["collection"] = "episodes"

        self.episodes_resource = EpisodeResource(episodes_context)
        """


        """"
        character_context = dict()
        character_context["data_service"] = self.data_service
        character_context["key_column"] = "characterName"
        character_context["database"] = "GoT_Basics"
        character_context["collection"] = "characters"

        self.character_resource = CharacterResource(character_context)

        self.mongo_config = MongoDataServiceConfig()
        self.mongo_data_service = MongoDBDataService(self.mongo_config)

        episodes_context = dict()
        episodes_context["data_service"] = self.mongo_data_service
        episodes_context["database"] = "S22_GoT"
        episodes_context["collection"] = "episodes"

        self.episodes_resource = EpisodesResource(episodes_context)

        classic_models_context = dict()
        classic_models_context["data_service"] = self.mongo_data_service
        classic_models_context["database"] = "Classic_Models"
        classic_models_context["collection"] = "Customers"

        self.customers_resource = CustomersResource(classic_models_context)
        """

    def get_resource(self, resource_name):
        """

        :param resource_name: The "name" for the resource implementation.
        :return: The resource implementation.
        """

        if resource_name == "ArtistResource":
            result = self.artist_resource
        elif resource_name == "CharacterResource":
            # result = self.character_resource
            result = None
        elif resource_name == "EpisodesResource":
            # result = self.episodes_resource
            # result = self.episodes_resource
            result = None
        elif resource_name == "CustomersResource":
            # result = self.customers_resource
            result = None
        elif resource_name == "StudentResource":
            result = self.student_resource
        else:
            result = None

        return result

