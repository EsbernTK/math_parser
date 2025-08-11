from symbols import *

class MathParser:

    def __init__(self):
        self.symbols = {}
        self.symbol_list = []



if __name__ == '__main__':
    print(ALL_SYMBOLS)
    parser = MathParser()
    # Example usage:
    parser.symbols['x'] = Variable('x')
    parser.symbols['y'] = Variable('y')
    parser.symbols['add'] = Add(parser.symbols['x'], parser.symbols['y'])

    print("Symbols:", parser.symbols)
    print("Symbol List:", parser.symbol_list)

    # Call the add operator
    result = parser.symbols['add'](x=5, y=3)
    print("Result of add:", result)  # Should output 8