from typing import Set

from .logic_circuit import LogicCircuit


class FullSubtractor(LogicCircuit):
    """
    Truth table:

    A  B  Borrow-In | Difference  Borrow-Out
    ----------------------------------------
    0  0      0     |     0           0
    0  0      1     |     1           1
    0  1      0     |     1           1
    0  1      1     |     0           1
    1  0      0     |     1           0
    1  0      1     |     0           0
    1  1      0     |     0           0
    1  1      1     |     1           1

    Equation:
    - Difference = A xor B xor Borrow-In
    - Borrow-Out = ((1 - A) and B) or ((1 - (A xor B)) and Borrow-In)

    Ref:
    - https://en.wikipedia.org/wiki/Subtractor
    - https://www.youtube.com/watch?v=dBXGGWbtt6U
    """

    def subtract(self, a: int, b: int) -> int:
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]

        str_a, str_b = self._pad_two_to_same_len(str(a), str(b), ' ', 'start')
        bin_a, bin_b = self._pad_two_to_same_len(bin_a, bin_b)
        bin_a_re, bin_b_re = bin_a[::-1], bin_b[::-1]
        
        print(
            f'Full Subtractor subtracting {a} and {b}...\n'
            f'    binary of {str_a}: {bin_a}\n'
            f'    binary of {str_b}: {bin_b}\n'
            f'\n'
            f'Operators:\n'
            f'    & = AND\n'
            f'    ^ = XOR\n'
            f'    | = OR\n'
            f'\n'
            f'Equations:\n'
            f'    Difference = A ^ B ^ Borrow-In\n'
            f'    Borrow-Out = ((1 - A) & B) | ((1 - (A ^ B)) & Borrow-In)\n'
        )

        n = len(bin_a)
        result = ''

        _difference = '0'
        _borrow_in = '0'
        _borrow_out = '0'

        for i in range(n):
            print(
                f'step {i+1}:\n'
                f'    {"  " + bin_a}\n'
                f'    {"  " + bin_b}\n'
                f'    {"- " + " " * (n-i-1)}^'
            )

            _difference = self._xor(
                self._xor(bin_a_re[i], bin_b_re[i]),
                _borrow_in,
            )

            _borrow_out = self._or(
                self._and(
                    str(1 - int(bin_a_re[i])),
                    bin_b_re[i],
                ),
                self._and(
                    str(1 - int(self._xor(bin_a_re[i], bin_b_re[i]))),
                    _borrow_in,
                ),
            )

            result += _difference
            
            print(
                f'    {" " + "-" * (n+1)}\n'
                f'    {" " * (n+2-len(result))}{result[::-1]} ({_borrow_out})\n'
                f'    difference = {bin_a_re[i]} ^ {bin_b_re[i]} ^ {_borrow_in} = {_difference}\n'
                f'    borrow-out = (1 - ({bin_a_re[i]} & {bin_b_re[i]})) | ((1 - ({bin_a_re[i]} ^ {bin_b_re[i]})) & {_borrow_in}) = {_borrow_out}'
            )

            _borrow_in = _borrow_out

        # A < B, take negative of each difference digit, then add 1
        if _borrow_in == '1':
            result = ''.join([str(1 - int(e)) for e in result])
            result = result[::-1]
            result = self._trim_start(result)
            result_int = -(int('0b' + result, 2) + 1)
            result_bin = '-' + bin(result_int)[3:]
        # A >= B
        else:
            result_str = result[::-1]
            result_bin = self._trim_start(result_str)
            result_int = int('0b' + result_bin, 2)
        
        print(f'\nfinal reslut: subtracting {a} and {b} in binary is {result_bin}, converted to integer is {result_int}')

        return result_int
