import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    all_chars = lowercase + uppercase + digits + special
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    try:
        user_input = input("Введите желаемую длину пароля (по умолчанию 12): ")
        length = int(user_input) if user_input.isdigit() else 12
        password = generate_password(length)
        print(f"\nВаш сгенерированный пароль: {password}")
    except ValueError as e:
        print(f"Ошибка: {e}")
