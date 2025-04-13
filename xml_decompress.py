import sys

def main():
    indent = 0
    char = ''
    while True:
        next = sys.stdin.read(1)
        match(char):
            case "<":
                if next != '/':
                    indent += 1
                print("<", end='')
            case ">":
                print(">\n" + ("  "*indent), end='')
            case "/":
                indent -= 1
                print("/", end='')
            case _:
                print(char, end='')
        char = next
        if not char:
            break


if __name__ == '__main__':
    main()
