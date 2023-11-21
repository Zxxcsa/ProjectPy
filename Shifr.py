def Encrypt(let: str, shift: int) -> str:
    """Функция, возвращающая символ let со сдвигом shift(по алфавиту, сохраняя резистр)"""

    i = ord(let)
    if 65 <= i <= 90:
        i -= 65
        i = (i + shift) % 26
        i += 65
    elif 97 <= i <= 122:
        i -= 97
        i = (i + shift) % 26
        i += 97
    return chr(i)

def Shift(shift: int, flag: bool) -> int:
    """Функция, возвращающая по коду передаваемого символа (shift) какой сдвиг о"""
    if 97 <= shift <= 122:
        shift -= 32
    shift -= 65
    if flag:
        shift *= - 1
    return shift

class Shifr:
    """Класс для шифра"""

    def __init__(self, vvod: str):
        self.vvod = vvod

    def Cezare(self, shift: int, flag: bool) -> str:
        """Функция, возвращающая сроку зашифрованную шифром Цезаря (при flag == false) или дешифрованную им (при flag == true) со сдвигом shift"""
        vivod = ''
        shift = shift % 26
        if flag:
            shift *= - 1
        for i in self.vvod:
            vivod += Encrypt(i, shift)
        return vivod

    def Viginer(self, key: str, flag: bool) -> str:
        """Функция, возвращающая сроку зашифрованную шифром Виженера (при flag == false) или дешифрованную им (при flag == false) с ключём key"""
        vivod = ''
        count = 0
        ln = len(key)
        for i in self.vvod:
            i_ord = ord(i)
            if i_ord < 65 or 90 < i_ord < 97 or 122 < i_ord:
                vivod += i
                continue
            shift = Shift(ord(key[count % ln]), flag)
            vivod += Encrypt(i, shift)
            count += 1
        return vivod

    def Vernam(self, key: str) -> str:
        """Функция, возвращающая сроку зашифрованную шифром Вернама (при flag == false) или дешифрованную им(при flag == false) с ключём key"""
        vivod = ''
        count = 0
        ln = len(key) - 1
        for i in self.vvod:
            i_ord = ord(i)
            if (i_ord < 65 or 90 < i_ord < 97 or 122 < i_ord):
                vivod += i
                continue  
            buf = (Shift(ord(i), False)) ^ (Shift(ord(key[count % ln]), False))
            vivod += chr(buf + 65)
            count += 1
        return vivod

    def HackCezare(self) -> list:
        """Функция, возвращающая список из наиболее вероятных дешифровок текста шифром Цезаря методом частичного анализа"""
        buf = []
        hack = []
        stat = [0] * 26
        count = 0
        for i in self.vvod:
            let = Shift(ord(i), False)
            if (0 <= let <= 25):
                stat[let] += 1
                count += 1
        var = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6,97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07]
        for i in range(26):
            stat[i] *= 100 / count
        for i in range(26):
            k = 0
            min = 101
            for j in range(26):
                if abs(var[i] - stat[j]) < min:
                    min = abs(var[i] - stat[j])
                    k = j
            shift = i - k
            if shift in buf:
                continue
            buf.append(shift)
            vivod = ''
            for j in self.vvod:
                vivod += Encrypt(j, shift)
            hack.append(vivod)
        return hack
