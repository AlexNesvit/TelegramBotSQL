from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    regName = State()
    regPhone = State()