import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
import sys
import time

a1 =0
a2 =0
a3=0
b1=0
b2=0
b3=0
c1=0
c2=0
c3=0
l = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
print("\n"+Fore.LIGHTBLUE_EX+Style.BRIGHT+"Hello Gamers!\n")
def exit_logic():   
    i = 3
    print(Fore.LIGHTRED_EX+ Style.BRIGHT +"\nBad Dimensions!","\n")
    while i > 0:
        print(Fore.WHITE + Style.BRIGHT +f"Game Ends In: ",end="")
        print(Fore.RED + Style.BRIGHT+str(i))
        i -=1
        time.sleep(0.97)
    sys.exit(0)

def board_logic():
    print(Fore.LIGHTRED_EX +Style.BRIGHT+ "  1    2    3")
    global board
    global board_map
    board = {"a1":"a1","a2":"a2","a3":"a3","b1":"b1","b2":"b2","b3":"b3","c1":"c1","c2":"c2","c3":"c3"}
    board_map= f"a {a1}  | {a2}  | {a3} \n\nb {b1}  | {b2}  | {b3} \n\nc {c1}  | {c2}  | {c3} \n"
    return board_map

print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_logic())
all_inputs = []

def win_logic():
    if board["a1"] == "X " and board["a2"] == "X " and board["a3"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["b1"] == "X " and board["b2"] == "X " and board["b3"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["c1"] == "X " and board["c2"] == "X " and board["c3"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a1"] == "X " and board["b1"] == "X " and board["c1"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a2"] == "X " and board["b2"] == "X " and board["c2"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a3"] == "X " and board["b3"] == "X " and board["c3"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a1"] == "X " and board["b2"] == "X " and board["c3"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a3"] == "X " and board["b2"] == "X " and board["c1"] == "X ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a1"] == "O " and board["a2"] == "O " and board["a3"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["b1"] == "O " and board["b2"] == "O " and board["b3"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["c1"] == "O " and board["c2"] == "O " and board["c3"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a1"] == "O " and board["b1"] == "O " and board["c1"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a2"] == "O " and board["b2"] == "O " and board["c2"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a3"] == "O " and board["b3"] == "O " and board["c3"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a1"] == "O " and board["b2"] == "O " and board["c3"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)
    elif board["a3"] == "O " and board["b2"] == "O " and board["c1"] == "O ":
        print(Fore.GREEN + "Won")
        i = 3
        while i > 0:
            print(Fore.GREEN + f"Game ends in {i}")
            i -=1
            time.sleep(0.97)
        sys.exit(0)


userinput_x= input(Fore.MAGENTA + "Enter where to change:" + Style.RESET_ALL)
all_inputs.append(userinput_x)

if userinput_x in l:
    board[str(userinput_x)]="X "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()

userinput_o= input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)
all_inputs.append(userinput_o)

if userinput_o != userinput_x:
    if userinput_o in l:
        board[str(userinput_o)] = "O "
        board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
        win_logic()
    else:
        exit_logic()
else:
    exit_logic()

userinput_x_2= input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)
all_inputs.append(userinput_x_2)

if userinput_x_2 != userinput_x and userinput_o:
    board[str(userinput_x_2)] = "X "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()

else:
    exit_logic()

userinput_o_2 =input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)


if userinput_o_2 not in all_inputs:
    all_inputs.append(userinput_o_2)
    board[str(userinput_o_2)] = "O "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()
userinput_x_3 = input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)

if userinput_x_3 not in all_inputs:
    all_inputs.append(userinput_x_3)
    board[str(userinput_x_3)] = "X "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()
userinput_o_3 = input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)

if userinput_o_3 not in all_inputs:
    all_inputs.append(userinput_o_3)
    board[str(userinput_o_3)] = "O "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()

userinput_x_4 =input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)

if userinput_x_4 not in all_inputs:
    all_inputs.append(userinput_x_4)
    board[str(userinput_x_4)] = "X "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()

userinput_o_4 =input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)

if userinput_o_4 not in all_inputs:
    all_inputs.append(userinput_o_4)
    board[str(userinput_o_4)] = "O "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()

userinput_x_5 =input(Fore.MAGENTA +"Enter where to change:"+ Style.RESET_ALL)

if userinput_x_5 not in all_inputs:
    all_inputs.append(userinput_x_5)
    board[str(userinput_x_5)] = "X "
    board_map= f"\n {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT+board_map,"\n")
    win_logic()
else:
    exit_logic()

