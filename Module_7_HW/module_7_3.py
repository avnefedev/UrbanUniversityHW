class WordsFinder:
    char = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file):
        self.file_names = [i for i in file]

    def get_all_words(self):
        all_words = dict()
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                word = file.read().lower()
                for k in self.char:
                    word = word.replace(k, '')
                all_words[i] = word.split()
        return all_words


    def find(self, word):
        words = dict()
        for key, value in self.get_all_words().items():
            words[key] = value.index(word.lower()) + 1
        return words

    def count(self, word):
        words = dict()
        for key, value in self.get_all_words().items():
            words[key] = value.count(word.lower())
        return words

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('test_file1.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('test_file2.txt')
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

finder1 = WordsFinder('test_file3.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
