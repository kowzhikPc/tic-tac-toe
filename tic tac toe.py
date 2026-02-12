import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

a1 =0
a2 =0
a3=0
b1=0
b2=0
b3=0
c1=0
c2=0
c3=0
l = ["a1","a2","a3","b1","b2","b3","c1","c2"]
def board_logic():
    print("  1    2    3")
    global board_map
    board_map= f"a {a1}  | {a2}  | {a3} \n\nb {b1}  | {b2}  | {b3} \n\nc {c1}  | {c2}  | {c3} "
    return board_map

print(board_logic())

userinput= input("Enter where to change:")


if userinput == "a1":
    a1 ="x"
    print(board_logic())


