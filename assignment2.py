import sys


# Global variable for the token
token = ' '
i = 0

# Early error detection 
class Error(Exception):
    pass

def expr():
    global token, i
    try:
        temp = term()
        while i < len(token) and token[i] in ('+', '-'):
            if token[i] == '+':
                i += 1
                temp += term()
            elif token[i] == '-':
                i += 1
                temp -= term()
        return temp
    except Error:
        raise Error("Invalid ")


def term():
    global token, i
    try:
        temp = factor()
        while i < len(token) and token[i] == '/':
            i += 1
            temp /= factor()
        while i < len(token) and token[i] == '*':
            i += 1
            temp *= factor()
        while i < len(token) and token[i] == '%':
            i += 1
            temp %= factor()
        return temp
    except Error:
        raise Error("Invalid syntax")


def factor():
    global token, i
    if i < len(token) and token[i] == '(':
        i += 1
        temp = expr()
        if i < len(token) and token[i] == ')':
            i += 1
        else:
            raise Error("Invalid Placement")
    elif i < len(token) and token[i].isdigit():
        start = i
        while i < len(token) and token[i].isdigit():
            i += 1
        temp = int(token[start:i])
    else:
        raise Error("Invalid token")
    return temp

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tokenize_expr(expr):
    operators = ['+', '-', '*', '/', '%']
    tokens = []
    current_token = ""
    for char in expr:
        if char in operators:
            if current_token:
                tokens.append(current_token)
            tokens.append(char)
            current_token = ""
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return build_expr_tree(tokens)


def build_expr_tree(tokens):
    if len(tokens) == 1:
        return TreeNode(tokens[0])
    else:
        operator = tokens.pop(1)
        return TreeNode(operator, build_expr_tree(tokens[:1]), build_expr_tree(tokens[1:]))


def print_tree(node, space=""):
    if node:
        print(space + node.value)
        if node.left:
            print_tree(node.left)
        if node.right:
            print_tree(node.right, space + " " * len(node.value))


if __name__ == "__main__":
    result = 0
    print("A RECURSIVE-DESCENT CALCULATOR.")
    print("\t the valid operations are +, - and *")
    user_input = input("Enter the calculation string, e.g. '34+6*56': ")
    #Tolerate empty space by removing it :) 
    user_input = user_input.replace(" ", "")
    parse_tree = tokenize_expr(user_input)
    print_tree(parse_tree)
    token = user_input + ' '

    try:
        result = expr()
        if i == len(token) - 1:
            print(f"Result = {result}")
        else:
            print("Error Detected ")
            print("Syntax Error: Invalid input")
    except Error as e:
        print(f"Error: {e}")
