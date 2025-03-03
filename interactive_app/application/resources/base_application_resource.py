#
# An abstract base class for all resources.
# The simplifies development in some cases because we can code to the base class.
#

# Enable Abstract Base Class
# https://www.educative.io/answers/what-is-the-abstract-base-class-in-python
#
from abc import ABC

import copy

# Use pydantic, especially for OpenAPI/models, type hints, ... ...
from typing import List, Union
from pydantic import BaseModel
from typing import Any, List


#
# The Links section for a HATEOAS REST response. https://en.wikipedia.org/wiki/HATEOAS
# There are many versions or styles for implementing HATEOAS. Different applications and sites
# implement differently. The key requirement is that related applications follow the same
# patter and design options.
#
class Link(BaseModel):
    # How is the resource related to the current resource?
    rel: str
    # The link tp the related resource.
    href: str


#
# A response to a GET returns the data/resources and an array of links to related resources.
# The data is the resource, which may be a single resources or a collection/array of resources.
#
class ResourceResponse(BaseModel):
    data: Any
    links: List[Link]


#
# A response to a GET returns that returns a set of values.
#
class QueryResourceResponse(BaseModel):
    data: List[ResourceResponse]
    links: List[Link]


class BaseResource(ABC):
    """
    The blueprint for REST resources.
    """

    def __init__(self, context):
        """

        :param context: A dictionary with references to dependencies and configuration that this implementation
            requires. This is a simple form of the dependency injection design pattern.
        """
        super().__init__()

        # The context is passed by reference. Make a copy to prevent changes from affecting the resource.
        self.context = copy.deepcopy(context)

    def get_by_id(self, id_string: str, requested_attributes: list = None) -> ResourceResponse:
        """
        In this model, all resources are in a collection, which itself is a resource. This class implements
        the collection. The id_string identifies a specific resource in the collection. A example for a versioned
        document might be: /documents/{documentid_versionno}

        This represents a composite key in the relational sense, i.e. two attributes form the primary key.

        request_attributes is a subset of the resources attributes to return. This is like the SELECT C1, C2, ...
        concept in SQL.

        In the simple cases, much of the implementation pattern is the same for all resources. Simply call the
        data service.

        :param id_string: The ID string.
        :param requested_attributes: A list of top-level attributes to return.
        :return: The response with links.
        """

        data_service = self.context["data_service"]
        database = self.context["database"]
        collection = self.context["collection"]
        id_attributes = self.context["id_attributes"]

        # Break the potentially complex key into a list of values.
        key_values = id_string.split("_")

        # Get the corresponding attribute names.
        key_attributes = self.context["key_attributes"]

        # Convert to a generic retrieve query.
        template = dict(zip(key_attributes, key_values))

        result_data = data_service.retrieve(
            database,
            collection,
            template,
            requested_attributes
        )

        # Call the method to add the links.
        full_result = self.get_links(result_data)

        return full_result

    def delete(self, template: dict) -> Union[int, None]:
        """
        Perform a DELETE on the resources matching the query parameters.

        :param template: A dictionary of key,value pairs containing the query parameters and values.
        :return: A count of the resources deleted.
        """
        raise NotImplementedError

    def get(self, template: dict) -> QueryResourceResponse:
        """
        Perform a GET with query parameters.

        :param template: A dictionary of key,value pairs containing the query parameters and values.
        :return: A QueryResourceResponse, which is the list of matching resources and the Links for the query result.
        """
        raise NotImplementedError

    def post(self, new_resource: BaseModel) -> str:
        """
        Perform a POST to create a new resource.

        :param new_resource: The data for the new resource.
        :return: URL to the created instance.
        """
        raise NotImplementedError

    def put(self, template: dict, new_resource: BaseModel) -> str:
        """
        Perform a POST to create a new resource.

        :param new_resource: The data for the new resource.
        :return: URL to the created instance.
        """
        raise NotImplementedError








