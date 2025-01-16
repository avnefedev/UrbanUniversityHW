from fastapi import FastAPI

app = FastAPI()


@app.get('/user/admin')
async def admin():
    return 'Вы вошли как администратор'


@app.get('/user/')
async def user_in(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, возраст: {age}'


@app.get('/user/{user_id}')
async def user_in(user_id: str):
    return f'Вы вошли как пользователь №{user_id}'


@app.get('/')
async def root():
    return 'Главная страница'
