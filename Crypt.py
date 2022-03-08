import cryptography.fernet as cf


def generate_key():
    message_key = cf.Fernet.generate_key()
    with open("key_code", 'wb') as key_file:
        key_file.write(message_key)

