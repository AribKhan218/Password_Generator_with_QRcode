import random
import os
import qrcode
from PIL import Image

CHARS = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"

def get_valid_length():
    while True:
        try:
            length = int(input("Enter your password length (8-50): "))
            if 8 <= length <= 50:
                return length
            print("Please enter a length between 8 and 50")
        except ValueError:
            print("Please enter a valid number")

def generate_password(length):
    return ''.join(random.choice(CHARS) for _ in range(length))

def save_qr_code(password):
    try:
        qr_text = f"Your Generated password is: {password}"
        img = qrcode.make(qr_text)
        path = os.path.join(os.getcwd(), "qrcode.png")
        img.save(path)
        return path
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

def main():
    password_length = get_valid_length()
    password = generate_password(password_length)
    print("Your generated password is:", password)

    while True:
        choice = input("Want to make your password QR code (y/n): ").lower()
        if choice == 'y':
            path = save_qr_code(password)
            if path:
                print("Your qrcode has been generated at", path)
            break
        elif choice == 'n':
            print("\nThanks for using!")
            break
        else:
            print("\nPlease enter 'y' or 'n'")

    print("\n" + "*" * 40 + "\n\nThank you for using our work\n\n" + "*" * 40)

if __name__ == "__main__":
    main()