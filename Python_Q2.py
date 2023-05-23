"""
Question 2: -
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if 
he can remove just one character at the index in the string, and the remaining characters will occur the same 
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide 
an explanation for the same.
Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
Example output 1- YES
Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves 
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - YES
Example input 3 - s “abccc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves 
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - NO
"""



def is_valid_string(string):
    # Count the frequency of each character
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    print(char_count)
    # Find the frequencies of the characters
    frequencies = list(char_count.values())

    # Check if all frequencies are the same
    if len(set(frequencies)) == 1:
        return "YES"

    # Check if removing one character makes all frequencies the same
    for index in range(len(string)):
        # Remove one character at index and count frequencies
        remaining_string = string[:index] + string[index+1:]
        remaining_char_count = {}
        for char in remaining_string:
            remaining_char_count[char] = remaining_char_count.get(char, 0) + 1
        remaining_frequencies = list(remaining_char_count.values())

        # Check if all remaining frequencies are the same
        if len(set(remaining_frequencies)) == 1:
            return "YES"

    return "NO"


# Example usage
input_string = input("Enter a string: ")
result = is_valid_string(input_string)
print(result)

"""
input1: abcdefghhgfedecba
output:YES 
Explanation: {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 3, 'f': 2, 'g': 2, 'h': 2}
All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.


input2 : aabbccddeefghi
Output: NO
Explanation: Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove 4 characters with a frequency of 1: {fghi}.
Remove 5 characters of frequency 2: {abcde}.
Neither of these is an option.
"""