import csv

def main():
    with open("users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    while True:
        user = input("Enter your username: ")
        try:
            for row in file:
                if row[0] == user:
                    print("username found", user)
                    user_found = [row[0],row[1]]
                    pass_check(user_found)
                else:
                    print("not found")
        except: 
            print('Processing error')

def pass_check(user_found):
    while True:

        user = input("enter your password: ")
        try:
            if user_found[1] == user:
                print("password match")
                print('Logged in.')
                break
            else:
                print("password not match")
                user_find(file_reader)
        except: 
            print('Processing error')
main()