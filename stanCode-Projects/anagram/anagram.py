"""
File: anagram.py
Name:Leon Hsieh
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
dic = []


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        s = input('Find anagrams for:')
        if s == EXIT:
            break
        else:
            anag_list = find_anagrams(s)
            print(f'{len(anag_list)} anagrams: {anag_list}')


def read_dictionary():
    global dic
    with open(FILE, 'r') as d:
        for line in d:
            new_line = line.strip()
            dic.append(new_line)


def find_anagrams(s):
    """
    :param s: the string user entered
    :return: list, containing the anagrams to the s that used typed in.
    """
    srh = []
    anagram_list = []
    for i in range(len(s)):
        srh.append((s[i], i))
    anag_list = find_anagrams_helper(srh, [], anagram_list)
    return anag_list


def find_anagrams_helper(srh, ans, anagram_list):
    global dic
    answer = ''
    for ele in ans:
        answer += ele[0]

    if len(ans) == len(srh):
        if answer in dic and answer not in anagram_list:
            print('Searching...')
            print(f'Found: {answer}')
            anagram_list.append(answer)
    else:
        for ele in srh:
            if ele not in ans and len(ans) < len(srh):
                ans.append(ele)
                test = ''
                for element in ans:
                    test += element[0]
                if has_prefix(test):
                    find_anagrams_helper(srh, ans, anagram_list)
                ans.pop()

    return anagram_list


def has_prefix(sub_s):
    """
    :param sub_s: the current string in the answer
    :return: boolean, deciding whether to keep searching or not
    """
    global dic
    for vocabulary in dic:
        if vocabulary.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
