import re

def cleanword(word):
    return ''.join(c for c in word if c.isalnum())

def has_dashdash(word):
    return '--' in word

def extract_words(phrase):
    if has_dashdash(phrase):
        phrase = re.sub('--', ' ', phrase)

    unclean_words = [s.lower() for s in phrase.split()] 

    return list(map(cleanword, unclean_words))

def wordcount(word, words):
    return words.count(word)

def wordset(words):
    words_list = list(set(words))
    words_list.sort()
    return words_list

def longestword(words):
    if len(words) == 0:
        return 0
    return max([len(x) for x in words])