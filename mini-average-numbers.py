#Make a 'dynamic list' (dynamic meaning it can be any size, we don't know how #many numbers that the user will give us). 
#List is a data structure. We assign the size inside of the brackets []
#If we put a number inside of the brackets, that's how long it is. We don't
#know in advance how long our list needs to be so we can put nothing inside
#of the brackets to "dynamically" allocate space to the list. It will
#be as big as we need it to be. Dynamic data structures like List are very
#important.
listOfNumbers = []

#This is a "do while" loop, the program's entry point for the loop
#will only begin with the option to input a value, and 
#we only exit the loop after we have received at least one
#value. In this case, hitting the ENTER key will create a 
#string value of "", which for our program is not useful,
#so it can be used as the exit point.
while True:
  inputLineValue = input('Please enter an integer (ENTER by itself to quit): ')
  #now we have a value, it's either an integer or a an empty string, so first
  #we check if the user hit enter without ever typing a number in during 
  #the while loop, in which case, our listOfNumbers length is 0. Otherwise,
  #they hit enter after they already entered numbers into the program.
  if inputLineValue == "":
      #check if listOfNumbers is empty (length is 0) using "if not" (this is unique to python)
      if not listOfNumbers:
          print("You did not enter any numbers.")
      break
  #else if, in python it's called "elif"         
  elif inputLineValue == "":
        break;

  #here we call the append function to add our values to the dynamic list,
  #but we need to parse our values as ints, because they are still
  #string data, but they represent numbers. So we "typecast" each string 
  #data that we receive at each individual iteration of this loop      
  listOfNumbers.append(int(inputLineValue))
    
#if listOfNumbers is NOT empty, program control flow goes inside of the if #statement, if listOfNumbers IS empty control does got go inside of the if
#statement, and the program terminates.
if listOfNumbers:
  #store the length of the list of numbers that we captured from user input
  #by assigning the result returned by calling the len() function, with our #list 
  #as a parameter, to a variable named "length"
  length = len(listOfNumbers)
  total = sum(listOfNumbers)
  #store the average by assigning the result returned by calling the round
  #function on the summation divided by the length, with 2 significant figures
  #(decimal precision points), to a variable named "average"
  average = round(total/length,2)
  #output the average, adding commas in a print statement
  #gives us spaces between our text that we have printed out
  print ("The average of the",
  length,
  "numbers you entered is", 
  average,
  ".")
