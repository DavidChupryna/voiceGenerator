import requests
from config import config


def send_request(text):
    iam_token = config['TTS']['IAM_TOKEN']
    folder_id = config['TTS']['FOLDER_ID']

    headers = {
        'Authorization': f'Bearer {iam_token}',
    }
    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'filipp',
        'folderId': folder_id,
    }
    response = requests.post(config['TTS']['URL'], headers=headers, data=data)

    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"

