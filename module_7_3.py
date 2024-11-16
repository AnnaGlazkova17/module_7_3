from idlelib.iomenu import encoding


class WordsFinder: # принимает только список файлов
    def __init__(self, spisok):
        self.file_names = spisok
    def get_all_words(self):
        all_words = {}
        slova = []
        for name in self.file_names: # открывает файлы из списка по очереди
            with open(name, 'r', encoding = 'utf-8') as file:
                slova = []
                for line in file: # идем по файлу построчно
                    line = line.lower()
                    sim = [',', '.', '=', '!', '?', ';', ':', ' - '] # список для проверки
                    for i in sim:
                        line = line.replace(f'{i}',' ') # заменяем знаки препинания на пробел
                    slova.extend(line.split()) # добавляем в список слов новые, разделители по умолчанию
                all_words[name] = slova # формирование словаря

        return all_words
    def find(self, word): # метод поиска первой позиции этого слова
        all_words = self.get_all_words()
        word = word.lower()
        poz = {} # обнуляю переменную первая позиция слова в списке
        for key in all_words.keys(): # идем по ключам словаря
            print(key)
            znach = all_words[key] # вытскиваю список значений из словаря
            for value in znach: # идем по элементам списка
                if value == word: # поиск слова
                   poz.update({key: znach.index(value) + 1}) # добавляем в словарь название файла: номер позиции слова
        return poz
    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        kol_word = {}
        for key in all_words.keys():  # идем по ключам словаря
            znach = all_words[key]  # вытскиваю список значений из словаря
            kol_word[key] = znach.count(word) # добавляем в словарь название файла и сколько раз встречается word
        return kol_word



finder2 = WordsFinder(['test_file.txt'])
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))