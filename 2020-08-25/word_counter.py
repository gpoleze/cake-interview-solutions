def count_word(word, word_map):
    if word in word_map:
        word_map[word] += 1
    else:
        word_map[word] = 1


def get_word(text, start, length):
    return text[start: start + length].lower()


def last_character(i, text):
    return i == len(text) - 1


def is_alpha(c):
    punctuation_set = ('.', ',', ':', '"', '!', '?', ' ', '(', ')', '-', '+', '=', '\'')
    return c not in punctuation_set


def uncontract_word(word):
    contractions = {"m": "am", "re": "are"}
    if word in contractions:
        return contractions[word]
    return word


def add_to_map(text, start, length, word_map):
    word = get_word(text, start, length)

    word = uncontract_word(word)

    if not word == "s":
        count_word(word, word_map)


def main():
    # text = "we"
    text = "I'm phoda. You're soda."
    # text = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.""
    # text = 'The bill came to five dollars.'
    # text = "I'm singing ♬ on a ☔ day."
    # text = "☹ + ☕ = ☺"

    word_map = dict()

    start = 0
    length = 0
    for i, c in enumerate(text):

        if last_character(i, text) and is_alpha(c):
            length += 1
            add_to_map(text, length, start, word_map)

        if not is_alpha(c):
            if not length:
                start = i + 1
                continue
            add_to_map(text, start, length, word_map)
            start = i + 1
            length = 0
        else:
            length += 1

    print(len(word_map.keys()))
    print(sorted(word_map.keys()))
    print(word_map)


if __name__ == '__main__':
    main()
