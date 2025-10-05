# FILE NAME - convert_C_to_F_02.py

# NAME: John Jones
# DATE: 10/3/25
# BRIEF DESCRIPTION: program that converts temperatures between Celsius and Fahrenheit based on user choice. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def convert_temperature():
    print("===== Temperature Converter =====\n")
    print("  1. Convert from Celsius to Fahrenheit")
    print("  2. Convert from Fahrenheit to Celsius\n")
    choice = input("Please choose from the above menu: ")
    if choice == "1":
        temp = float(input("Enter a temperature to convert: "))
        converted = temp * 9 / 5 + 32
        print(f"\n{temp:.1f} degrees Celsius is {converted:.1f} degrees Fahrenheit.\n")
    elif choice == "2":
        temp = float(input("Enter a temperature to convert: "))
        converted = (temp - 32) * 5 / 9
        print(f"\n{temp:.1f} degrees Fahrenheit is {converted:.1f} degrees Celsius.\n")
    else:
        print("\nInvalid selection. Please choose 1 or 2.\n")
if __name__ == "__main__":
    convert_temperature()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
not to rush through labs. This lab took me multiple days to get done as I didnt understant some of the concepts and had to break to study more.






'''
