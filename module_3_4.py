def single_root_words(*args):

    root_word, *other_words = args

    root_word = root_word.lower()
    
    same_words = []

    for word in other_words:
        word_lower = word.lower()
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)

    return same_words

result = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result)  