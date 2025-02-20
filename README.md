#Completed in Fall of 2022 in Discrete Mathematics class as Programming Project #1 (out of 3)

#My code performs binary addition on two binary string inputs (x and y)
#String inputs are in two's complement format

#result stores the final sum
#carry determines the value needed to be carried for the operation

#The loop iterates through x and y from the rightmost bit to the leftmost bit

#Each bit is converted from a char to an int

#The sum is calculated, carryNum is updated for binary carry and the remainder is taken to determine the current bit of the result.

#If the sign bits of both the inputs are equal but the sign bit of the result is not equal to the sign bit of the x input then an "Error Overflow" is detected

#If no "Error Overflow" is detected then the computed binary sum is returned as a string

#Test cases are commented out at the bottom of the program.
