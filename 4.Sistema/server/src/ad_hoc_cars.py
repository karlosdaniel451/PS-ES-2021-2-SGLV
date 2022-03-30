from src.models.car import Car, Category, Fuel
from src.models.address import Address

ad_hoc_cars_list: list[Car] = [
    Car(
        code=1,
        brand='Honda',
        model='Civic',
        year=2015,
        category=Category.standard,
        fuel=Fuel.gasoline,
        value_in_cents=7500000
    ),
    Car(
        code=2,
        brand='Chevrolet',
        model='Onix',
        year=2019,
        category=Category.standard,
        fuel=Fuel.gasoline,
    ),
    Car(
        code=3,
        brand='Volkswagen',
        model='Golf',
        year=2018,
        category=Category.standard,
        fuel=Fuel.gasoline,
    ),
    Car(
        code=4,
        brand='Chevrolet',
        model='Cruze',
        year=2015,
        category=Category.standard,
        fuel=Fuel.flex,
    ),
    Car(
        code=5,
        brand='Porsche',
        model='911',
        year=2019,
        category=Category.sport,
        fuel=Fuel.gasoline,
        seats=2,
        value_in_cents=40000000
    )
]

ad_hoc_cars_list[0].accessories.update(['Freio ABS', 'Teto solar'])
