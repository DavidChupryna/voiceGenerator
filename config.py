import configparser

config = configparser.ConfigParser()
config['LOGGING'] = {
    'level': 'INFO',
    'format': '%%(asctime)s - %%(name)s - %%(levelname)s - %%(message)s',
    'filename': 'log_file.txt',
    'filemod': 'w'
    }

config['TTS'] = {
    'URL': 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize',
    'IAM_TOKEN': 't1.9euelZqRy5mTkJGUy4nLlcuKns_Lju3rnpWay52RlYuSns_Hx8mZlYnNlZfl9PcpSwVP-e8MYwb43fT3aXkCT_nvDGMG-M3n9euelZrMmsnNkYyTkZeJyseLi86LkO_8xeuelZrMmsnNkYyTkZeJyseLi86LkL3rnpWaks7Lj8aWls7LiciTkZSSm4213oac0ZyQko-Ki5rRi5nSnJCSj4qLmtKSmouem56LntKMng.f7C5IsAAr-elBeh1u1Z20RIT65uls3L6ET5wkMWEZRwnQrbVoznXa5YuX6OikUBYP8eFQpOr3j2cgqInwVjVBg',
    'FOLDER_ID': 'b1gmco3nm6e4ud4orfv9'
    }

config['LIMITS'] = {
    'MAX_USER_TTS_SYMBOLS': '100',
    'MAX_USERS': '2',
    'MAX_TTS_SYMBOLS': '1000',
    }

bot_token = ('7067069927:AAHOp05z2tcqb5OQwvjwIu7y1QgLqhRgcSI')