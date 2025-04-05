# Simple starter project for FastAPI REST Microservice.
#
# Based on https://fastapi.tiangolo.com/tutorial/first-steps/
#

# Explicitly included uvicorn to enable starting within main program.
# Starting within main program is a simple way to enable running
# the code within the PyCharm debugger
#
import uvicorn

# Import JSON for mapping between Python dict classes and various uses of JSON.
# JSON is a lightweight approach to defining and exchanging data.
# https://www.json.org/json-en.html
import json


# The FastAPI server class.
#
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse

# See https://fastapi.tiangolo.com/tutorial/middleware/ for an explanation of middleware.
#
# See https://en.wikipedia.org/wiki/Cross-origin_resource_sharing for an explanation of CORS
#
from fastapi.middleware.cors import CORSMiddleware

# Added support for "static" web pages and other content.
# Static pages, e.g. HTML are in the path /static. For example,
# http://localhost:8001/static/index.html
#
from fastapi.staticfiles import StaticFiles

# FastAPI understands pydantic for defining "models" for REST API
# bodies. https://swagger.io/specification/
#
# An overview: https://medium.com/@nicola88/your-first-openapi-document-part-ii-data-model-52ee1d6503e0
#
# This is a form of the data transfer object pattern.
#
from typing import List, Union
from pydantic import BaseModel

# The implementation of the IMDB Artist Resource and data transfer object.
# Artist is the model definition.
# ArtistRsp extends the model with support for linked resources and a simple HATEOAS
# pattern (https://restfulapi.net/hateoas/)
#
from resources.imdb_resources.artist_resource import Artist, ArtistRsp, ArtistsRsp, ArtistResource

# from resources.got_resource.character_resource import Character, CharacterRsp, CharacterResource

# from resources.got_resource.episodes_resource import EpisodesResource

from resources.classic_models_resource.customers_resource import CustomersResource, Customer

from resources.db_book.student_resource import Student, StudentRsp

# Import a simple resource service factory. See the implementation for an explanation.
#
from service_factory import ServiceFactory
resource_factory = ServiceFactory()


# This is sloppy and lazy.
#
artist_resource = resource_factory.get_resource("ArtistResource")
student_resource = resource_factory.get_resource("StudentResource")
# character_resource = resource_factory.get_resource("CharacterResource")
# episodes_resource = resource_factory.get_resource("EpisodesResource")
customer_resource = resource_factory.get_resource("CustomersResource")


# Create the application/api server class.
#
app = FastAPI()

# This is sloppy. The CORS configuration should come from the environment.
# 12 - Factor Application design pattern suggest configuration should come from environment,
# not be hard coded.
#
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# See the explanation for static files and mount on the FastAPI documentation.
# https://fastapi.tiangolo.com/tutorial/static-files/
#
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """
    Basic test for root path. I added the "hint" to the returned message to guide students to
    find the OpenAPI document pages.

    :return: Simple JSON message.
    """
    return {
        "message": "Hello World",
        "hint": "Go to /docs to see the OpenAPI documentation."
    }


@app.get("/hello")
async def say_hello(name: str) -> str:
    """
    Implements the pass /hello
    :param name: A string as a query parameter. That is, /hello?name=some name
    :return: A JSON object in text format with the message saying hello.
    """
    return json.dumps({"message": f"Hello {name}"}, indent=2)


@app.get("/api/artists/{nconst}", response_model=ArtistRsp)
async def get_artist(nconst: str) -> ArtistRsp:
    """

    :param nconst: The IMDB nconst primary key for the information from name_basics.
        https://www.imdb.com/interfaces/
    :return:A data transfer object/OpenAPI model containing the response.
        TODO Should return 404 if not found.
    """

    result = artist_resource.get_by_key(nconst)
    return result


@app.get("/api/artists/", response_model=ArtistsRsp)
async def get_artists(
        last_name: str= None,
        first_name: str= None) -> ArtistsRsp:
    """

    :param last_name: The artist last name to find.
    :param first_name: First name to find.
    :return: A list of artists matching the predicate.
    """
    predicate = None

    if last_name or first_name:
        predicate = {}

        if last_name:
            predicate["last_name"] = last_name
        if first_name:
            predicate["first_name"] = first_name

    result = artist_resource.retrieve(predicate, None)
    return result


@app.put("/api/artists/{nconst}")
async def update_artist(new_artists: Artist) -> HTMLResponse:
    raise NotImplemented


@app.post("/api/artists/")
async def create_artist(new_artists: Artist) -> HTMLResponse:
    raise NotImplemented


@app.delete("/api/artists/{nconst}")
async def delete_artist(new_artists: Artist) -> HTMLResponse:
    raise NotImplemented


@app.get("/api/students/{ID}", response_model=StudentRsp)
async def get_student(ID: str) -> StudentRsp:
    """

    :param ID: The student's ID
        https://www.imdb.com/interfaces/
    :return:A data transfer object/OpenAPI model containing the response.
        TODO Should return 404 if not found.
    """

    # TODO Handle 404 and other errors.
    #
    result = student_resource.get_by_key(ID)
    return result

@app.get("/api/customers/{customer_number}", response_model=Customer)
async def get_customer(customer_number: str) -> Customer:
    """

    :param customer_number:
        https://www.imdb.com/interfaces/
    :return:A data transfer object/OpenAPI model containing the response.
        TODO Should return 404 if not found.
    """

    number = int(customer_number)
    result = customer_resource.retrieve({"number": number}, None)
    if result:
        result = result[0]
    return result


# Added the code below to enable running in PyCharm debugger.
# Modified the port from 8000 to 8001 because I often have multiple
# microservices running and need to spread over ports.
#
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
