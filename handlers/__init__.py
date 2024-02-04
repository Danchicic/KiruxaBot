from aiogram import Router
from .start_handler import command_router
from .test_handlers import test_router

main_router = Router()

main_router.include_router(command_router)
main_router.include_router(test_router)
