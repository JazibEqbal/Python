def palindrome_string(s):
    s2 = s.replace(' ', '')
    reversed_string = ''

    # for char in range(len(s2) - 1, -1, -1):
    #     reversed_string += s2[char]

    reversed_string = s2[::-1]

    if reversed_string.casefold() == s2.casefold():
        print(f'{s} is palindrome')
    else:
        print(f'{s} is not palindrome')

palindrome_string('Madam')
palindrome_string('Race car')


def check_anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    for i in s1:
        if i.isalpha():
            if s1.count(i) != s2.count(i):
                print('Not an anagram')
                break
    else:
        print('Anagram')

check_anagrams('snooze alarms', "alas, no more Z's")
