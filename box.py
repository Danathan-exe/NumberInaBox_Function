def number_in_a_box(number):
  #defining how many digets are in the number
  length = len(str(number))
  #initiating the variable
  string = "####"
  #for how many characters in length it goes through it.
  for i in range(length): 
#adding # per character
    string = string + "#"
#prints and outputs the variables
  print(string)
  print("# " + str(number) + " # ")
  print(string)
number_in_a_box(8008)


# Trichler's Test
number_in_a_box(7)
print("")
number_in_a_box(8008)

