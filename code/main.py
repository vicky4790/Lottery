import modules.imports as dep

print(dep.dt.now())

#  function module to accept inputs from a user


def userinputs():
    # print("Hey there!\n")
    # username = input("Please enter your name:")
    # print("\nWelcome to the game " + username + "!")
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


userinputs()


if __name__ != '__main__':
    pass
else:
    print("\nLottery Program main program")
