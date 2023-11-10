#CRUD
#Project1
global default, e101, e102, e103
clients = ["Luis", "Mateo"]
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

def menu():
    option = input("Select an option: ").upper()
    if option == "C":
        cclient()
    elif option == "R":
        rclient()
    elif option == "U":
        uclient()
    elif option == "D":
        dclient()
    else:
        print(e101)

def _get_client_name(m):
    if (m == default):
        return input("Enter the client name: ").lower().capitalize()
    else:
        return input(m).lower().capitalize()

def list_clients():
    global clients
    print(clients)

def cclient():
    global clients

    client_name = _get_client_name(default)

    if not (client_name in clients):
        clients += client_name + ", "

    else:
        print(e102)

def rclient():
    global clients

    client_name = _get_client_name(default)

    if (client_name in clients):
        print("the client ",client_name, " is in the list")

    else:
        print(e103)

def uclient():
    global clients

    client_name = _get_client_name(default)
    if (client_name in clients):
        new_client_name = _get_client_name("Enter the new name: ")
        clients = clients.replace(client_name, new_client_name)

    else:
        print(e103)

def dclient():
    global clients

    client_name = _get_client_name(default)
    if (client_name in clients):
        clients = clients.replace(client_name + ", ", "")

    else:
        print(e103)

def main():
    _print_welcome()
    _print_menu()
    Menu()
    list_clients()

if __name__ == "__main__":
    main()
