def showlogo():
    open_logo = open("logo.txt","r")
    read_logo = open_logo.read()
    print(read_logo)
    open_logo.close()