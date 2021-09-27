n = True
while n:
    final_number = None
    while final_number == None:
            
        # elif (function == "c"):
        #     final_number = final_number

        # elif (second_number == "c"):
        #     final_number = final_number

        
        first_number = input("Enter your fist number: ")
        if (first_number == "c"):
            final_number = 0
            first_number = 0
            function = "+"
            second_number = 0
        else :
            function = input("What acction do you want to execute? (+ , - , * , / ): ")
            if function == "c":
                final_number = 0
                first_number = 0
                function = "+"
                second_number = 0
            else:
                second_number = input("Enter your second number: ")
                if second_number == "c":
                    final_number = 0
                    first_number = 0
                    function = "+"
                    second_number = 0
            


        if function == "+":
            final_number = int(first_number) + int(second_number)
            print(final_number)
        elif function == "-":
            final_number = int(first_number) - int(second_number)
            print(final_number)
        elif function == "*":
            final_number = int(first_number) * int(second_number)
            print(final_number)
        elif function == "/":
            final_number = int(first_number) / int(second_number)
            print(final_number)