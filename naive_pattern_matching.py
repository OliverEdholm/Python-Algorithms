'''
Naive string matching

Implementation of a the Naive string matching algorithm, with a time
complecity of O(nm), where n is the length of the string and m is the length
of the pattern.

Oliver Edholm, 14 years old 2016-12-21 17:13
'''
# imports
from random import randint
from six.moves import xrange


# functions
def rand_char(alphabet):
    return alphabet[randint(0, len(alphabet) - 1)]

def rand_str(alphabet, str_len):
    return ''.join([rand_char(alphabet)
                    for _ in xrange(str_len)])


def naive_search(string, pattern):
    pattern_occurences = []
    for i in xrange(len(string)):
        for j in xrange(len(pattern)):
            if pattern[j] != string[i + j]:
                break
        else:
            pattern_occurences.append(i)

    return pattern_occurences


def main():
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    s = rand_str(alphabet, randint(8, 15))

    pattern_len = randint(2, 5)
    pattern_index = randint(0, len(s) - pattern_len - 1)

    pattern = s[pattern_index: pattern_index + pattern_len]
    corrupted_pattern = False
    if not randint(0, 4):  # 20% percent probability of corruption
        corrupted_pattern = True
        pattern = list(pattern)
        pattern[randint(0, len(pattern) - 1)] = rand_char(alphabet) 
        pattern = ''.join(pattern)

    print('string: {}\npattern: {}\ncorrupted pattern: {}'.format(s, pattern,
                                                                  corrupted_pattern))
    print('found pattern at following indexes: {}'.format(naive_search(s, pattern)))


if __name__ == '__main__':
    main()

