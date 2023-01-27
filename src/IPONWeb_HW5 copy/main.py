#Task1 Write a Python program to create a new dictionary by extracting the mentioned keys
# from the below dictionary.


def create_new_dict(d: dict, l):
    new_d = dict()
    for i in d:
        if i in l:
            new_d[i] = d[i]
    return new_d


# print(create_new_dict({"a": 1, "b": 2, "c": 3}, ["b", "a"]))


#Task2 Get the key of a minimum value from the following dictionary.


def dict_min_key(d: dict):
    l = list(d.items())
    min_value = l[0][1]
    min_key = l[0][0]
    for i in l:
        if i[1] < min_value:
            min_value = i[1]
            min_key = i[0]
    return min_key


# print(dict_min_key({"a": 10, "b": 2, "c": 3}))


#Task4 Write a Python program to copy the contents of a file to another file


def copy_from_other_file(string1, string2):
    f1 = open(string1, "r")
    content1 = f1.read()
    f1.close()
    f2 = open(string2, "w")
    f2.write(content1)
    f2.close()


# copy_from_other_file("file1.txt", "file2.txt")


#Task5 Write a Python program to count the frequency of words in a file


def frequency_of_words(file_name: str):
    f = open(file_name, "r")
    words_list = f.read().split()
    f.close()
    d = {}
    for i in words_list:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] = d[i] + 1
    return d


# print(frequency_of_words("frequency.txt"))


#Task6 Write a Python program to read last n lines of a file


def read_last_lines(file_name, n):
    f = open(file_name, "r")
    l = f.read().split("\n")
    for i in range(len(l) - n - 1, len(l) - 1):
        print(l[i])


# read_last_lines("file1.txt", 2)


