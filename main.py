"""Этот модуль предназначен для вычисления RPN

"""
# expression = input()

def evaluate(expression):
    """Функция для вычисления RPN
    :param expression:
    :return:
    """
    expression = infix_to_postfix(expression).split()
    stack = []

    for ele in expression:
        if ele not in '/*+-^':
            stack.append(int(ele))

        else:
            right = stack.pop()
            left = stack.pop()

            if ele == '+':
                stack.append(left + right)

            elif ele == '-':
                stack.append(left - right)

            elif ele == '*':
                stack.append(left * right)

            elif ele == '/':
                stack.append(int(left / right))
            elif ele == '^':
                stack.append(int(left ** right))
            else:
                raise ValueError


    return stack.pop()


def infix_to_postfix(expression):
    """Фукнция для преобразования из инфиксной в постфиксную
    :param expression:
    :return:
    """
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    def is_operator(char):
        return char in precedence

    def is_operand(char):
        return char.isalnum()

    stack = []
    postfix = ""

    for char in expression:
        if is_operand(char):
            postfix += ' ' + char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += ' ' + stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()
        elif is_operator(char):
            while stack and is_operator(stack[-1]) and precedence[stack[-1]] >= precedence[char]:
                postfix += ' ' + stack.pop()
            stack.append(char)

    while stack:
        postfix += ' ' + stack.pop()
    return postfix
