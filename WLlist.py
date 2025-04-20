import itertools

# Colors
GREEN = "\033[1;92m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;96m"
RED = "\033[1;91m"
BLUE = "\033[1;94m"
YELLOW = "\033[1;93m"
RESET = "\033[0m"

# Banner
def banner():
    print(GREEN + r"""
 __      __.____    .__  .__          __
/  \    /  \    |   |  | |__| _______/  |_
\   \/\/   /    |   |  | |  |/  ___/\   __\
 \        /|    |___|  |_|  |\___ \  |  |
  \__/\  / |_______ \____/__/____  > |__|
       \/          \/            \/       v1.0.0
""" + RESET + MAGENTA + """
           Wordlist Generator Tool
          Created by I AM NOT HACKER
""" + RESET)

banner()

# Menu
print(YELLOW + "============================================" + RESET)
print(BLUE + "                    Menu" + RESET)
print(YELLOW + "============================================" + RESET)
print(CYAN + "[1]  Numbers Only (0000-9999)")
print("[2]  Lowercase Only (abcd-xyz)")
print("[3]  Uppercase Only (ABCD-XYZ)")
print("[4]  Numbers + Uppercase (1234ABCD)")
print("[5]  Numbers + Lowercase (1234abcd)")
print("[6]  Uppercase + Numbers (ABCD1234)")
print("[7]  Lowercase + Numbers (abcd1234)")
print("[8]  Uppercase + Lowercase (ABCDabcd)")
print("[9]  Lowercase + Uppercase (abcdABCD)")
print("[10] Numbers + Symbols (1234!@#$)")
print("[11] Uppercase + Symbols (ABCD!@#$)")
print("[12] Lowercase + Symbols (abcd!@#$)")
print("[13] Lowercase + Symbols + Numbers")
print("[14] Uppercase + Symbols + Numbers")
print("[15] Uppercase + Space + Numbers")
print("[16] Lowercase + Space + Numbers")
print("[17] Base Word + Ending Numbers")
print("[18] Lowercase + Uppercase + Symbols + Numbers")
print("[19] Uppercase + Lowercase + Symbols + Numbers")
print("[20] Uppercase + Lowercase + Numbers")
print("[21] Lowercase + Uppercase + Numbers" + RESET)
print(YELLOW + "============================================\n" + RESET)
choice = input(GREEN + "Select Option ⟩ " + RESET).strip()

def ask_range(name):
    print(YELLOW + f"\nEnter {name} Min Length:" + RESET)
    min_len = int(input(GREEN + "➤ " + RESET))
    print(YELLOW + f"Enter {name} Max Length:" + RESET)
    max_len = int(input(GREEN + "➤ " + RESET))
    return min_len, max_len

def generate_combinations(charset, min_len, max_len, filename):
    with open(filename, 'w') as f:
        for i in range(min_len, max_len + 1):
            for combo in itertools.product(charset, repeat=i):
                f.write(''.join(combo) + '\n')
    print(GREEN + f"\n[+] Wordlist saved as: {filename}" + RESET)

# Basic sets
basic_sets = {
    '1': '0123456789',
    '2': 'abcdefghijklmnopqrstuvwxyz',
    '3': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
}

if choice in basic_sets:
    name = ["Number", "Lowercase", "Uppercase"][int(choice)-1]
    min_len, max_len = ask_range(name)
    filename = input(YELLOW + "Enter save file name: " + RESET) + ".txt"
    print(CYAN + "\n[+] Generating combinations...\n" + RESET)
    generate_combinations(basic_sets[choice], min_len, max_len, filename)
    exit()

# Duo sets
duo_options = {
    '4': ('0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "Numbers", "Uppercase"),
    '5': ('0123456789', 'abcdefghijklmnopqrstuvwxyz', "Numbers", "Lowercase"),
    '6': ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', "Uppercase", "Numbers"),
    '7': ('abcdefghijklmnopqrstuvwxyz', '0123456789', "Lowercase", "Numbers"),
    '8': ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', "Uppercase", "Lowercase"),
    '9': ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "Lowercase", "Uppercase"),
    '10': ('0123456789', '!@#$%^&*', "Numbers", "Symbols"),
    '11': ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*', "Uppercase", "Symbols"),
    '12': ('abcdefghijklmnopqrstuvwxyz', '!@#$%^&*', "Lowercase", "Symbols"),
}

