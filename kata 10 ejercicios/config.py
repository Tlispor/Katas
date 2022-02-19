def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except PermissionError:
        print("no tiene permiso")
if __name__ == '__main__':
    main()