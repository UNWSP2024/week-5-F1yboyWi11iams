# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    miles = 0.0
    ######################
    # WRITE YOUR CODE HERE
    ######################    


    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion
    
    # Display the miles


def kilometer_conversion():
    kilometers = 0.0
    miles = 0.0
    kilometers = float(input("Please input a distance in kilometers to see the equivalent value in miles: "))
    distance_miles = float(0.6214 * kilometers)
    print(kilometers, " kilometers is equal to ", distance_miles, " miles.")
    return miles
kilometer_conversion()
