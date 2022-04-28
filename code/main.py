import modules.imports as dep
import modules.userinputs as usi

print(dep.dt.now())

print("Hey there!\n")
username = input("Please enter your name:")
print("\nWelcome to the game " + username + "!")

#  function module to accept inputs from a user


usi.userinputs()


if __name__ != '__main__':
    pass
else:
    print("\nLottery Program main program")
