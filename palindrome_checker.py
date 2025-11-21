def is_palindrome():
    original_string = input("Enter a word, I'll tell you if it's a palindrome or not: ").lower().replace(" ", "")

    string_length = len(original_string)
    reversed_result = ''

    for i in range(-1, -string_length - 1, -1):
        reversed_result = reversed_result + original_string[i]

    if reversed_result == original_string:
        print("This is a PALINDROME!!!")
    else:
        print("Sadly, not a palindrome.")

is_palindrome()