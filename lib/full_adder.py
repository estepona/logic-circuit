from typing import Set

from .logic_circuit import LogicCircuit


class FullAdder(LogicCircuit):
    """
    Truth table:

    A  B  Carry-In | Sum  Carry-Out
    -------------------------------
    0  0      0    |  0       0
    0  0      1    |  1       0
    0  1      0    |  1       0
    0  1      1    |  0       1
    1  0      0    |  1       0
    1  0      1    |  0       1
    1  1      0    |  0       1
    1  1      1    |  1       1

    Equation:
    - Sum = A xor B xor Carry-In
    - Carry-Out = (A and B) or ((A xor B) and Carry-In)

    Ref:
    - https://en.wikipedia.org/wiki/Adder_(electronics)
    - https://www.youtube.com/watch?v=RK3P9L2ZXk4
    """

    def add(self, a: int, b: int) -> int:
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]

        str_a, str_b = self._pad_two_to_same_len(str(a), str(b), ' ', 'start')
        bin_a, bin_b = self._pad_two_to_same_len(bin_a, bin_b)
        bin_a_re, bin_b_re = bin_a[::-1], bin_b[::-1]
        
        print(
            f'Full Adder adding {a} and {b}...\n'
            f'    binary of {str_a}: {bin_a}\n'
            f'    binary of {str_b}: {bin_b}\n'
            f'\n'
            f'Operators:\n'
            f'    & = AND\n'
            f'    ^ = XOR\n'
            f'    | = OR\n'
            f'\n'
            f'Equations:\n'
            f'    Sum = A ^ B ^ Carry-In\n'
            f'    Carry-Out = (A & B) | ((A ^ B) & Carry-In)\n'
        )

        n = len(bin_a)
        result = ''

        _sum = '0'
        _carry_in = '0'
        _carry_out = '0'

        for i in range(n):
            print(
                f'step {i+1}:\n'
                f'    {"  " + bin_a}\n'
                f'    {"  " + bin_b}\n'
                f'    {"+ " + " " * (n-i-1)}^'
            )

            _sum = self._xor(
                self._xor(bin_a_re[i], bin_b_re[i]),
                _carry_in,
            )

            _carry_out = self._or(
                self._and(bin_a_re[i], bin_b_re[i]),
                self._and(
                    self._xor(bin_a_re[i], bin_b_re[i]),
                    _carry_in,
                ),
            )

            result += _sum
            if i == n - 1 and _carry_out != '0':
                result += _carry_out
            
            print(
                f'    {" " + "-" * (n+1)}\n'
                f'    {" " * (n+2-len(result))}{result[::-1]} ({_carry_out})\n'
                f'    sum       = {bin_a_re[i]} ^ {bin_b_re[i]} ^ {_carry_in} = {_sum}\n'
                f'    carry-out = ({bin_a_re[i]} & {bin_b_re[i]}) | (({bin_a_re[i]} ^ {bin_b_re[i]}) & {_carry_in}) = {_carry_out}'
            )

            _carry_in = _carry_out

        result_str = result[::-1]
        result_bin = self._trim_start(result_str)
        result_int = int('0b' + result_bin, 2)
        
        print(f'\nfinal reslut: adding {a} and {b} in binary is {result_bin}, converted to integer is {result_int}')

        return result_int
