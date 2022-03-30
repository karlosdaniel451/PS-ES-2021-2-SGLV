from random import choice, random

from fastapi import FastAPI, Path, Query, Response, status, HTTPException, Depends
from pydantic import BaseModel, EmailStr

from src.models.car import Car, Category
from src.ad_hoc_cars import ad_hoc_cars_list

app = FastAPI()


class CommonQueryParams:
    #def __init__(self, q: str | None = None, skip: int = 0, limit : int = 100):
    def __init__(self, q: str | None = None, start: int = 0, limit : int = 0):
        self.q = q
        self.start = start 
        self.limit = limit

@app.get('/')
async def root():
    return {'message': 'Hello, World!'}


@app.get('/cars/', response_model=list[Car], tags=['cars'])
async def read_car(category: Category = Query(None, description='Category of cars to be searched'),
                   city: str = Query(None, description='City of cars to be searched'),
                   commons: CommonQueryParams = Depends(CommonQueryParams)):

    # found_cars = [
    #     car for car in ad_hoc_cars_list if (
    #         category is None or category == car.category) and (
    #         city is None or city.lower() in car.city.lower())]

    # if not found_cars:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No cars were found with the given category and city')

    # return found_cars
    if commons.limit == 0:
        commons.limit = len(ad_hoc_cars_list)

    return ad_hoc_cars_list[commons.start:commons.limit+1]


@app.get('/cars/random/', response_model=Car, tags=['cars'])
async def read_random_car(q: str | None = None):
    """
    Read a random car from the list of all cars.
    """
    #random_car = ad_hoc_cars_list[randint(0, len(ad_hoc_cars_list - 1))]
    random_car = choice(ad_hoc_cars_list)

    # return {'random_car': random_car}
    return random_car


@app.get('/cars/{car_code}/', response_model=Car, tags=['cars'])
async def read_car_by_code(response: Response, car_code: int = Path(..., title='The code of the car to get', ge=1, le=2**32)):
    found_cars = [car for car in ad_hoc_cars_list if car.code == car_code]

    if found_cars:
        # return {'car': found_cars[0]}
        return found_cars[0]

    #response.status_code = status.HTTP_404_NOT_FOUND
    # return {'error': f'There is no car with code {car_code}'}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'There is no car with code {car_code}')


@app.post('/cars/',
          response_model=Car,
          status_code=status.HTTP_201_CREATED,
          tags=['cars'],
          response_description='The created car')
async def create_car(car: Car):
    ad_hoc_cars_list.append(car)

    return car


@app.put('/cars/{car_code}/', response_model=Car, tags=['cars'], response_description='The new data of the updated car')
async def update_car(car_code: int, car: Car):
    """
    Update a car with code equals to `car_code`.
    """

    new_car_data = car

    try:
        #new_car_data.uuid = ad_hoc_cars_list[ad_hoc_cars_list.index(car)].uuid
        car_index = ad_hoc_cars_list.index(car)
        new_car_data.code = ad_hoc_cars_list[car_index].code
        ad_hoc_cars_list[car_index] = new_car_data

        return new_car_data
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'There is no car with code {car_code}')



class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str) -> str:
    return 'supersecret' + raw_password


def fake_save_user(user_in: UserIn) -> UserInDB:
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print('User saved! ..not really')
    return user_in_db


@app.post('/users/',
          response_model=UserOut,
          status_code=status.HTTP_201_CREATED,
          tags=['users'],
          response_description='The created user')
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
