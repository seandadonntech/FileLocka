import click
import inquirer
from cryptography.fernet import Fernet
import os

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()


def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def generate_key():
    key = Fernet.generate_key()
    return key

def get_file_choices():
    files = os.listdir(os.getcwd())
    return [file for file in files if file.endswith('.txt')]

@click.command()
@click.option('--decrypt', is_flag=True, help="Decrypt a message")
@click.option('--encrypt', is_flag=True, help="Encrypt a message")
def main(decrypt, encrypt):
    if decrypt:
        questions = [
            inquirer.Text('key_file', message="Enter the path to the key file"),
            inquirer.List('file',
                          message="Select the file to decrypt",
                          choices=get_file_choices())
        ]
        answers = inquirer.prompt(questions)

        with open(answers['key_file'], 'r') as file:
            key = file.read().strip().encode()

        file_path = os.path.join(os.getcwd(), answers['file'])

        with open(file_path, 'rb') as file:
            encrypted_message = file.read()

        try:
            decrypted_message = decrypt_message(key, encrypted_message)
            print(f"Decrypted Message: {decrypted_message}")
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
    elif encrypt:
        questions = [
            inquirer.Text('message', message="Enter your message: ")
        ]
        answers = inquirer.prompt(questions)

        key = generate_key()
        encrypted_message = encrypt_message(key, answers['message'])

        print(f"Encryption Key: {key.decode()}")
        print(f"Encrypted Message: {encrypted_message.decode()}")

        with open('encrypted_message.txt', 'wb') as file:
            file.write(encrypted_message)
            file.write(key.decode())
    else:
        print("Please provide either --decrypt or --encrypt option")

if __name__ == "__main__":
    main()