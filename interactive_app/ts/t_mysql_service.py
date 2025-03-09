from interactive_app.application.services.mysql_data_service import MySQLDataService, MySQLDataServiceConfig


def get_service():
    config = MySQLDataServiceConfig()
    svc = MySQLDataService(config)
    return svc


def t_get_svc():
    svc = get_service()
    sql = "show databases";
    result = svc.run_q(sql, fetch=True)
    print("t_get_svc: result = \n", result)


def t_name_basics_template():
    template = {"primaryName": "Tom Hanks", "birthYear": 1956}
    svc = get_service()
    result = svc.retrieve("F24_IMDB_Raw", "name_basics", template, project=None)
    print("t_name_basics_template: result = \n", result)


if __name__ == "__main__":
    # t_get_svc()
    t_name_basics_template()