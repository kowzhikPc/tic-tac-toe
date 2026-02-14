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
print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"Hello Gamers!\n")
def exit_logic():   
    print("\n-->Game Restart!") 
    time.sleep(2)
    sys.exit(0)

def board_logic():
    print(Fore.LIGHTRED_EX +Style.BRIGHT+ "  1    2    3")
    global board
    global board_map
    board = {"a1":"a1","a2":"a2","a3":"a3","b1":"b1","b2":"b2","b3":"b3","c1":"c1","c2":"c2","c3":"c3"}
    board_map= f"a {a1}  | {a2}  | {a3} \n\nb {b1}  | {b2}  | {b3} \n\nc {c1}  | {c2}  | {c3} \n"
    return board_map

print(board_logic())
all_inputs = []

userinput_x= input("Enter where to change:")
all_inputs.append(userinput_x)

if userinput_x in l:
    board[str(userinput_x)]="x "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print(Fore.LIGHTRED_EX+"\nInvalid Dimensions!")
    exit_logic()

userinput_o= input("Enter where to change:")
all_inputs.append(userinput_o)

if userinput_o != userinput_x:
    if userinput_o in l:
        board[str(userinput_o)] = "o "
        board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
        print(board_map)
    else:
        print("Invalid Dimensions!\n")
        exit_logic()
else:
    print("\nPosition alderdy used!")
    exit_logic()

userinput_x_2= input("Enter where to change:")
all_inputs.append(userinput_x_2)

if userinput_x_2 != userinput_x and userinput_o:
    board[str(userinput_x_2)] = "x "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)

else:
    print("Invalid Dimensions")
    exit_logic()

userinput_o_2 =input("Enter where to change:")


if userinput_o_2 not in all_inputs:
    all_inputs.append(userinput_o_2)
    board[str(userinput_o_2)] = "o "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print("invalid dimensions")
    exit_logic()
userinput_x_3 = input("Enter where to change:")

if userinput_x_3 not in all_inputs:
    all_inputs.append(userinput_x_3)
    board[str(userinput_x_3)] = "x "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print("invalid Dimensions")
    exit_logic()
userinput_o_3 = input("Enter where to change:")

if userinput_o_3 not in all_inputs:
    all_inputs.append(userinput_o_3)
    board[str(userinput_o_3)] = "o "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print("invalid dimensions")
    exit_logic()

userinput_x_4 =input("Enter where to change:")

if userinput_x_4 not in all_inputs:
    all_inputs.append(userinput_x_4)
    board[str(userinput_x_4)] = "x "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print("invalid dimensions")
    exit_logic()

userinput_o_4 =input("Enter where to change:")

if userinput_o_4 not in all_inputs:
    all_inputs.append(userinput_o_4)
    board[str(userinput_o_4)] = "o "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print("invalid dimensions")
    exit_logic()

userinput_x_5 =input("Enter where to change:")

if userinput_x_5 not in all_inputs:
    all_inputs.append(userinput_x_5)
    board[str(userinput_x_5)] = "x "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print("invalid dimensions")
    exit_logic()

