#CRUD
#Project1
global default, e101, e102, e103
Clients = "Luis, Mateo, "
default = " "
e101 = "Error 101: Wrong value"
e102 = "Error 102: The client is already in the list"
e103 = "Error 103: The client is not in the list"

def _print_welcome():
    print("*"*15)
    print("* Welcome to  *")
    print("*"*15)
    print("What would you like to do?")

def _print_menu():
    print("[C]reate a new user")
    print("[R]ead an user")
    print("[U]pdate an user")
    print("[D]elete an user")

def Menu():
    option = input("Select an option: ").upper()
    if option == "C":
        CClient()
    elif option == "R":
        RClient()
    elif option == "U":
        UClient()
    elif option == "D":
        DClient()
    else:
        print(e101)

def _get_client_name(m):
    if (m == default):
        return input("Enter the client name: ").lower().capitalize()
    else:
        return input(m).lower().capitalize()

def list_clients():
    global Clients
    print(Clients)

def CClient():
    global Clients

    client_name = _get_client_name(default)

    if not (client_name in Clients):
        Clients += client_name + ", "

    else:
        print(e102)

def RClient():
    global Clients

    client_name = _get_client_name(default)

    if (client_name in Clients):
        print("the client ",client_name, " is in the list")

    else:
        print(e103)

def UClient():
    global Clients

    client_name = _get_client_name(default)
    if (client_name in Clients):
        new_client_name = _get_client_name("Enter the new name: ")
        Clients = Clients.replace(client_name, new_client_name)

    else:
        print(e103)

def DClient():
    global Clients

    client_name = _get_client_name(default)
    if (client_name in Clients):
        Clients = Clients.replace(client_name + ", ", "")

    else:
        print(e103)

def main():
    _print_welcome()
    _print_menu()
    Menu()
    list_clients()

if __name__ == "__main__":
    main()