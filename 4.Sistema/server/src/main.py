from random import choice, random

from fastapi import FastAPI, Path, Query, Response, status

from src.models.car import Car, Category
from src.ad_hoc_cars import ad_hoc_cars_list

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello, World!'}


@app.get('/cars/')
async def read_car(category: Category = Query(None, description='Category of cars to be searched'),
                   city: str = Query(None, description='City of cars to be searched')):

    found_cars = [
        car for car in ad_hoc_cars_list if (
            category is None or category == car.category) and (
            city is None or city.lower() in car.city.lower())]

    if found_cars:
        return {'cars': found_cars}

    return {'error:': 'No cars were found with the given category and city'}


@app.get('/cars/{car_code}/')
async def read_car_by_code(response: Response, car_code: int = Path(..., title='The code of the car to get', ge=1, le=2**32)):
    found_cars = [car for car in ad_hoc_cars_list if car.code == car_code]

    if len(found_cars) == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'There is no car with code {car_code}'}

    return {'car': found_cars[0]}


@app.get('/cars/random/')
async def read_random_car(q: str | None = None):
    #random_car = ad_hoc_cars_list[randint(0, len(ad_hoc_cars_list - 1))]
    random_car = choice(ad_hoc_cars_list)

    return {'random_car': random_car}


@app.post('/cars/')
async def create_car(car: Car):
    ad_hoc_cars_list.append(car)

    return car
