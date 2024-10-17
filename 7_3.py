
class WordsFinder:
    def __init__(self , *args ):
        self.file_names = [*args]

    def get_all_words(self):
        super().__init__()
        all_words = {}
        for items in self.file_names:
            list_for_del = [',', '.', '=', '!', '?', ';', ':', ' - ' , '"' , '»' , '«']
            with open(items , encoding= 'utf-8') as file:
                list_1 = []
                for line in file:
                    for char in list_for_del:
                        line = line.replace(char , '').lower()
                    list_1 += line.split()
                all_words[items] = list_1
        return all_words


    def find(self , word):
        super().__init__()
        ret = {}
        if isinstance(word , str):
            dict_1 = self.get_all_words()
            for keys in dict_1.keys():
                for k in range(len(dict_1.keys())):
                    list_val = dict_1[keys]
                    if str(word.lower()) in list_val:
                        for i in range(len(list_val)):
                            if word.lower() == list_val[i]:
                                ret[keys] = i
            return ret



    def count(self , word):
        super().__init__()
        ret = {}
        if isinstance(word, str):
            dict_1 = self.get_all_words()
            for keys in dict_1.keys():
                for k in range(len(dict_1.keys())):
                    list_val = dict_1[keys]
                    if str(word.lower()) in list_val:
                        for i in range(len(list_val)):
                            c = 0
                            if word.lower() == list_val[i]:
                                c += 1
                                ret[keys] = c
        return ret





finder2 = WordsFinder('test_file.txt' , 'test_file1.txt' , 'test_file2.txt')
print(finder2.get_all_words())
print(finder2.find('на'))
print(finder2.count('на'))