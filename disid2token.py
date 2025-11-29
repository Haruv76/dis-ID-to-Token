import os
import base64
import time
import random
import string

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init

init()

banner = (Fore.MAGENTA + """by haruv""" + Fore.LIGHTCYAN_EX)
print(banner)

userid = input(" [INPUT] USER ID : ")

if not (userid.isdigit() and len(userid) == 18):
    print(Fore.RED + "\n [ERROR] INVALID USER ID (must be 18 digits)" + Fore.RESET)
    os.system('pause >nul')
    exit()

wait_time = random.randint(10, 20)
print(Fore.YELLOW + f"\n [LOGS] VALID USER ID — PROCESSING ({wait_time}s)..." + Fore.RESET)
time.sleep(wait_time)

def rand(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))

part1 = rand(12)
part2 = rand(6)
part3 = rand(27)

result = f"{part1}.{part2}.{part3}"

print(Fore.CYAN + f"\n [LOGS] OUTPUT : {result}" + Fore.RESET)

os.system('pause >nul')
