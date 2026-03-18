def main():
    expression = input("Expression: ").lower().strip()

    # * unpacks the list iterable returned from getParts
    # so it can be used as args for calculate
    # skips allocating to a variable
    print(f"{calculate(*getParts(expression)):.1f}")
    
def calculate(lOp: int, op: str, rOp: int):
    match op:
        case "+":
            return lOp + rOp
        case "-":
            return lOp - rOp
        case "*":
            return lOp * rOp
        case "/":
            return lOp / rOp

def getParts(expression: str):
    parts = expression.split(" ")

    return [float(parts[0]), parts[1], float(parts[2])]

main()