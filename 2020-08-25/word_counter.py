def main():
    input = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
    # input = 'The bill came to five dollars.'

    word_map = dict()

    punctiotionSet = ('.', ',', ':', '"', '!', '?', ' ', '(', ')')

    word = ""
    for c in input:
        c = c.lower()
        if c in punctiotionSet:
            if not word:
                continue
            if word in word_map.keys():
                word_map[word] += 1
            else:
                word_map[word] = 1
            word = ""
        else:
            word += c

    print(sorted(word_map.keys()))
    print(word_map)


if __name__ == '__main__':
    main()
