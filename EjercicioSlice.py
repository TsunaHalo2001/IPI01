def main():
    name = "uniValle"
    print(name)

    name = name.lower()
    print(name)

    name = name.upper()
    print(name)

    name = name.capitalize()
    print(name)

    name = name.replace("a","A")
    print(name)

    len(name)

    name = "     " + name
    print(name)

    name = name.strip()
    print(name)

    print(name[0:3])

if __name__ == "__main__":
    main()