from Shifr import Shifr

if __name__ == "__main__":
    while True:
        with open(input("Имя входного файла: "), "r") as f:
            vvod = f.read()
        print(
        """Выберете шифр с которым будете работать:
        Шифр Цезаря - 0
        Шифр Виженера - 1
        Шифр Вернама - 2""")
        vid = int(input("Номер шифра: "))
        line = Shifr(vvod)
        way = input("Вы хотите зашифровать(Y) или дешифровать(n) файл: ")
        if way == 'Y':
            flag = False
        else:
            flag = True
        ok = True
        if vid == 0:
            if way == "n":
                if input("Вы знаете шаг шифровки(Y) или хотите дешифровать методом частотного анализа(n): ") == "n":
                    vivod = line.HackCezare()
                    ok = False
                else:
                    step = int(input("Шаг шифровки: "))
                    vivod = line.Cezare(step, flag)
            else:
                step = int(input("Шаг шифровки: "))
                vivod = line.Cezare(step, flag)
        if vid == 1:
            key = input("Кодовое слово: ")
            vivod = line.Viginer(key, flag)
        if vid == 2:
            key = input("Кодовое слово: ")
            vivod = line.Vernam(key)
        with open(input("Имя выходного файла: "), "w") as f:
            if ok:
                f.write(vivod)
            else:
                for i in vivod:
                    f.write(i + '\n' + '\n')
        if input("Хотите продолжить работу[Y/n]: ") != "Y":
            break
