from typing import Union


class Symbol:
    symbol: str = None
    symbol_list = []
    name:str = None

    def __init__(self):
        if self.symbol is None:
            raise ValueError("Symbol must have a defined symbol attribute.")
        if self.symbol not in self.symbol_list:
            self.symbol_list.append(self.symbol)


    def __call__(self, *args, **kwargs):
        """This method allows the symbol to be called like a function."""
        raise NotImplementedError("Subclasses must implement this method.")


class Constant(Symbol):
    def __init__(self, value: Union[int, float], symbol: str = None, symbol_list: Union[list, None] = None):
        super().__init__()
        self.value = value
        if symbol is None:
            self.symbol = str(value)
        else:
            self.symbol = symbol
        if self.symbol not in self.symbol_list:
            self.symbol_list.append(self.symbol)

        if symbol_list is not None:
            self.symbol_list.extend(symbol_list)

    def __call__(self, *args, **kwargs):
        """Returns the constant value."""
        return self.value


class Variable(Symbol):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        #Base name is the name without any numbers or suffixes.
        self.base_name = name.rstrip('0123456789').rstrip("_")
        self.symbol = name
        self.symbol_list.append(name)

    def __call__(self, *args, **kwargs):
        """Returns the value of the variable."""
        return kwargs.get(self.name, None)

class Operator(Symbol):
    def __init__(self, a: Symbol, b: Symbol):
        super().__init__()
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        a_val = self.a(*args, **kwargs)
        b_val = self.b(*args, **kwargs)
        return a_val, b_val

class SymbolGroup(Symbol):
    symbol = "("
    symbol_list = ['(', ')']

    def __init__(self, *symbols: Symbol):
        super().__init__()
        self.symbols = symbols
        self.symbol_list.extend([s.symbol for s in symbols])



class Add(Operator):
    symbol = '+'
    def __call__(self, *args, **kwargs):
        a, b = super().__call__(*args, **kwargs)
        return a + b

class Subtract(Operator):
    symbol = '-'
    def __call__(self, *args, **kwargs):
        a, b = super().__call__(*args, **kwargs)
        return a - b

class Multiply(Operator):
    symbol = '*'
    def __call__(self, *args, **kwargs):
        a, b = super().__call__(*args, **kwargs)
        return a * b

class Divide(Operator):
    symbol = '/'
    def __call__(self, *args, **kwargs):
        a, b = super().__call__(*args, **kwargs)
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

class Modulus(Operator):
    symbol = '%'
    symbol_list = ['%', 'mod']
    def __call__(self, *args, **kwargs):
        a, b = super().__call__(*args, **kwargs)
        return a % b

class Power(Operator):
    symbol = '^'
    def __call__(self, *args, **kwargs):
        a, b = super().__call__(*args, **kwargs)
        return a ** b

class Sqrt(Operator):
    symbol = 'sqrt'
    symbol_list = ['sqrt', '√']

    def __init__(self, a: Symbol, b: Union[None, Symbol] = None):
        super().__init__(a, None)

    def __call__(self, *args, **kwargs):
        a_val = self.a(*args, **kwargs)
        if a_val < 0:
            raise ValueError("Square root of negative number is not allowed.")
        return a_val ** 0.5