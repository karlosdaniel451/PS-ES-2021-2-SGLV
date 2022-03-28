from enum import Enum

from pydantic import BaseModel


class Fuel(str, Enum):
    gasoline = 'gasoline'
    ethanol = 'ethanol'
    diesel = 'diesel'
    flex = 'flex'
    hybrid = 'hybrid'


class Category(str, Enum):
    standard = 'standard'
    sport = 'sport'
    van = 'van'


class Car(BaseModel):
    code: int
    brand: str
    model: str
    year: int
    category: Category | None = Category.standard
    fuel: Fuel
    value: float | None = None
    city: str
