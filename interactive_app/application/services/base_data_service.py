# Import support for abstract base classes.
#
# See https://www.educative.io/answers/what-is-the-abstract-base-class-in-python if you are unfamiliar with the
# concepts of abstract base classes.
#
from abc import ABC, abstractmethod

from typing import Union, List

#
# TODO Check that the doc strings are correct for automatic documentation generation, e.g. sphinx.
# https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
#


class BaseDataService(ABC):
    """
    A base class for defining implementations for create, retrieve, update and delete (CRUD) for databases and
    data sources supporting the application.
    """
    def __init__(self, config):
        """

        :param config: An object providing configuration information and dependencies. This is a very simple form
            of dependency injection (https://en.wikipedia.org/wiki/Dependency_injection).
        """

        # TODO I intentionally am not using protected or private properties because having public properties.
        # makes simple demos and code walk through easier.
        #
        # If you are not familiar with the concepts, see
        # https://www.tutorialsteacher.com/python/public-private-protected-modifiers
        #
        self.config = config

    @abstractmethod
    def get_connection(self, create=False):
        """
        Get a connection to the database/data service.

        :param create: Caching a connection and serially reusing is an option for performance. If create=True the method
            will not use a cached connection if it is implementing caching.
        :return: A connection to the database/dataservice.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self, database, collection, document) -> Union[None, str]:
        """

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection. The concrete implementation of
            the dataservice determines the mapping of the abstract concept of collection to the specific realization.
        :param document: The data to create/insert in dictionary format. The concrete dataservice converts to the representation
            of the underlying database.
        :return: A string representing the key/ID of the inserted/created database element, if any.
        """
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, database, collection, predicate=None, project=None):
        """
        Query the data service/database and return matching items.

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection. The concrete implementation of
            the dataservice determines the mapping of the abstract concept of collection to the specific realization.
        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ... If this is None, all documents in the commection match.
        :param project: A list of the entity's properties to return. That is, if the list is
            [k1, k2, k3], this is logically like SELECT k1, k2, k3 ...
        :return: A list containing dictionaries of the projected properties for matching entities.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, database, collection, document_update, predicate=None) -> Union[None, int]:
        """

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection. The concrete implementation of
            the dataservice determines the mapping of the abstract concept of collection to the specific realization.
        :param document_update: The new version of the data/document. A concrete data source MAY choose for this to be
            an incremental update or a complete overwrite.
        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ... If this is None, all documents in the commection match.
            This identifies the documents matched for update.
        :return: The number of documents updated. If the underlying database does not provide the information, it can
            return None.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, database, collection, predicate=None) -> Union[None, int]:
        """

        :param database: The database.
        :param collection: In MySQL, this would be a table. In MongoDB this is a collection. The concrete implementation of
            the dataservice determines the mapping of the abstract concept of collection to the specific realization.
        :param predicate: A dictionary of the form {k, v}. A entity matches if the resource's property v has
            value k, for all entries in the dictionary. That is, a match if logically
            k1 = v1 AND k2 = v2 AND ... ... If this is None, all documents in the commection match.
            This identifies the documents matched for deletion.
        :return: The number of documents deleted. If the underlying database does not provide the information, it can
            return None.
        """
        raise NotImplementedError

