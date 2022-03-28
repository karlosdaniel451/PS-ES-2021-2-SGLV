from src.models.car import Car, Category, Fuel

ad_hoc_cars_list: list[Car] = [
    Car(
        code=1,
        brand='Honda',
        model='Civic',
        year=2015,
        category=Category.standard,
        fuel=Fuel.gasoline,
        city='Goiânia'
    ),
    Car(
        code=2,
        brand='Chevrolet',
        model='Onix',
        year=2019,
        category=Category.standard,
        fuel=Fuel.gasoline,
        city='Anápolis'
    ),
    Car(
        code=3,
        brand='Volkswagen',
        model='Golf',
        year=2018,
        category=Category.standard,
        fuel=Fuel.gasoline,
        city='Goiânia'
    ),
    Car(
        code=4,
        brand='Chevrolet',
        model='Cruze',
        year=2015,
        category=Category.standard,
        fuel=Fuel.flex,
        city='Goiânia'
    ),
    Car(
        code=5,
        brand='Porsche',
        model='911',
        year=2019,
        category=Category.sport,
        fuel=Fuel.gasoline,
        city='Brasília'
    )
]
