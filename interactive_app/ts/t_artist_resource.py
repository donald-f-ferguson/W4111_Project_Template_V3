from interactive_app.application.services.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
from interactive_app.application.resources.imdb_resources.artist_resource import ArtistResource
import json
from interactive_app.application.service_factory import ServiceFactory

service_factory = ServiceFactory()
artist_resource = service_factory.get_resource("ArtistResource")


def t1():

    a_resource = artist_resource
    result = a_resource.get_by_key("nm0000293")
    print("t1: result = \n", json.dumps(result.dict(), indent=2))


def t2():

    a_resource = artist_resource
    new_d = {"nconst": "xyzaa", "last_name": "Zaphod"}
    result = a_resource.create(new_d)
    print("t1: result = \n", result)


if __name__ == "__main__":
    t1()
    # t2()
