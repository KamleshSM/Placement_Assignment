
string = input("Enter a string: ")
words = string.split()

    
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
max_frequency = max(word_count.values())


highest_frequency_word = [word for word, count in word_count.items() if count == max_frequency]
highest_frequency_word_length = []
for word1 in highest_frequency_word:
    highest_frequency_word_length.append(len(word1))

maximum_value_of_all =  highest_frequency_word[(highest_frequency_word_length.index(max(highest_frequency_word_length)))]

print(f'Explanation - From the given string we can note that the most frequent words are {highest_frequency_word} and the maximum value of all the values is {maximum_value_of_all} and its corresponding length is {max(highest_frequency_word_length)}')
print(max(highest_frequency_word_length))

"""
1. input : we we we are Rady Rady Rady
    Output: 4
Explanation : 
        From the given string we can note that the most frequent words are ['we', 'Rady'] and the maximum value of all the values is Rady and its corresponding length is 4

2. input : I I I am am am Kamlesh Kamlesh Kamlesh
    Output: 7
Explanation :
    From the given string we can note that the most frequent words are ['I', 'am', 'Kamlesh'] and the maximum value of all the values is Kamlesh and its corresponding length is 7

"""