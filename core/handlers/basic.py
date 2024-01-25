from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.settings import cursor, connection   # переменная подключения к базе
import database


async def start_command(message: Message): # привет
    builder = create_start_buttons()
    await message.answer("Приветственное сообщение", reply_markup=builder.as_markup())
    if not(await database.check_user(user_id = message.from_user.id)):
        await database.set_new_user(user_id= message.from_user.id,username= message.from_user.first_name)
 


