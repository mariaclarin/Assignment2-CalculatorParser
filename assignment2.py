tokens = []

def error():
    print("Error")
    exit(1)

def match(expected_token):
    global tokens
    if tokens and tokens[0] == expected_token:
        tokens.pop(0)
    else:
        error()

def expr():
    global tokens
    while tokens and tokens[0].isspace():
        tokens.pop(0)
    if not tokens:
        return 0

    temp = term()
    while tokens and tokens[0] in ('+', '-', '%', '/'):
        while tokens and tokens[0].isspace():
            tokens.pop(0)
        if not tokens:
            break
        if tokens[0] == '+':
            match('+')
            temp += term()
        elif tokens[0] == '-':
            match('-')
            temp -= term()
        elif tokens[0] == '%':
            match('%')
            temp %= term()
        elif tokens[0] == '/':
            match('/')
            temp /= term()
    return temp

def term():
    global tokens
    while tokens and tokens[0].isspace():
        tokens.pop(0)
    if not tokens:
        return 0

    temp = factor()
    while tokens and tokens[0] == '*':
        while tokens and tokens[0].isspace():
            tokens.pop(0)
        if not tokens:
            break
        match('*')
        temp *= factor()
    return temp

def factor():
    global tokens
    while tokens and tokens[0].isspace():
        tokens.pop(0)
    if not tokens:
        return 0

    temp = 0
    if tokens[0] == '(':
        match('(')
        temp = expr()
        match(')')
    elif tokens[0].isdigit():
        while tokens and tokens[0].isdigit():
            temp = temp * 10 + int(tokens[0])
            tokens.pop(0)
    else:
        error()
    return temp

def main():
    global tokens
    result = 0
    print("\n==========================================================")
    print("A RECURSIVE-DESCENT CALCULATOR.")
    print("\t the valid operations are +, -, *, /, and %")
    print("Enter the calculation string, e.g. '34+6*56/5%3': ")

    while True:
        input_token =input(">> ")
        tokens.clear() 
        tokens.extend(input_token.replace(" ", ""))
        
        try:
            result = expr()
            if not tokens:
                print("Result =", result)
                print("==========================================================\n")
                break
            else:
                print("Invalid input string, please re-enter.")

        except:
                print("Invalid input string, please re-enter.")


main()