from enum import Enum
from datetime import date, datetime
from multiprocessing.connection import wait
from uuid import UUID, uuid4

from pydantic import BaseModel, Field



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
    #uuid: UUID = Field(default_factory=uuid4)
    # updated: datetime = Field(default_factory=datetime.utcnow)
    code: int = Field(..., ge=1, le=2**32)
    brand: str = Field(..., max_length=100)
    model: str = Field(..., max_length=100)
    year: int = Field(..., ge=2010, le=date.today().year+1)
    category: Category | None = Category.standard
    fuel: Fuel
    seats: int = Field(4, ge=1)
    #acessories: list[str] = Field(None, unique_items=True)
    accessories: set[str] = set()
    value_in_cents: float | None = None

    def __eq__(self, other) -> bool:
        return self.code == other.code

            