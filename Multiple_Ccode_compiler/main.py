from distutils.ccompiler import new_compiler
from subprocess import call
import glob
import os


def keep_running():
    while True:
        print("\t\t  ------Multiple C code compiler------")
        print("1. Compile all c files in current directory.\t 2. Compile files one at a time.")
        print("3. List all c files.                        \t 4. show installed compilers.")
        print(f"5. Display current working directory.      \t 6. change directory (current: {os.getcwd().split('/')[-1]})")
        print("7. Delete files.                            \t 8. Quit program.")
        try:
            choice = input("Enter your desired choice: ")
        except KeyboardInterrupt:
            print("-------------------------")
            if input("You really want to quit(y/n): ") == 'y':
                exit(0)
            else:
                continue
        if choice == '1':                                                  # In order to understand this code read from if choice == '2'
            try:
                compiler2 = new_compiler()
                print("WARNING:")
                print("Don't use this option if you wanna compile different files with different libraries.")
                print("since it compiles all files the linking library must be same.")
                print("Please don't include -l type what's after -l since -l will be already included.")
                print("For example to link math library you pass -lm.")
                print("gcc mathfile.c -o mathfile -lm")
                print("So to include math library you should only type 'm'")
                link_lib = input("Link library?(y/n) (OPTIONAL): ")
                if link_lib == 'y':
                    libname = input("Linker option: ")
                    print("***********************************************")
                    for file in glob.glob("*.c"):
                        compiler2.compile([f'{file}'])
                        compiler2.link_executable([f'{file}'], f'{file[:-2]}', libraries=[f'{libname}'])
                        print(f"STATUS: COMPILED SUCCESSFULLY (File: {file})")
                    print("***********************************************")
                else:
                    print("***********************************************")
                    for file2 in glob.glob("*.c"):
                        compiler2.compile([f'{file2}'])
                        compiler2.link_executable([f'{file2}'], f'{file2[:-2]}')
                        print(f"STATUS: COMPILED SUCCESSFULLY (File: {file2})")
                    print("***********************************************")

            except:
                print("-------------------------------------------------------------")
                print("Something went wrong during linking stage! please re-check.")
                print("-------------------------------------------------------------")

        if choice == '2':
            while True:
                compiler = new_compiler()
                print("Enter 'q' to quit the program.")
                i = input("Enter the name of file you wanna compile->  ")
                if i == 'q':
                    break
                try:
                    compiler.compile([f'{i}'])
                    exe = input("Enter the name for your executable file->  ")
                    link_lib2 = input("Link option?(y/n) (OPTIONAL): ")
                    if link_lib2 == 'y':
                        libname2 = input("linker option: ")
                        compiler.link_executable([f'{i}'], exe, libraries=[f'{libname2}'])
                        prompt = input("Run the compiled code?(yes/no): ")
                        print("-------------------------------------------")
                        if prompt == 'yes':
                            call(f'./{exe}')
                            print("-------------------------------------------")
                        elif prompt == 'no':
                            continue
                    elif link_lib2 == 'n':
                        compiler.link_executable([f'{i}'], exe)
                        prompt = input("Run the compiled code?(yes/no): ")
                        print("-------------------------------------------")
                        if prompt == 'yes':
                            call(f"./{exe}")
                            print("-------------------------------------------")
                        elif prompt == 'no':
                            continue
                except:
                    print("-------------------------------------------------------------")
                    print("File not found or something went wrong during linking stage!")
                    print("-------------------------------------------------------------")

        if choice == '3':
            print("Listing all c files in current directory...")
            for file in os.listdir():
                if file.endswith(".c"):
                    print(file)

        if choice == '4':
            if os.system("uname") == 0:
                os.system("dpkg --list | grep compiler")
            else:
                print("This won't print since uname gonna work anyway.")    # A friendly remainder for windows guys the reason it's not gonna
                                                                            # work on windows is because huh!! it's too long visit
                                                                            # https://stackoverflow.com/questions/59820244/has-windows-an-integrated-built-in-c-c-compiler-package
        if choice == '5':
            path = os.getcwd()
            print(f"Current working directory: {path}\n")

        if choice == '6':
            change_dir = os.chdir(os.path.expanduser('~'))   # Change to home dir.
            for folder in os.listdir():
                print(folder)
            print("\tListing done. ")
            print("Changed to home directory.")
            print("-----------------------------------------------------")
            print("Enter 'no' to stay in home dir!")
            response = input("do you wish to change directory?(yes/no):  ")
            if response == 'yes':
                change_dir2 = input("Enter the name of directory: ")
                try:
                    os.chdir(f"{change_dir2}")
                    print(f"Changed folder to {change_dir2}")
                except FileNotFoundError:
                    print("---------------------------------")
                    print("No such file or directory")
                    print("---------------------------------")
            elif response == 'no':
                continue


        if choice == '7':
            try:
                while True:
                    print("-------------------------")
                    print("Listing files..")
                    print("-------------------------")
                    for file in os.listdir():
                        print(file)
                    print("-------------------------")
                    print("Listing done..")
                    print("-------------------------")

                    print("Enter 'q' to exit (Please don't keep a file named q lol.)")
                    file_name = input("Enter the filename: ")
                    if file_name == 'q':
                        break
                    os.remove(f"{file_name}")
                    print("-------------------------")
                    print(f"File {file_name} has been deleted.")
            except FileNotFoundError:
                print("\n")
                print("File not found or something went wrong!")
                print("\n")


        if choice == '8':
            print("-------------------------")
            print("Bye onii chan.")
            print("It was nice to see you.")
            quit()

keep_running()

# I could've shorted the whole script in many functions but it's not necessary
# it's easy to read this way by looking at choice number. I tried functions after
# completing the script but it made code more messy and hard to understand.
