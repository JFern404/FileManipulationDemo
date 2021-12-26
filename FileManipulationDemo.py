#Jonathan Fernandez 1002267273 12/11/2021 CIS 1531
import os

def get_menu():
    print("Please enter a number that represents an option below:")
    while True:
        try:
            user_menu_input = int(input("1-Create a file\n2-Delete a file\n3-Write to a file\n4-Read a file\n5-Create a directory\n6-Change Directory\n7-Exit\n>>>"))
            break
        except ValueError:
            print("Your entry was invalid, please enter a number corresponding to the options provided.")
    return user_menu_input

def file_creation():
    while True:
        try:
            file_name = input("Enter the name of the file you would like to create followed by the .txt extension:\n>>>")
            file_created = open(file_name,"x")
            file_created.close()
            break
        except:
            print("That file already exists please choose a different name.\n")

def file_deletion():
    while True:
            file_name = input("Enter the name of the file you would like to delete followed by the .txt extension:\n>>>")
            if os.path.exists(file_name):
                os.remove(file_name)
                break
            else:
                print("The file you entered does not exist currently.")

def file_write():
    while True:
        try:
            file_name = input("Enter the name of the file you would like to write to followed by the .txt extension:\n>>>")
            user_choice = input("Would you like to append to or overwrite a file? A/O\n>>>")
            if user_choice == 'A' or user_choice == 'a':
                file_appended = open(file_name,'a')
                user_content = input("Enter what you would like to append to this file:\n>>>")
                file_appended.write(user_content)
                file_appended.close()
                break
            elif user_choice == "O" or user_choice == "o":
                file_appended = open(file_name,'w')
                user_content = input("Enter what you would like to overwrite this file with:\n>>>")
                file_appended.write(user_content)
                file_appended.close()
                break
            else:
                print("That wasn't a valid choice, please enter either A to append or O to overwrite\n")
        except:
            print("That file does not exist please choose a different name.\n")

def read_file():
    while True:
        try:
            print("Enter the name of the file you would like to read from, the entire directory can be used to find it. Remember to add the .txt extension.")
            file_name = input(">>>")
            file_content = open(file_name,'r')
            print('\n',file_content.read(),'\n')
            break
        except:
            print("\nThat file does not exist please choose a different name.\n")
            
def create_directory():
    while True:
        try:
            directory_path = input("Enter the path followed by the name of the directory you would like to create (Ex. C:/Desktop/newfilehere) :\n>>>")
            os.mkdir(directory_path)
            break
        except:
            print("Please enter a valid directory path such as the example presented to you previously.")
            
def user_directory_change():
    
    yes = ['Yes','YES','Y','y']
    no = ['No','NO','N','n']
    
    cwd = os.getcwd()
    print("The current directory is: ", cwd,'\n')
    
    user_dir_choice = input("Would you like to change the directory?\n>>>")
    while True:
        if user_dir_choice in yes:
            try:
                path = input('Please enter the path/directory you would like to reach:\n>>>')
                os.chdir(path)
                cwd = path
                print("The current directory is now:", cwd,'\n')
                break
            except FileNotFoundError:
                print("Directory:", path, "does not exist.\n")
            except NotADirectoryError:
                print(path, "is not a directory.\n")
            except PermissionError:
                print("You do not have permissions to change to.\n", path)
            except:
                print("That was invalid input please make sure it follows the correct structure of a path/directory.\n")   
        elif user_dir_choice in no:
            break
        else:
            user_dir_choice = input('That is not a valid option, please enter either Y or N\n>>>')
    print(cwd)
    return cwd

def main():
    menu = 0
    while True:
        menu = get_menu()
        if menu == 1:
            file_creation()
        elif menu == 2:
            file_deletion()
        elif menu == 3:
            file_write()
        elif menu == 4:
            read_file()
        elif menu == 5:
            create_directory()
        elif menu == 6:
            user_directory_change()
        elif menu == 7:
            exit()
        else:
            print("Please enter a number corresponding to the options provided:\n")

main()
