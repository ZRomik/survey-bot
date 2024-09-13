from dotenv import set_key
from pathlib import Path
from os import path


def create_empty_config():
    config = {
        'SSB_TOKEN': 'Токен бота',
        'SSB_DB': 'Тип БД',
        'SSB_ADM_CMD': 'Команда для получения прав администратора',
        'SSB_ADM_PWD': 'Пароль администратора',
        'SSB_SYS_CMD': 'Команда для получения прав супервайзера',
        'SSB_SYS_PWD': 'Пароль супервайзера',
    }
    filename = path.join('.env')
    envfile = Path(filename)
    envfile.open(mode="w", encoding="utf-8")
    for key, value in config.items():
        set_key(envfile, key, value, quote_mode='never')


if __name__ == '__main__':
    create_empty_config()
