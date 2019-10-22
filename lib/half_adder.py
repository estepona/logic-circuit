from typing import Set, Tuple

from .logic_circuit import LogicCircuit


class HalfAdder(LogicCircuit):
  """
  Truth table:

  A  B | Sum  Carry-Out
  ---------------------
  0  0 |  0       0
  0  1 |  1       0
  1  0 |  1       0
  1  1 |  0       1

  Equation:
  - Sum = A xor B
  - Carry-Out = A and B

  Ref:
  - https://en.wikipedia.org/wiki/Adder_(electronics)
  - https://www.youtube.com/watch?v=aLUY-s7LSns
  """
  def add(self, a: int, b: int) -> Tuple[int]:
    str_a = str(a)
    str_b = str(b)

    assert LogicCircuit.is_binary(str_a), ValueError('input should be 0 or 1')
    assert LogicCircuit.is_binary(str_b), ValueError('input should be 0 or 1')

    print(
      f'Half Adder adding {a} and {b}...\n'
      f'\n'
      f'Operators:\n'
      f'    & = AND\n'
      f'    ^ = XOR\n'
      f'\n'
      f'Equations:\n'
      f'    Sum = A ^ B\n'
      f'    Carry-Out = A & B\n'
    )

    _sum = self._xor(str_a, str_b)
    _carry_out = self._and(str_a, str_b)

    print(
      f'{"  " + str_a}\n'
      f'{"  " + str_b}\n'
      f'+ ^\n'
      f' --\n'
      f'{"  " + _sum} ({_carry_out})\n'
      f'sum       = {str_a} XOR {str_b} = {_sum}\n'
      f'carry-out = {str_a} AND {str_b} = {_carry_out}'
    )

    return (int(_sum), int(_carry_out))
