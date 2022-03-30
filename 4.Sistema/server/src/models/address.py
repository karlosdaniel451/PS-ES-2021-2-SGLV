from enum import Enum

from pydantic import BaseModel, Field

class State(str, Enum):
    acre = 'Acre'
    alagoas = 'Alagoas'
    amapa = 'Amapá' 
    amazonas = 'Amazonas'
    bahia = 'Bahia'
    ceara = 'Ceará'
    distrito_federal = 'Distrito Federal'
    espirito_santo = 'Espírito Santo'
    goias = 'Goiás'
    maranhao = 'Maranhão'
    mato_grosso = 'Mato Grosso'
    mato_grosso_do_sul = 'Mato Grosso do Sul'
    minas_gerais = 'Minas Gerais'
    para = 'Pará'
    paraiba = 'Paraíba'
    parana = 'Paraná'
    pernambuco = 'Pernambuco'
    piaui = 'Piauí'
    rio_de_janeiro = 'Rio de Janeiro'
    rio_grande_do_norte = 'Rio Grande do Norte'
    rio_grande_do_sul = 'Rio Grande do Sul'
    rondonia = 'Rondônia'
    roraima = 'Roraima'
    santa_catarina = 'Santa Catarina'
    sao_paulo = 'São Paulo'
    sergipe = 'Sergipe'
    tocantins = 'Tocantins'


class Address(BaseModel):
    street: str = Field(..., max_length=100)
    number: int = Field(0)
    district: str = Field(..., max_length=100)
    city: str = Field(..., max_length=100)
    state: State
    zip_code: str = Field(..., min_length=8, max_length=8)

