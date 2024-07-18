from pprint import pprint

from console import find_all, create, find, delete, update


def main():
    while True:
        command = input(">")
        if command == 'find_all':
            pprint(find_all())
        if command == 'create':
            create()
        if command == 'find':
            pprint(find())
        if command == 'delete':
            delete()
        if command == 'update':
            update()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
