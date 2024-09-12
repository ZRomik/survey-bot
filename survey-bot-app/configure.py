from dotenv import set_key
from pathlib import Path
from os import path


def create_empty_config():
    config = {
        'SSB_TOKEN': '',
        'SSB_DB': '',
        'SSB_ADM_CMD': '',
        'SSB_ADM_PWD': '',
        'SSB_SYS_CMD': '',
        'SSB_SYS_PWD': '',
    }
    filename = path.join('.env')
    envfile = Path(filename)
    envfile.open(mode="w", encoding="utf-8")
    for key, value in config.items():
        set_key(envfile, key, value, quote_mode='never')


if __name__ == '__main__':
    create_empty_config()
