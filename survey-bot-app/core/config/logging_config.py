import logging
from logging.handlers import RotatingFileHandler

# настройка логирования

# определение шаблонов форматирования
brief_fmt = "[%(asctime)s.%(msecs)-03d] %(levelname)-8s : %(message)s"
date_fmt = "%d.%m.%Y в %H:%M:%S"
detailed_fmt = "[%(asctime)-s.%(msecs)-03d] %(levelname)-8s {(%(module)s->%(funcName)s:%(lineno)-d)} : %(message)s"

# настройка форматтеров
brief_formatter = logging.Formatter(
    fmt=brief_fmt,
    datefmt=date_fmt
)
detailed_formatter = logging.Formatter(
    fmt=detailed_fmt,
    datefmt=date_fmt
)
# настройка обработчиков
debug_handler = RotatingFileHandler(
    filename=".\logs\debug.log",
    mode="w",
    encoding="utf-8",
    backupCount=50,
    maxBytes=10 * 1024 * 1024
)
debug_handler.setFormatter(brief_formatter)
debug_handler.setLevel(logging.DEBUG)
error_handler = logging.FileHandler(
    filename=".\logs\error.log",
    mode="w",
    encoding="utf-8"
)
error_handler.setFormatter(detailed_formatter)
error_handler.setLevel(logging.WARNING)

# инициализация системы логирования
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        debug_handler,
        error_handler
    ]
)