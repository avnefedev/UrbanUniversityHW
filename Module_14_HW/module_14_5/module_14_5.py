from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from set import API
from crud_functions import *

initiate_db()
# add_values()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


inl_kb = InlineKeyboardMarkup()
inl_button1 = KeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inl_button2 = KeyboardButton(text='Формулы расчета', callback_data='formulas')
inl_kb.add(inl_button1, inl_button2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button1, button2)
kb.add(button3, button4)

inl_menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
inl_menu_button1 = KeyboardButton(text='Product1', callback_data='product_buying')
inl_menu_button2 = KeyboardButton(text='Product2', callback_data='product_buying')
inl_menu_button3 = KeyboardButton(text='Product3', callback_data='product_buying')
inl_menu_button4 = KeyboardButton(text='Product4', callback_data='product_buying')
inl_menu.add(inl_menu_button1, inl_menu_button2, inl_menu_button3, inl_menu_button4)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    date = await state.get_data()
    print(date)
    add_user(date['username'], date['email'], date['age'])
    await message.answer('Регистрация прошла успешно')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inl_kb)


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age']
    await message.answer(f'Ваша норма каллорий {calories}')
    await state.finish()


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n'
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    all_prod = get_all_products()
    for i in all_prod:
        await message.answer(f'Название: Product{i[1]}, | Описание: описание {i[2]}| Цена: {i[3]}')
        with open(f'picture{i[0]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки.', reply_markup=inl_menu)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
