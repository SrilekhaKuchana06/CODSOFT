print("***** CALCULATOR *****")
while True:
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    print("Enter \n 1. For Addition \n 2. For Subtraction \n 3. For Multiplication \n 4. For Division")
    operation = input()
    if operation == '1':
        print("Sum of",num1,"and",num2,"is",num1+num2)
    elif operation == '2':
        print("Difference of",num1,"and",num2,"is",num1-num2)
    elif operation == '3':
        print("Product of",num1,"and",num2,"is",num1*num2)
    else:
        if num2 == 0:
            print("Cannot perform Division with zero")
        else:
            print("Division of",num1,"and",num2,"is",num1/num2)
    print("Once again?(yes/no)")
    inp = input()
    if inp == 'yes':
        continue
    else:
        print("***** GOODBYE *****")
        break

        