# It's string which has four blanks. 
formatter = "{} {} {} {}"

# formatter(string) formated by four numbers
print(formatter.format(1, 2, 3, 4))
# formatter(string) formated by four strings
print(formatter.format("one", "two", "three", "four"))
# formatter(string) formated by four bools
print(formatter.format(True, False, False, True))
# formatter(string) formated by four variables
print(formatter.format(formatter, formatter, formatter, formatter))
# formatter(string) formated by four strings
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))
