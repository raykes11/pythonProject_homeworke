def send_email( message, recipient, *, sender = "university.help@gmail.com"):
    recipient = str(recipient).upper().lower()
    sender = str(sender).upper().lower()
    if recipient.find('@') < 0 or sender.find('@') < 0:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif recipient[::-1].find('moc.') == 0 or recipient[::-1].find('ur.') == 0 or recipient[::-1].find('ten.') == 0:
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        elif sender[::-1].find('moc.') == 0 or sender[::-1].find('ur.') == 0 or sender[::-1].find('ten.') == 0:
            print(
                f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')