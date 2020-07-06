import requests
import json

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'NOZhKTljnasv42AMGkHwJ9bxdVB8fIcgprXP3UYRyeLmt7zSQ6tJ9fIjvQihxVw1Dy6oPGgX5TmWed7s',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)gitg
send_sms("987654321","this is me")