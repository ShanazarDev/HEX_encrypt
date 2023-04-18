from colorama import Fore

# class AES, all algorithm
class HexEncrypting:
    # Inputs function
    def __init__(self):
        print("Select language (type number of language): \t\n 1. Russian \t\n 2. English")
        self.lang = input('\t')

        match self.lang:
            case '1':
                self.row_input = input(Fore.BLUE + 'Введите слово для шифрования в HEX (длина строки должна быть 16): ')
            case '2':
                self.row_input = input(Fore.BLUE + 'Enter your word for encrypting to HEX (string length should be 16): ')
            case _:
                print(Fore.RED + 'Wrong input! Try again.\t\nНерпавильное значение! Попробуйте заново!')

        self.rowed_input = []
        self.new_key = []
        self.row_ABC = []
        self.HEX_code = []
        self.HEX_line = []
        self.abc = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 
                    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' '}
        self.rowed_input.append(self.row_input.lower())

        for i in self.row_input:
            if i in str(list(range(1, 11))):
                if self.lang == '1':
                    print(Fore.RED + 'Только буквы, попробуйте еще раз!!!' + Fore.RESET)
                elif self.lang == '2':
                    print(Fore.RED + 'Only letters, try again!!!' + Fore.RESET)
            else:
                break


    # Scan input for validate
    def CheckingRus(self):
        while len(self.row_input) != 16:
            print(Fore.RED + 'Нужно ровно 16 букв (Пробел тоже символ)!' + Fore.RESET)
            self.row_input = input(Fore.BLUE + 'Попробуйте еще раз: ')
            self.rowed_input.clear()
            self.rowed_input.append(self.row_input.lower())

        else:
            print(Fore.RED + f'Принято: {self.rowed_input}' + Fore.RESET)

    def CheckingEng(self):

        while len(self.row_input) != 16:
            print(Fore.RED + 'Need 16 letters (Space 1 symbol)!' + Fore.RESET)
            self.row_input = input(Fore.BLUE + 'Try again: ')
            self.rowed_input.clear()
            self.rowed_input.append(self.row_input.lower())

        else:
            print(Fore.RED + f'Accept: {self.rowed_input}' + Fore.RESET)

    # Encrypt information
    def EncryptRus(self):
        b = str(self.rowed_input)
        d = b.strip("[]'")

        for i in d:
            self.new_key.append(i)

        # Get KEY form dictionaries
        def get_key(val):
            for KEY, value in self.abc.items():
                if val == value:
                    return KEY

        # Set what KEY need
        for x in self.new_key:
            if x in self.new_key:
                key = get_key(x)
                self.row_ABC.append(key)
            # Empty string
            elif x is None in self.new_key:
                key = get_key(x)
                self.row_ABC.append(key)

        print(Fore.MAGENTA + f'Алфавитный номер: {self.row_ABC}')

        for i in self.row_ABC:
            HEX = hex(i).upper()
            res = HEX.strip('0X')
            self.HEX_code.append(res)

        print(Fore.LIGHTGREEN_EX + f'HEX зашифрованное слово: {self.rowed_input} \t\n' + Fore.RESET + Fore.BLUE + 'Зашифрованная таблица HEX 4x4: ',end='')

        # 4x4 table HEX code
        for i in range(4):
            print(Fore.MAGENTA)
            print(f'{i+1} строка ---> {self.HEX_code[i*4:i*4+4]}')

        # One line string
        one_line = ' '.join([''.join(sub) for sub in self.HEX_code])
        self.HEX_line.append(one_line)
        print()
        print(Fore.BLUE + f'HEX без 4x4: {self.HEX_line}')

    def EncryptEng(self):
        b = str(self.rowed_input)
        d = b.strip("[]'")

        for i in d:
            self.new_key.append(i)

        # Get KEY form dictionaries
        def get_key(val):
            for KEY, value in self.abc.items():
                if val == value:
                    return KEY
        # Set what KEY need
        for x in self.new_key:
            if x in self.new_key:
                key = get_key(x)
                self.row_ABC.append(key)
            # Empty string
            elif x is None in self.new_key:
                key = get_key(x)
                self.row_ABC.append(key)

        print(Fore.MAGENTA + f'Alphabetical letter number: {self.row_ABC}')

        for i in self.row_ABC:
            HEX = hex(i).upper()
            res = HEX.strip('0X')
            self.HEX_code.append(res)

        print(Fore.LIGHTGREEN_EX + f'HEX encrypted word: {self.rowed_input} \t\n' + Fore.RESET + Fore.BLUE + 'Encrypted HEX 4x4 table: ', end='')

        # 4x4 table HEX code
        for i in range(4):
            print(Fore.MAGENTA)
            print(f'{i+1} string ---> {self.HEX_code[i*4:i*4+4]}')

        # One line string
        one_line  = ' '.join([''.join(sub) for sub in self.HEX_code])
        self.HEX_line.append(one_line)
        print()
        print(Fore.BLUE + f'HEX without 4x4: {self.HEX_line}')

    def Language(self):
        match self.lang:
            case '1':
                h.CheckingRus()
                h.EncryptRus()

            case '2':
                h.CheckingEng()
                h.EncryptEng()

# Run
if __name__ == '__main__':
    h = HexEncrypting()
    h.Language()
