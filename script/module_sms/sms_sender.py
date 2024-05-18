from .config_sms import *

import urllib.request
import urllib.parse
import json


def EmitMessageSmS(number_phone: str, text_message: str) -> tuple[bool, str]:
    params = {
        "login": login,
        "psw": password,
        "phones": number_phone,
        "mes": text_message,
        "cost": 0,
        "sender": sender,
        "fmt": 3
    }
    url = "http://smsc.ru/sys/send.php?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url) as response:
            answer = json.loads(response.read())
        if "error_code" in answer:
            return False, errors[answer["error_code"]]
        else:
            # СМС отправлен, ответ сервера
            return True, "Успешно отправлено сообщение"
        
    except Exception as error:
        return False, error
   