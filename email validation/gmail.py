from curses.ascii import isalpha


email = input("Enter Your Email : ")
k = 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@") == 1):
            if(email[-4] == ".")^(email[-3] == "."):
                for i in email:
                    if(i == i.isspace()):
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        k = 1
                if k == 1:
                    print("Failed 5 !")
                else:
                    print("Right Email")
            else:
                print("Failed 4 !")
        else:
            print("Failed 3 !")
    else:
        print("Failed 2 !")
else:
    print("Failed 1 !")