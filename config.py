import configparser

config = configparser.ConfigParser()

config['LOGGING'] = {
    'level': 'INFO',
    'format': '%%(asctime)s - %%(name)s - %%(levelname)s - %%(message)s',
    'filename': 'log_file.txt',
    'filemod': 'w'
    }

config['STT'] = {
    'URL': 'https://stt.api.cloud.yandex.net/speech/v1/stt:recognize',
    'IAM_TOKEN': 't1.9euelZqQzZqKzsiQiZyLyJyclcqczO3rnpWay52RlYuSns_Hx8mZlYnNlZfl9PcCWW9O-e8CPhWB3fT3QgdtTvnvAj4Vgc3n9euelZqOns6JysfKlZKSlpOWkInJyu_8xeuelZqOns6JysfKlZKSlpOWkInJyr3rnpWayZzOy4zHlMyeycqZicyYyZ213oac0ZyQko-Ki5rRi5nSnJCSj4qLmtKSmouem56LntKMng.RQI4zc3btXXfz7I8LL_aEMAxFNjtQLVv3D3bcHtg9EU4bj1lcznLkm8AfnfMV1JUbhcwxVQBvqRkCSnVvL2fAA',
    'FOLDER_ID': 'b1gmco3nm6e4ud4orfv9'
    }

config['LIMITS'] = {
    'MAX_USERS': '2',
    'MAX_USER_STT_BLOCKS': '12',
    }


bot_token = '6873991240:AAHLs0o3pbZx0i5iZA4fE9FUCmA4DJ_p2W4'