from dotenv import set_key
from pathlib import Path
from os import path

def create_empty_config():
    config = {
        'SSB_TOKEN': 'Токен вашего бота',
        'SSB_DB': '',
        'SSB_HOST': 'localhost',
        'SSB_DB_PORT': 'Порт для подключения к БД (можно удалить строку, если порт не изменялся).',
        'SSB_DB_USER': 'Имя пользователя для подключеня к БД.',
        'SSB_DB_PASS': 'Пароль для подключения к БД',
        'SSB_ADM_CMD': 'Команда для получения прав администратора',
        'SSB_ADM_PWD': 'Пароль администратора',
        'SSB_SYS_CMD': 'Команда для получения прав супервайзера',
        'SSB_SYS_PWD': 'Пароль супервайзера',
        'SSB_LOG_PATH': '\logs',
        'SSB_ERR_MAIL': '',
        'SSB_DB_HOST': 'localhost'
    }
    filename = path.join('.env')
    envfile = Path(filename)
    envfile.open(mode="w", encoding="utf-8")
    for key, value in config.items():
        set_key(envfile, key, value)



if __name__ == '__main__':
    create_empty_config()
