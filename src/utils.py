import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.config.config import settings


def send_email(receiver_email, subject, body):
    # Ваши данные
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD

    # Создание объекта MIMEMultipart
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Добавление текста письма
    message.attach(MIMEText(body, "plain"))

    # Отправка письма
    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