if choice in duo_options:
    charset1, charset2, name1, name2 = duo_options[choice]
    min1, max1 = ask_range(name1)
    min2, max2 = ask_range(name2)
    filename = input(YELLOW + "Enter save file name: " + RESET) + ".txt"
    print(CYAN + "\n[+] Generating combinations...\n" + RESET)
    with open(filename, 'w') as f:
        for l1 in range(min1, max1 + 1):
            for l2 in range(min2, max2 + 1):
                for p1 in itertools.product(charset1, repeat=l1):
                    for p2 in itertools.product(charset2, repeat=l2):
                        f.write(''.join(p1) + ''.join(p2) + '\n')
    print(GREEN + f"\n[+] Wordlist saved as: {filename}" + RESET)
    exit()

# Triple/Quad charset logic
trio_quadro = {
    '13': ['abcdefghijklmnopqrstuvwxyz', '!@#$%^&*', '0123456789'],
    '14': ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*', '0123456789'],
    '18': ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*', '0123456789'],
    '19': ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '!@#$%^&*', '0123456789'],
    '20': ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789'],
    '21': ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789']
}

set_names = {
    '13': ("Lowercase", "Symbols", "Numbers"),
    '14': ("Uppercase", "Symbols", "Numbers"),
    '18': ("Lowercase", "Uppercase", "Symbols", "Numbers"),
    '19': ("Uppercase", "Lowercase", "Symbols", "Numbers"),
    '20': ("Uppercase", "Lowercase", "Numbers"),
    '21': ("Lowercase", "Uppercase", "Numbers")
}

if choice in trio_quadro:
    print()
    selected = trio_quadro[choice]
    set_labels = set_names[choice]
    lengths = []
    for i in range(len(selected)):
        lmin, lmax = ask_range(set_labels[i])
        lengths.append((selected[i], lmin, lmax))

    filename = input(YELLOW + "Enter save file name: " + RESET) + ".txt"
    print(CYAN + "\n[+] Generating combinations...\n" + RESET)

    with open(filename, 'w') as f:
        def nested_generate(depth=0, prefix=''):
            if depth == len(lengths):
                f.write(prefix + '\n')
                return
            charset, lmin, lmax = lengths[depth]
            for l in range(lmin, lmax + 1):
                for part in itertools.product(charset, repeat=l):
                    nested_generate(depth + 1, prefix + ''.join(part))
        nested_generate()

    print(GREEN + f"\n[+] Wordlist saved as: {filename}" + RESET)
    exit()

# Special Options
if choice == '15' or choice == '16':
    upper = choice == '15'
    case = "Uppercase" if upper else "Lowercase"
    c_min, c_max = ask_range(case)
    n_min, n_max = ask_range("Number")
    filename = input(YELLOW + "Enter save file name: " + RESET) + ".txt"
    print(CYAN + "\n[+] Generating combinations...\n" + RESET)
    with open(filename, 'w') as f:
        for c_len in range(c_min, c_max + 1):
            for n_len in range(n_min, n_max + 1):
                for c in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ' if upper else 'abcdefghijklmnopqrstuvwxyz', repeat=c_len):
                    for n in itertools.product('0123456789', repeat=n_len):
                        f.write(''.join(c) + ' ' + ''.join(n) + '\n')
    print(GREEN + f"\n[+] Wordlist saved as: {filename}" + RESET)
    exit()

elif choice == '17':
    base_word = input(YELLOW + "\nEnter base word (e.g., Hacker): " + RESET)
    n_min, n_max = ask_range("Number")
    filename = input(YELLOW + "Enter save file name: " + RESET) + ".txt"
    print(CYAN + "\n[+] Generating combinations...\n" + RESET)
    with open(filename, 'w') as f:
        for length in range(n_min, n_max + 1):
            for i in range(10 ** length):
                number = str(i).zfill(length)
                f.write(f"{base_word}{number}\n")
    print(GREEN + f"\n[+] Wordlist saved as: {filename}" + RESET)
    exit()

else:
    print(RED + "\n[!] Invalid choice." + RESET)
