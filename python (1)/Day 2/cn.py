#  ⭐ string 

#       string is data types that stores a sequance of character

#  ⭐ Basics operations 

#  ❤    - coneectantion 
connect = "hello" + "world"
print(connect)


#  ❤    - replication
repl = "hello" * 3
print(repl)

#  ❤    - indexing
index = "hello"
print(index[0])
print(index[-1])
print(index[1:4])
print(index[:3])
print(index[2:])
print(index[:])

# # ❤     - membership
print("h" in index)
print("a" not in index)
print("e" in index)


# ❤     -slicing
slice = "hello world"
print(slice[0:5])
print(slice[6:11])
print(slice[:5])





# ⭐ string methods

str = "i am a coder"

 # - upper()
print(str.upper())

# lower()
print(str.lower())

# capitalize()
print(str.capitalize())

# replace()
print(str.replace("coder", "developer"))
 

# split()
print(str.split())

# join()
print("-".join(str))

# find()
print(str.find("coder"))

# index()
print(str.index("coder"))

# count()
print(str.count("a"))



#  ⭐ condationl statment 


# if 
# elif 
# else

  age = int(input("enter your age: "))
if age < 18:
     print("you are a minor")
else:
     print("you are a major")

