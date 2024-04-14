import configparser

config = configparser.ConfigParser()
config['LOGGING'] = {
    'level': 'INFO',
    'format': '%%(asctime)s - %%(name)s - %%(levelname)s - %%(message)s',
    'filename': 'log_file.txt',
    'filemod': 'w'
    }

config['TTS'] = {
    'URL': '',
    'IAM_TOKEN': '',
    'FOLDER_ID': 'b1gmco3nm6e4ud4orfv9'
    }

config['LIMITS'] = {
    'MAX_USER_TTS_SYMBOLS': '200',
    'MAX_USERS': '2',
    'MAX_TTS_SYMBOLS': '1000',
    }

bot_token = ''