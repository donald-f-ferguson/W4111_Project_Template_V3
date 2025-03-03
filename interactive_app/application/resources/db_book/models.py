#
# Implement the "model" for the student data in the "db_book" database.
# Pydantic, FastAPI and OpenAPI documentation explains the concept.
#

# Import Pydantic types.
#
from typing import List, Union
from pydantic import BaseModel


# Import the definition of a Links section for a HATEOAS resource.
#
from interactive_app.application.resources.base_application_resource import Link


class Student(BaseModel):
    """
    The model/data transfer object for a single entry from the database book student table.
    """

    # Primary key.
    ID: str
    last_name: str
    department_name: str
    total_credits: int

    class Config:

        # The sample response for OpenAPI docs.
        #
        json_schema_extra = {
            "example": {
                "ID": "00128",
                "last_name": "Zhang",
                "department_name": "Comp. Sci.",
                "total_credits": 102
            }
        }


class StudentRsp(BaseModel):
    """
    A class implementing a HATEOAS pattern for return GET /student/{ID}
    """

    # A data object with the Artist information.
    data: Student

    # Links associated with the response.
    links: List[Link]

    class Config:
        json_schema_extra = {
            "example": {
                "data": {
                    "ID": "00128",
                    "last_name": "Zhang",
                    "department_name": "Comp. Sci.",
                    "total_credits": 102
                },
                "links": [
                    {"rel": "self", "href": "/api/students/00128"},

                    # TODO Change this over time to a department ID instead of name.
                    #
                    {"rel": "department", "href": "/api/departments/Comp. Sci."}
                ]
            }
        }


class StudentsRsp(BaseModel):
    """
    Return a List of artists matching a query and links.
    """
    data: List[StudentRsp]

    # TODO Add links for pagination, etc.
    #
    links: Union[List, None]

