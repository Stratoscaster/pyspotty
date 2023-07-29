from datetime import datetime


def get_time_as_str():
    time = datetime.now()
    text = time.strftime('%X %p')
    return text
