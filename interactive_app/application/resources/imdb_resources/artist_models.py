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


class Artist(BaseModel):
    """
    The model/data transfer object for a single entry from name_basics.

    Prof. Ferguson modified the format from the downloaded TSV file to produce a better
    relational/object schema.
    """

    # Primary key.
    nconst: str

    # TODO All of the name stuff might be better handled using an embedded class.
    # This would handle a name of the form "Dr. Donald Francis Ferguson IV (Darth Don)
    # See https://pypi.org/project/nameparser/ for what the fields mean.
    #
    title: Union[str, None] = None
    first_name: Union[str, None] = None
    middle_name: Union[str, None] = None
    last_name: str = None
    suffix: Union[str, None] = None
    nick_name: Union[str, None] = None

    birth_year: Union[int, None]
    death_year: Union[int, None] = None

    class Config:

        # The sample response for OpenAPI docs.
        #
        json_schema_extra = {
            "example": {
                "nconst": "nm0000001",
                "title": "Dr.",
                "first_name": "Boris",
                "middle_name": "Alexander",
                "last_name": "Badenov",
                "suffix": "III",
                "nick_name": "Bubba",
                "birth_year": "1900",
                "death_year": "2000"
            }
        }


class ArtistRsp(BaseModel):
    """
    A class implementing a HATEOAS pattern for return GET /artists?query string
    """

    # A data object with the Artist information.
    data: Artist

    # Links associated with the response.
    links: List[Link]

    class Config:
        json_schema_extra = {
            "example": {
                "data": {
                    "nconst": "nm0000001",
                    "title": "Dr.",
                    "first_name": "Boris",
                    "middle_name": "Alexander",
                    "last_name": "Badenov",
                    "suffix": "III",
                    "nick_name": "Bubba",
                    "full_name": "Boris Badenov",
                    "birth_year": "1900",
                    "death_year": "2000"
                },
                "links": [
                    {"rel": "primary_professions", "href": "/api/artists/nm0000293/primary_professions"},
                    {"rel": "primary_professions", "href": "/api/artists/nm0000293/titles"},
                    {"rel": "self", "href": "/api/artists/nm0000293"}
                ]
            }
        }


class ArtistsRsp(BaseModel):
    """
    Return a List of artists matching a query and links.
    """
    data: List[ArtistRsp]
    links: Union[List, None]

