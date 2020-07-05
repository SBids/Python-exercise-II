# 12. Create a function is_palindrome, to determine if a supplied word is the same if the letters are reversed


def is_palindrome(word):
    reverse_word = ''.join(reversed(word))
    if reverse_word == word:
        return "palindrome"
    else:
        return "not palindrome"


print(is_palindrome('dad'))
