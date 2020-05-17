# Program to find the ASCII value of the given character

'''
ASCII stands for American Standard Code for Information Interchange.
ASCII value of number (0-9) is 48-57
ASCII value of A-Z is 65-90
ASCII value of a-z is 97-122

Here we have used ord() function to convert a character to an integer
(ASCII value). This function returns the Unicode code point of that character.'''

ch=input("Enter character :")

print("The ASCII value of '" + ch + "' is", ord(ch))


'''
output:
Enter character :T
The ASCII value of 'T' is 84
or
Enter character :a
The ASCII value of 'a' is 97
or
Enter character :2
The ASCII value of '2' is 50
or
Enter character :%
The ASCII value of '%' is 37
'''
