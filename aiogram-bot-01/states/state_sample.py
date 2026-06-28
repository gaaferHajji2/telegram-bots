from aiogram.fsm.state import StatesGroup, State

class DialogBot(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()