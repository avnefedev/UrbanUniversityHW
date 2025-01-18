from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_message() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='Vasilii')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='22')]):
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registred'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='Vasilii')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='22')]):
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is update'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    users.pop(str(user_id))
