"""
File: anagram.py
Name: Allen Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


# Global variables
dictionary = {}


def main():
    read_dictionary()
    while True:
        print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(s)


def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary[line.strip()] = [line.strip()]


def find_anagrams(s):
    """
    :param s: (str) A word needs to be found its anagrams
    :return: The function does not return any value
    """
    ans_l = []
    helper(s, '', ans_l)
    print(f'{len(ans_l)} anagrams: {ans_l}')


def helper(s, current_s, ans_l):
    if len(current_s) == len(s) and current_s in dictionary:
        if current_s not in ans_l:
            ans_l.append(current_s)
            print(f'Found: {current_s}')
            print('Searching...')
    else:
        for i in range(len(s)):
            ch = s[i]
            if count_ch(s, current_s, ch):
                current_s += ch
                if has_prefix(current_s):
                    helper(s, current_s, ans_l)
                    current_s = current_s[:-1]
                else:
                    current_s = current_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: (str) A string needs to be verified if there is any word in dictionary starting with
    :return: (bool) If there is any word in dictionary starting with sub_s
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


def count_ch(s, current_s, ch):
    count1 = 0
    count2 = 0
    for i in range(len(s)):
        if s[i] == ch:
            count1 += 1
    for j in range(len(current_s)):
        if current_s[j] == ch:
            count2 += 1
    if count1 == count2:
        return False
    elif count1 > count2:
        return True
    else:
        pass


if __name__ == '__main__':
    main()
