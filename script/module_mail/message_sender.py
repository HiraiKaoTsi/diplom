import smtplib
from email.message import EmailMessage
from .config_mail import *

from PyQt5 import QtCore
from collections.abc import Callable


class MessageSend(QtCore.QThread):

    signal_successful_sending = QtCore.pyqtSignal(str)
    signal_error_sending = QtCore.pyqtSignal(str)

    def __init__(self, function_successful: Callable[[str], None], function_error: Callable[[str], None]):
        super().__init__()

        self.signal_successful_sending .connect(function_successful)
        self.signal_error_sending.connect(function_error)

    def EmitMessage(self, email_recipient: str, message: str):
        msg = EmailMessage()
        msg["From"] = SENDER_ADDRESS
        msg["To"] = email_recipient
        msg.add_alternative(message, subtype="text")

        smtpObj = None
        try:
            smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            smtpObj.starttls()
            smtpObj.login(SENDER_ADDRESS, PASSWORD_SEND_ADDRESS)
            smtpObj.send_message(msg)
            print(1)
        except Exception:
            self.signal_error_sending.emit(
                "Во время отправки сообщение произошла ошибка, проверти правильно ли указан почтовый")
        finally:
            if smtpObj is not None:
                smtpObj.quit()
