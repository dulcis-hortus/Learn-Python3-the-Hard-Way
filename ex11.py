print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("It's right?")
answer = input()
if answer == 'yes':
    print("Good.")
else: print("Hum...That's VERY interesting.")
