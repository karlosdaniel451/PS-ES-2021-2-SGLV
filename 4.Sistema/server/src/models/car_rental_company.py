from src.models.address import Address
from src.models.car import Car

from pydantic import BaseModel, Field

class CarRentalCompany(BaseModel):
    name: str = Field(..., max_length=200)
    address: Address
    cnpj: str = Field(..., min_length=11, max_length=11)
    secret_code: str = Field(..., min_length=8, max_length=15)
    cars: set[Car] = set()
