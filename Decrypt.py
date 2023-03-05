# Import all from Encrypt.py file
# from Encrypt import *
# Install requirements!!!
from colorama import Fore


# HexEncrypting class heir
# If you wont to heir class from Encrypt.py file put your class Name to Decrypt class
class Decrypt():
    def __init__(self):
        self.row_input = []
        self.numbers = []
        self.result = []
        self.abc = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                    13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                    24: 'x', 25: 'y', 26: 'z', 27: ' '}

        print("Select language (type number of language): \t\n 1. Russian \t\n 2. English")
        self.lang_input = input('\t')

        if self.lang_input == '1':
            for i in range(1, 17):
                self.get_input = input(Fore.BLUE + 'Напишите свой HEX код по одной нажимая ввод: ')
                if self.get_input == ' ':
                    print(Fore.RED + 'Пустая строка не является доступом. Попробуйте еще раз!' + Fore.RESET)
                    break
                else:
                    pass
                self.row_input.append(self.get_input)
            print(Fore.YELLOW + 'Ваш HEX код: \t', self.row_input)

        elif self.lang_input == '2':
            for i in range(1, 17):
                self.get_input = input(Fore.BLUE + 'Enter 16 digits of HEX code 1 to 1 with pressing enter: ')
                if self.get_input == ' ':
                    print(Fore.RED + 'Empty string is not access. Try again!' + Fore.RESET)
                    break
                else:
                    pass
                self.row_input.append(self.get_input)
            print(Fore.YELLOW + 'Your HEX code: \t', self.row_input)

        else:
            print(Fore.RED + 'Wrong input! Try again.\t\nНерпавильное значение! Попробуйте заново!')

    # Checker input function Rus and Eng
    def CheckerRus(self):
        row_input = self.row_input

        for i in row_input:
            if i in ' ':
                print(Fore.RED + 'Пустая строка не является доступом. Пожалуйста, попробуйте еще раз!' + Fore.RESET)
                row_input.clear()
            else:
                pass

        for i in row_input:
            if 2 < len(i):
                print(Fore.RED + 'Ошибка. Длина одной цифры не должна превышать 2 (Длина цифр 2!)' + Fore.RESET)
                row_input.clear()
            else:
                pass

    def CheckerEng(self):
        row_input = self.row_input

        for i in row_input:
            if i in ' ':
                print(Fore.RED + 'Empty string is not access. Please try again!' + Fore.RESET)
                row_input.clear()
            else:
                pass

        for i in row_input:
            if 2 < len(i):
                print(Fore.RED + 'Error. Length of one digits should not exceed (Digits length 2!)' + Fore.RESET)
                row_input.clear()
            else:
                pass

    # Decrypting inputted HEX code
    def Decrypting(self):

        # Alphabetical numbers of hex code list
        numbers = self.numbers
        # Finish result list
        result = self.result

        for i in self.row_input:
            r = int(i, 16)
            numbers.append(r)

        if self.lang_input == '1':
            print(Fore.LIGHTGREEN_EX + 'Нумерация в алфавите : ', numbers)
        elif self.lang_input == '2':
            print(Fore.LIGHTGREEN_EX + 'Alphabetical numbering :) : ', numbers)

        # Getting value from dictionary of ABC
        def get_val():
            for i in numbers:
                if i in self.abc:
                    res = self.abc.get(i)
                    result.append(res)

        get_val()
        one_line = ''.join([''.join(sub) for sub in result])

        if self.lang_input == '1':
            print(Fore.LIGHTGREEN_EX + 'Ваша зашифрованная строка расшифрована :) : \t' + Fore.RED + one_line)
        elif self.lang_input == '2':
            print(Fore.LIGHTGREEN_EX + 'Your encrypted string decrypted :) : \t' + Fore.RED + one_line)

    # Language selector
    def Lang(self):
        if self.lang_input == '1':
            dec.CheckerRus()
            dec.Decrypting()

        elif self.lang_input == '2':
            dec.CheckerEng()
            dec.Decrypting()


dec = Decrypt()
dec.Lang()
