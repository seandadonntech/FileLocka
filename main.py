import click
import inquirer
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

@click.command()
@click.option('--decrypt', is_flag=True, help="Decrypt a message")
def main(decrypt):
    if decrypt:
        
        questions = [
            inquirer.Text('key', message="Enter the encryption key"),
            inquirer.Text('encrypted_message', message="Enter the encrypted message")
        ]
        answers = inquirer.prompt(questions)

        key = answers['key'].encode()
        encrypted_message = answers['encrypted_message'].encode()

        try:
            decrypted_message = decrypt_message(key, encrypted_message)
            print(f"Decrypted Message: {decrypted_message}")
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
    else:
        # Ask for the message to encrypt
        questions = [
            inquirer.Text('message', message="Enter your message")
        ]
        answers = inquirer.prompt(questions)

        # Generate encryption key
        key = generate_key()
        encrypted_message = encrypt_message(key, answers['message'])

        # Print encrypted message and key
        print(f"Encryption Key: {key.decode()}")
        print(f"Encrypted Message: {encrypted_message.decode()}")

if __name__ == "__main__":
    main()
