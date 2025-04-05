from interactive_app.application.services.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
from interactive_app.application.resources.classic_models_resource.customers_resource import CustomersResource
import json
from interactive_app.application.service_factory import ServiceFactory

service_factory = ServiceFactory()
customers_resource = service_factory.get_resource("CustomersResource")


def t1():

    a_resource = customers_resource
    result = a_resource.retrieve({"number": 103}, None)
    print("t1: result = \n", json.dumps(
        [d.dict() for d in result], indent=2))


if __name__ == "__main__":
    t1()
