def main():
    key = 9871
    key_check = input("Podaj kod: ")
    if int(key_check) == key:
        print("Prawidłowy kod")
    else:
        print("Nieprawidłowy kod")


if __name__ == '__main__':
    main()
