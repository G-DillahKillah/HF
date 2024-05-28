import os
import subprocess

def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')

def landlubber():
    clear_screen()
    os.system("git clone https://github.com/drooling/phosint")
    os.chdir("phosint")
    os.system("pip install -r requirements.txt")
    os.system("git pull")
    os.system("git fetch")
    clear_screen()
    print("Please Input Number \033[92m EXAMPLE 1112223333")
    choice = input("Enter Number: ")

    try:
        subprocess.run(["python3", "phosint.py", choice])
    except Exception as e:
        print(f"Error: {e}")
    print('\033[92m1\033[0m) \033[92mSearch again\033[0m')
    print('\033[91m2\033[0m) \033[91mExit\033[0m')
    choice = input("Make selection: ")
    
    if choice == "1":
        landlubber()
    elif choice == "2":
        exit
    else:
        print('Too Bad')
    
if __name__ == "__main__":
    landlubber()
