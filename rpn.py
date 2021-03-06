import readline
import operator
from colored import fg, bg, attr

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def funcy(someArg):
    newVal = someArg + 3
    if newVal > 5:
        newVal = newVal - 100
    else:
        newVal = newVal + 1000

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print("Result: ", fg(1), result, fg(15))
        else:
            print("Result: ", result, fg(15))

if __name__ == '__main__':
    main()
