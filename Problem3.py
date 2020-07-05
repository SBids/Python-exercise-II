# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

import re


def get_anagrams(text):
    word_list = re.sub("[^\w]", " ",  text).split()  # to remove all other signs like .! from the paragraph
    word_dict = {}
    for word in word_list:
        sorted_word = "".join(sorted(word))
        if sorted_word not in word_dict:
            word_dict[sorted_word] = [word]
        else:
            word_dict[sorted_word].append(word)

    result = []
    for item in word_dict.values():
        result.append(item)
    return result


paragraph = "This is paragraph to get the anagrams in the given  paragraph! ot ni hpapargra"
print(get_anagrams(paragraph))
