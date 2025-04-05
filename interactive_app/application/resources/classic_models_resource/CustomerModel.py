# Use pydantic to define models and transfer objects.
from typing import List, Union
from pydantic import BaseModel


class Contact(BaseModel):
    lastName: str
    firstName: str
    phone: str


class Address(BaseModel):
    line1: str
    line2: Union[str, None] = None
    city: str
    state: Union[str, None] = None
    country: str
    postalCode: str = None


class Detail(BaseModel):
    lineNumber: int
    quantityOrdered: int
    priceEach: float
    productCode: str


class Order(BaseModel):
    number: int
    orderDate: str
    requiredDate: str
    shippedDate: str = None
    status: str
    details: List[Detail] = None


class Customer(BaseModel):
    number: int
    name: str
    contact: Contact
    address: Address
    orders: List[Order] = None