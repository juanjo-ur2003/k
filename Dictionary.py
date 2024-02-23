with open("book.txt") as file:
    text = file.read()
file.close()
# crate a dictionary of word frequencies
word_freq = {}
punctuation = ",.'?;\n-()"

file = open("book.txt")
for line in file:
    # remove punctuation
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split(" ")
    for word in words:
        word = word.lower()
        # check and add into the dictionary
        if word in word_freq:
            # word in the dictionary, increase frequency by 1
            word_freq[word] += 1
        else:
            # not there, so we add it with initial value of 1
            word_freq[word] = 1

# find the 10 biggest frequencies
frequencies = list(word_freq.values())
frequencies.sort(reverse=True)
top_frequencies = frequencies[:10]
print(top_frequencies)

# match the words
for top_word in top_frequencies:
    for key in word_freq:
        if word_freq[key] == top_word:
            print(f"Word '{key}' appers {top_word} times")
            break
