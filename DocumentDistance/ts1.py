import string
import math

def read_file(filename):
    f = open(filename, 'r')
    return f.read()

def get_words_from_line_list(text):
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list

def count_frequency(word_list):
    D = {}
    for new_word in word_list:

        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1

    return D

def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    return freq_mapping

def inner_product(D1,D2):
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

def vector_angle(D1,D2):
    numerator = inner_product(D1,D2)
    denominator = math.sqrt(inner_product(D1,D1)*inner_product(D2,D2))
    return math.acos(numerator/denominator)

file = open('./01_input.in', 'r')
translation_table = string.maketrans(string.punctuation + string.uppercase,
                                     " "*len(string.punctuation)+string.lowercase)

while True:
    filename_1 = file.readline().rstrip()
    filename_2 = file.readline().rstrip()
    if not filename_1 or not filename_2:
        break
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)

    print ("The distance between the documents is: %0.6f" % distance)

file.close()
