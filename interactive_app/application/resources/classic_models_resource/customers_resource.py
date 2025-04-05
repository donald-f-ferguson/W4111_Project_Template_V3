from abc import ABC
import copy

# Use pydantic to define models and transfer objects.
from typing import List, Union
from pydantic import BaseModel

from datetime import date


from interactive_app.application.resources.base_application_resource import BaseResource, Link
from interactive_app.application.services.mongodb_data_service import MongoDBDataService

from interactive_app.application.resources.classic_models_resource.CustomerModel \
    import Contact, Customer, Address, Order, Detail


class CustomersResource(BaseResource):
    """
    """

    def __init__(self, context):
        super().__init__(context)

        self.db_service = context['data_service']
        self.collection = context["collection"]
        self.database = context["database"]

        self.predicate_type_map = {
            "number": int
        }

    def map_query_types(self, predicate):

        if self.predicate_type_map and predicate:
            new_result = copy.copy(predicate)

            for k,v in new_result.items():
                t = self.predicate_type_map.get(k, None)
                if t:
                    new_result[k] = t(v)
        else:
            new_result = None

        return new_result

    def retrieve(self, predicate, project):
        """
        Query the data service/database and return matching items.

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection.
        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ...
        :param project: A list of subsets of the entity's properties to return. That is, if the list is
            [k1, k2, k3], this is logically like SELECT k1, k2, k3 ...
        :return: A list containing dictionaries of the projected properties for matching entities.
        """
        new_predicate = self.map_query_types(predicate)

        res = self.db_service.retrieve(
            self.database, self.collection, new_predicate, project
        )

        result = []

        for r in res:
            if r.get("_id", None):
                # r["_id"] = str(r["_id"])
                del r["_id"]

            new_c = Customer(**r)
            result.append(new_c)

        return result


