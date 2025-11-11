"""Этот модуль предназначен для вычисления RPN

"""

def evaluate(expression):
    """Функция для вычисления RPN
    :param expression:
    :return:
    """
    expression = expression.split()
    stack = []

    for ele in expression:
        if ele not in '/*+-':
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
            else:
                raise ValueError


    return stack.pop()
