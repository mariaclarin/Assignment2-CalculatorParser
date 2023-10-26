import sys

# Global variable for the token
token = ' '


def error():
    sys.stderr.write("Error\n")
    sys.exit(1)


def match(expected_token):
    global token
    if token == expected_token:
        token = sys.stdin.read(1)
    else:
        error()


def expr():
    temp = term()
    while token in ('+', '-'):
        if token == '+':
            match('+')
            temp += term()
        elif token == '-':
            match('-')
            temp -= term()
    return temp


def term():
    temp = factor()
    while token == '*':
        match('*')
        temp *= factor()
    return temp


def factor():
    global token
    temp = 0
    if token == '(':
        match('(')
        temp = expr()
        match(')')
    elif token.isdigit():
        while token.isdigit():
            temp = temp * 10 + int(token)
            token = sys.stdin.read(1)
    else:
        error()
    return temp


def main():
    global token
    result = 0
    print("A RECURSIVE-DESCENT CALCULATOR.")
    print("\t the valid operations are +, - and *")
    print("Enter the calculation string, e.g. '34+6*56'")
    token = sys.stdin.read(1)
    result = expr()
    if token == '\n':
        print("Result =", result)
    else:
        error()


if __name__ == "__main__":
    main()
