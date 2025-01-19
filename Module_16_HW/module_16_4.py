from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_message() -> list[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='Vasilii')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='22')]):
    if len(users) == 0:
        new_user = User(id=1, username=username, age=age)
        users.append(new_user)
    else:
        new_user = User(id=users[-1].id+1, username=username, age=age)
        users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='Vasilii')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='22')]):
    try:
        for i in range(len(users) + 1):
            if users[i].id == user_id:
                users[i].username = username
                users[i].age = age
                return users[i]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=0, le=100, description='Enter User ID', example='1')]):
    try:
        for i in range(len(users)+1):
            if users[i].id == user_id:
                del_user = users.pop(i)
                return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
