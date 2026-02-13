import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
import sys
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
def board_logic():
    print(Fore.LIGHTRED_EX +Style.BRIGHT+ "  1    2    3")
    global board
    global board_map
    board = {"a1":"a1","a2":"a2","a3":"a3","b1":"b1","b2":"b2","b3":"b3","c1":"c1","c2":"c2","c3":"c3"}
    board_map= f"a {a1}  | {a2}  | {a3} \n\nb {b1}  | {b2}  | {b3} \n\nc {c1}  | {c2}  | {c3} \n"
    return board_map

print(board_logic())

userinput_x= input("Enter where to change:")

if userinput_x in l:
    board[str(userinput_x)]="x "
    board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
    print(board_map)
else:
    print(Fore.LIGHTRED_EX+"\nInvalid Dimensions!")
    sys.exit(0)

userinput_o= input("Enter where to change:")

if userinput_o != userinput_x:
    if userinput_o in l:
        board[str(userinput_o)] = "o "
        board_map= f" {board["a1"]}  | {board["a2"]} | {board["a3"]} \n\n {board["b1"]}  | {board["b2"]} | {board["b3"]} \n\n {board["c1"]}  | {board["c2"]} | {board["c3"]} "
        print(board_map)
    else:
        print("Invalid Dimensions!\n")
else:
    print("\nPosition alderdy used!")