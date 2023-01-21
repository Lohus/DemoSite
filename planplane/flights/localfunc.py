from datetime import datetime, timedelta, date
from pytz import timezone

def getStringDay():
    return str((datetime.now(timezone('Europe/Moscow')) + timedelta(hours=2)).date())