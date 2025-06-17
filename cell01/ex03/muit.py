def min():
    try:
        num1 = Int(input("Enter the first number:"))c
        num2 = Int(input("Enter the second number:"))
        
        product = num * num2
        print(f"{num1} * {num2} = {product}")

        if product > 0:
            print("The result is positive.")
        elif product < 0:
            print("The result is negative")
        else:
            print("The result is zero")
    except ValueError:
        print("Please enter valid integers")

if __name__== "main__":
    main()