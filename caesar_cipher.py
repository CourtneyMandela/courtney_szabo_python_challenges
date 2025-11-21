#Define a function called caesar_cipher that accepts:
#a string text
#an integer shift
def caesar_cipher(text, shift):
    char_list = []

    for char in text:
        # If uppercase A–Z
        if 'A' <= char <= 'Z':
            base = ord('A')
            original = ord(char) - base       # 0–25
            wrapped = (original + shift) % 26
            new_value = base + wrapped
            char_list.append(new_value)

        # If lowercase a–z
        elif 'a' <= char <= 'z':
            base = ord('a')
            original = ord(char) - base       # 0–25
            wrapped = (original + shift) % 26
            new_value = base + wrapped
            char_list.append(new_value)

        # Non-letters stay the same
        else:
            char_list.append(ord(char))

    # Now build the final shifted string
    shifted_text = ''
    for value in char_list:
        shifted_text += chr(value)

    return shifted_text


    #Use ord() to get the Unicode value of a character.
    
    # add shift to each unicode value
    
    #Use chr() to convert back to a character.

    #Wrap around the alphabet using % 26 when needed.

    #Return a new string with each alphabetical character shifted by the shift amount.


print(caesar_cipher("abc", 3)) #Output:  "def"  
print(caesar_cipher("xyz", 2)) #Output:  "zab"  
print(caesar_cipher("Hello, World!", 5)) #Output:  "Mjqqt, Btwqi!"