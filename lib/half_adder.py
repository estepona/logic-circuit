from typing import Set, Tuple

from .logic_circuit import LogicCircuit


class HalfAdder(LogicCircuit):
    """
    Truth table:

    A  B | Sum  Carry
    -----------------
    0  0 |  0     0
    0  1 |  1     0
    1  0 |  1     0
    1  1 |  0     1

    Ref:
    - https://en.wikipedia.org/wiki/Adder_(electronics)
    - https://www.youtube.com/watch?v=aLUY-s7LSns
    """

    def add(self, a: int, b: int) -> Tuple[int]:
        sa = str(a)
        sb = str(b)

        assert LogicCircuit.is_binary(sa), ValueError('input should be 0 or 1')
        assert LogicCircuit.is_binary(sb), ValueError('input should be 0 or 1')

        print(f'half adder adding {a} and {b}...\n')

        _sum = self._xor(sa, sb)
        _carry = self._and(sa, sb)

        print(
            f'{"  " + sa}\n'
            f'{"  " + sb}\n'
            f'+ ^\n'
            f' --\n'
            f'{"  " + _sum} ({_carry})\n'
            f'calculating sum digit:\n'
            f'    XOR of {sa} and {sb} is {_sum}\n'
            f'calculating carry-out digit:\n'
            f'    AND of {sa} and {sb} is {_carry}'
        )

        return (int(_sum), int(_carry))
