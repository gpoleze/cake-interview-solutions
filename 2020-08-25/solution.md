### Solution
In our solution, we make three decisions:

1. **We use a class**. This allows us to tie our methods together, calling them on instances of our class instead of passing references.
2. To handle duplicate words with different cases, **we choose to make a word uppercase in our dictionary only if it is always uppercase in the original string**. While this is a reasonable approach, it is imperfect (consider proper nouns that are also lowercase words, like "Bill" and "bill").
3. **We build our own `split_words()` method** instead of using a built-in one. This allows us to pass each word to our add_word_to_dictionary() method as it was split, and to split words and eliminate punctuation in one iteration.

To split the words in the input string and populate a dictionary of the unique words to the number of times they occurred, we:

1. **Split words** by spaces, em dashes, and ellipses—making sure to include hyphens surrounded by characters. We also include all apostrophes (which will handle contractions nicely but will break possessives into separate words).
2. **Populate the words in our dictionary** as they are identified, checking if the word is already in our dictionary in its current case or another case.
If the input word is uppercase and there's a lowercase version in the dictionary, we increment the lowercase version's count. If the input word is lowercase and there's an uppercase version in the dictionary, we "demote" the uppercase version by adding the lowercase version and giving it the uppercase version's count.