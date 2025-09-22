def match_words(words):
    ctr = 0
    empty_list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            empty_list.append(word)
            ctr += 1
    return ctr
count = match_words(['abc', 'xyz', 'aba', '1221'])
print(count)