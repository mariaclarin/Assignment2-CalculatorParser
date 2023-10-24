def error():
  print("Error")
  exit(1)

def match(token, expected_token):
  if token == expected_token:
    token = input()
  else:
    error()

def expr(token):
  print("expr")
  if token == "-":
    token = input()
    if not token.isdigit():
      error()
    temp = -int(token)
    token = input()
  else:
    temp = term(token)

  while token in "+-":
    if token == "+":
      match(token, "+")
      temp += term(token)
    elif token == "-":
      match(token, "-")
      temp -= term(token)
  return temp

def term(token):
  print("term")
  temp = factor(token)

  while token == "*":
    match(token, "*")
    temp *= factor(token)

  return temp


# THIS IS THE MAIN PART OF THE PROBLEM I CANT WORK IT OUTHJABDHJSBAHDBASH
def factor(token):
    print("factor")
    #the input goes straight into the else which prints error and exits
    #if u use ' if not token.isdigit() it works and if u try printing token before the if else, it prints the entire token
    #im guessing its bcs the program reads the input string as a whole string and not individual characters so need to 
    #somehow deal w that so it reads by char and not the whole thing maybe?

    #print(token)
    if token.isdigit():
        print("if")
        temp = int(token)
        #this input() is also a problem i think bcs dia jd minta user input again? but when i search 
        # it up it basically says its necessary to read the rest of the token input 
        token = input()
        if token == "*":
            print("if if ")
            match(token, "*")
            temp *= factor(token)
    elif token == "(":
        print("elif")
        match(token, "(")
        temp = expr(token)
        match(token, ")")

    else:
        error()

    return temp

def main():
  print("A RECURSIVE-DESCENT CALCULATOR.")
  print("\t the valid operations are +, - and *")
  print("Enter the calculation string, e.g. \'34+6*56\'\n")

  token = input()
  result = expr(token)

  if token == "\n":
    print("Result =", result)
  else:
    error()

if __name__ == "__main__":
  main()
