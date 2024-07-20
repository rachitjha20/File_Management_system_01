import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f'file {filename}: Created Successfully')
    except FileExistsError:
        print(f"file {filename} alreadt present.")

    except Exception as E:
        print("An error occured.")

def view_files():
    files = os.listdir()
    if not files:
        print("No file found.")
    else :
        print("File present in directory!!!!!")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been removed.")

    except FileNotFoundError:
        print("File not Found")
    
    except Exception as e:
        print("An error occured.")

def read_file(filename):

    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f'Content of {filename} : \n {content}')

    except FileNotFoundError:
        print("File not Found")
    
    except Exception as e:
        print("An error occured.")

def write_file(filename):
    try:
        with open('sample.txt', 'w') as f:
            content = input("Enter data taht needs to be added: \n")
            f.write(content+ '\n')
            print('content added to {filename} !!!')
        
    except FileNotFoundError:
        print("File not Found")
    
    except Exception as e:
        print("An error occured.")

def main():
    while True:
        print(*"FILE MANAGENET APPLICATION")
        print('1. Create File')
        print('2. View File')
        print('3. Delete File')
        print('4. Read File')
        print('5. Write File')
        print('6. Exit')

        choice = int(input('What would you like to do. Chose 1-6:: '))

        if choice == 1:
            filename = input("Enter the file name: ")
            create_file(filename)
        elif choice == 2:
            print("Files are below to read")
            view_files()
        elif choice == 3:
            filename = input("Enter the file that needs to be deleted: ")
            delete_file(filename)
        elif choice == 4:
            filename = input("Enter the file that needs to be read: ")
            read_file(filename)
        elif choice == 5:
            filename = input("Enter the file name for editing: ")
            write_file(filename)
        elif choice == 6:
            print("Bye Bye..... Have a great day.....")
            break
        else:
            print("Invalid Option. Chose again.")

if __name__ == "__main__":
    main()
