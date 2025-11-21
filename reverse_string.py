def reverse_a_string(original_string):
    string_length = len(original_string)
    reversed_result = ''

    for i in range(-1, -string_length - 1, -1):
        reversed_result = reversed_result + original_string[i]
    return reversed_result


user_word = input("Type a word to reverse: ")
print(reverse_a_string(user_word))