
# ⭐string method⭐

#   Q no 1 Take a string input and print its length.
str = input("Enter a string:")
print("lendth of string is:", len(str))


# q no 2 Concatenate first name + last name
first_Name = input("Enter your first name:")
last_Name = input("Enter your last name:")
full_Name =first_Name + " " + last_Name
print("Full name is:", full_Name)



#   Q no 3 Print the first and last character of a string.
str = "Muhammad_Ashfaq"
print("First character is:", str[0])
print("Last character is:", str[-1])

# Q no 4 everse a string using slicing.
str = "Ashfaq"
print("Reverse string is:", str[::-1])


# Q no 5 Extract "World" from "HelloWorld"
 str = "HelloWorld"
 print(str[5:10])


# Q no 6 Convert "python" into uppercase
str = "python"
print(str.upper())


# Q no 7 Convert "PYTHON" into lowercase.
str = "PYTHON"
print(str.lower())


#  Q no 8 Remove spaces from " hello ".
str = " hello "
print(str.strip())


# Q no 9 Replace "AI" with "ML" in "AI is the future"
str = "AI is the future"
print(str.replace("AI", "ML"))


# Q no 10 Count how many times "0" 
str = "Hello How are you what are you doing today"
print(str.count("o"))

# Q no 11 Split "I love Python programming" into words
str1 = "I love Python programming"
# Split into words
words = str1.split(" ")
print(words)

# Q no 12 Join ["Python", "is", "fun"] into "Python is fun"
str1 = "Python"
str2 = "is"
str3 = "fun"

sentence = " ".join([str1, str2, str3])
print(sentence)


    




# ⭐Conditionals + Strings⭐

# Q no1 . Take a word and check if it is "Python" (case-insensitive).

word = input("Enter a word: ")
if word.lower() == "python":   # convert both sides to lowercase
    print("Yes, it is Python!")
else:
    print("No, it is not Python.")




# Q no 2 Check if input string is a palindrome

words = input("Enter a word: ")
clean = words.replace(" ", "").lower()
if clean == clean[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")



# Q no 3 cheak if contain vovwel or not
text = input("Enter a string: ").lower()

vowels = "aeiou"

found = False
for ch in text:
    if ch in vowels:
        found = True
        break

if found:
    print("Yes, the string contains vowels.")
else:
    print("No, the string does not contain vowels.")


q no 4 Check if string length is even or odd.
text = input("Enter a string: ")

if len(text) % 2 == 0:
    print("The string length is Even.")
else:
    print("The string length is Odd.")


# Q no 5  Take a password input and check if its length is ≥ 8.
password = input("Enter your password: ")

if len(password) >= 8:
    print("Password length is valid.")
else:
    print("Password too short! Must be at least 8 characters.")



# q no 6 Print "Valid Email" if string contains "@", else "Invalid".
email = input("Enter your email: ")

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")



  





