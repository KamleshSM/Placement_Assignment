
string = input("Enter a string: ")
words = string.split()

    
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
max_frequency = max(word_count.values())
highest_frequency_word = [word for word, count in word_count.items() if count == max_frequency]
highest_frequency_word_length = len(highest_frequency_word[0])

print("Length of the highest-frequency word:", highest_frequency_word_length)
