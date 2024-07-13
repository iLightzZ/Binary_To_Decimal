print("\nThe following program will read a binary integer and will print its decimal"
" equivalent.\n\n");

#initialization phase
decimal = 0; #This object is used to accumulate the binary values
base = 1; #This object is used for multiplying the binary value depending on its position

#processing phase
binaryNum = int(input("Enter your binary integer(only 0s and 1s): "));
num = binaryNum; #This object is used for the last step (termination phase)

while(binaryNum != 0):
    
    rem = binaryNum % 10; #Object "rem" is used to obtain the last digit of the integer
    decimal = decimal + rem*base;
    binaryNum = int(binaryNum / 10);
    base = base * 2;

#termiantion phase
print("The decimal equivalent of", num, "is:", decimal);
