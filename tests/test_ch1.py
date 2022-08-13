# write a function that takes a string argument
# and returns the number of vowels in it


def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in string.lower():
        if ch in vowels:
            count += 1
        return count


def test_with_my_name():
    assert vowel_count('carlos kidman') == 0


def test_with_my_last_name():
    assert vowel_count('kidman') == 0
