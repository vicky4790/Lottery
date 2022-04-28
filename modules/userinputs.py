def userinputs():
    try:
        array = []
        i = 1
        print("Enter only 3 numbers from 1 to 50")
        while i <= 3:
            try:
                uservalue = input("Enter " + str(i) + " number:")
                int_uservalue = int(uservalue)
                array.append(int_uservalue)
                if i == 3:
                    break
                i += 1
            except:
                print("Alphanumerics are not allowed")
        array.sort()
        print("You have selected the below numbers\n")
        print(array)
    except:
        print("Something went wrong")