# The number of types of people
types_of_people = 10
# sentence
x = f"There are {types_of_people} types of people."

# variable of strings
binary = "binary"
do_not = "don't"
# sentence
y = f"Those who know {binary} and those who {do_not}."

# print two sentence
print(x)
print(y)

# print string with variable
print(f"I said: {x}")
print(f"I also said: '{y}'")

# What is a 'hilarious'?
# Oh... Its mean 'extremely funny'
# .format is very useful tool
# .format is function?
hilarious = False
joke_evaluation = "Isn't that {} joke so funny?! {}"

# .format () example
print(joke_evaluation.format(hilarious, hilarious))

# Two variable of two sentence
w = "This is the left side of..."
e = "a string with a right side."

# combination
print(w + e)
