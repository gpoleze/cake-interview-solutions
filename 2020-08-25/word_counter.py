def main():
    input = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
    # input = 'The bill came to five dollars.'

    word_map = dict()

    punctiotionSet = ('.', ',', ':', '"', '!', '?', ' ', '(', ')')

    start = 0
    length = 0
    for i, c in enumerate(input):
        c = c.lower()
        if c in punctiotionSet:
            if not length:
                start = i + 1
                continue
            word = input[start: start + length]
            if word in word_map.keys():
                word_map[word] += 1
            else:
                word_map[word] = 1
            start = i + 1
            length = 0
        else:
            length += 1

    print(sorted(word_map.keys()))
    print(word_map)


if __name__ == '__main__':
    main()
