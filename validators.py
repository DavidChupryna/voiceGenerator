import math
from database import count_all_blocks
from config import config


def is_stt_block_limit(message, duration):
    user_id = message.from_user.id

    audio_blocks = math.ceil(duration / 15)
    all_blocks = count_all_blocks(user_id) + audio_blocks

    if duration >= 30:
        msg = "SpeechKit STT работает с голосовыми сообщениями меньше 30 секунд"
        return None, msg

    if all_blocks >= int(config['LIMITS']['MAX_USER_STT_BLOCKS']):
        msg = f"Превышен общий лимит SpeechKit STT {int(config['LIMITS']['MAX_USER_STT_BLOCKS'])}. Использовано {all_blocks} блоков. Доступно: {int(config['LIMITS']['MAX_USER_STT_BLOCKS']) - all_blocks}"
        return None, msg

    return audio_blocks, None
