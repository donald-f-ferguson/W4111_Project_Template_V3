import pymongo
from interactive_app.application.services.mongodb_data_service import MongoDBDataService
import interactive_app.app_secrets as app_secrets
from interactive_app.application.service_factory import ServiceFactory
import json

def get_data_service():
    mongo_db_svc = ServiceFactory().mongo_data_service
    return mongo_db_svc


def t1():

    svc = get_data_service()
    result = svc.run_find("F24_GoT", "characters",
                          filter={"characterName": "Sansa Stark"},
                          project={
                              "_id": 0,
                              "characterName": 1, "houseName": 1,
                              "characterImageThumb": 1,
                              "characterImageFull": 1,
                              "actorName": 1,
                              "actorLink": 1,
                              "royal": 1
                          })
    print("t1 result = \n", json.dumps(result, indent=2, default=str))

def t2():

    svc = get_data_service()
    result = svc.run_find("F24_GoT", "episodes",
                          filter={"seasonNum": 1, "episodeNum": 2},
                          project={
                              "_id": 0,
                              "seasonNum": 1, "episodeNum": 1, "episodeTitle": 1,
                              "episodeLink": 1,
                              "episodeTitle": 1, "episodeDescription": 1
                          })
    print("t1 result = \n", json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    t1()