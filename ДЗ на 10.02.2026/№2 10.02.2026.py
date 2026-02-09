def ask_password():
    password = "password"
    attempts = 3
    for _ in range(attempts):
        user_input = input().strip()
        if user_input == password:
            print("Пароль принят")
            return
    print("В доступе отказано")


