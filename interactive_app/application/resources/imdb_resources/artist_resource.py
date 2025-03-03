#
# Implement the resource logic and methods for IMDB name_basics data.
#

# Use pydantic to define models and transfer objects.
from typing import List, Union
from pydantic import BaseModel


# All resources implement a common base interface. This simplifies using
# resources in some scenarios.
#
from interactive_app.application.resources.base_application_resource import BaseResource, Link

# Import the models
#
from interactive_app.application.resources.imdb_resources.artist_models import Artist, ArtistRsp, ArtistsRsp


class ArtistResource(BaseResource):
    """
    Implement the Artist Resource
    """

    # DFF TODO -- Some of the methods can be moved into the base class.

    def __init__(self, context):
        super().__init__(context)
        self.key_column = context["key_column"]
        self.database = context["database"]
        self.collection = context["collection"]

    # Implements getting a single artists based on primary key.
    # Corresponds to GET /api/artists/nm0000001
    #
    def get_by_key(self, key):
        """

        :param key: The value of the primary key/ID in the collection.
        :return: An ArtistRsp with the data and links.
            TODO Need to convert to a 404 somewhere.
        """

        result = None

        ds = self.context['data_service']

        predicate = {self.key_column: key}

        result = ds.retrieve(self.database, self.collection, predicate, None)

        # Get on a path like /api/artists/id returns a single resource.
        # The collection query returns a list of matching resources.
        # Need to convert to a single element.
        #
        if result:
            result = result[0]
            tmp = dict()
            tmp["data"] = result

            # This is pretty lazy and could be handled by config information.
            #
            tmp["links"] = [
                {"rel": "primaryProfessions", "href": "/api/artists/" + key + "/primaryProfession"},
                {"rel": "self", "href": "/api/artists/" + key}
            ]

            # Create the response model from the dictionary.
            result = ArtistRsp(**tmp)

        return result

    def retrieve(self, predicate, project):
        """
        Query the data service/database and return matching items.

        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ...
        :param project: A list of subsets of the entity's properties to return. That is, if the list is
            [k1, k2, k3], this is logically like SELECT k1, k2, k3 ... If this is None, return all.
        :return: A list containing dictionaries of the projected properties for matching entities.
        """
        result = None

        ds = self.context['data_service']
        final_result = {}

        result = ds.retrieve(self.database, self.collection, predicate, None)

        # Get on a path like /api/artists/id returns a single resource.
        # The collection query returns a list of matching resources.
        # Need to convert to a single element.
        #
        if result:
            final_result['data'] = []
            final_result['links'] = []

            for r in result:

                tmp = dict()
                tmp["data"] = r
                key = r['nconst']

                # This is pretty lazy and could be handled by config information.
                #
                tmp["links"] = [
                    {"rel": "primaryProfessions", "href": "/api/artists/" + key + "/primaryProfession"},
                    {"rel": "self", "href": "/api/artists/" + key}
                ]

                # Create the response model from the dictionary.
                result = ArtistRsp(**tmp)

                final_result['data'].append(result)

        return final_result


    def delete(self, predicate):
        """
        Query the data service/database and return matching items.

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection.
        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ...
        :return: A list containing dictionaries of the projected properties for matching entities.
        """
        raise NotImplementedError()

    def update(self, predicate, new_data):
        """
        Query the data service/database and return matching items.

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection.
        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ...
        :param new_data: The keys and values used to form the set statement in SQL.
        :return: A list containing dictionaries of the projected properties for matching entities.
        """
        raise NotImplementedError()

    def create(self, new_data):
        """
        Query the data service/database and return matching items.

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection.
        :param new_data: The data to insert into the table.
        :return: A list containing dictionaries of the projected properties for matching entities.
        """
        database = self.database
        collection = self.collection

        ds = self.context['data_service']

        res = ds.create(database, collection, new_data)

        if res == 1:
            result = new_data["nconst"]
        else:
            result = None

        return result


