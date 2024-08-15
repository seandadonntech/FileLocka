import click
import inquirer
from cryptography.fernet import Fernet
import os
from pathlib import Path

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
    files = Path.cwd().glob('*.txt')
    return [file.name for file in files]

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

        try:
            with open(answers['key_file'], 'rb') as file:
                key = file.read().strip()

            file_path = os.path.join(os.getcwd(), answers['file'])

            with open(file_path, 'rb') as file:
                encrypted_message = file.read()

            decrypted_message = decrypt_message(key, encrypted_message)
            print(f"Decrypted Message: {decrypted_message}")

        except Exception as e:
            print(f"An error occurred during decryption: {e}")

    elif encrypt:
        questions = [
            inquirer.Text('message', message="Enter your message:")
        ]
        answers = inquirer.prompt(questions)

        try:
            key = generate_key()
            encrypted_message = encrypt_message(key, answers['message'])

            key_file_path = 'encryption_key.key'
            message_file_path = 'encrypted_message.txt'

            with open(key_file_path, 'wb') as key_file:
                key_file.write(key)

            with open(message_file_path, 'wb') as message_file:
                message_file.write(encrypted_message)

            print(f"Encryption Key saved to: {key_file_path}")
            print(f"Encrypted Message saved to: {message_file_path}")

        except Exception as e:
            print(f"An error occurred during encryption: {e}")

    else:
        print("Please provide either --decrypt or --encrypt option")

if __name__ == "__main__":
    main()
