class DictionaryIterator(object):
    def __init__(self, dict):
        self.dict = dict
        self.idx = 0
        self.keys = list(dict.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.keys):
            raise StopIteration
        else:
            key = self.keys[self.idx]
            value = self.dict[key]
            self.idx += 1
            return self.idx-1, key, value

my_dict = {}
count = int(input())
for i in range(count):
    my_input = input().split(' ')
    my_dict[my_input[0]] = my_input[1]
dict_it = DictionaryIterator(my_dict)
for idx, key, value in dict_it:
    print("index :", idx, " key :", key, "/ value :", value)
