from typing import Set, Tuple

from .logic_circuit import LogicCircuit


class HalfSubtractor(LogicCircuit):
  """
  Truth table:

  A  B | Difference  Borrow-Out
  -----------------------------
  0  0 |     0           0
  0  1 |     1           1
  1  0 |     1           0
  1  1 |     0           0

  Equation:
  - Difference = A xor B
  - Borrow-Out = (1 - A) and B

  Ref:
  - https://en.wikipedia.org/wiki/Subtractor
  - https://www.youtube.com/watch?v=SV4VTYWxKV4
  """
  def subtract(self, a: int, b: int) -> Tuple[int]:
    str_a = str(a)
    str_b = str(b)

    assert LogicCircuit.is_binary(str_a), ValueError('input should be 0 or 1')
    assert LogicCircuit.is_binary(str_b), ValueError('input should be 0 or 1')

    print(
      f'Half Subtractor subtracting {a} and {b}...\n'
      f'\n'
      f'Operators:\n'
      f'    & = AND\n'
      f'    ^ = XOR\n'
      f'\n'
      f'Equations:\n'
      f'    Difference = A ^ B\n'
      f'    Borrow-Out = (1 - A) & B\n'
    )

    _difference = self._xor(str_a, str_b)
    _borrow_out = self._and(str(1 - a), str_b)

    print(
      f'{"  " + str_a}\n'
      f'{"  " + str_b}\n'
      f'- ^\n'
      f' --\n'
      f'{"  " + _difference} ({_borrow_out})\n'
      f'difference = {str_a} XOR {str_b} = {_difference}\n'
      f'borrow-out = (1 - {str_a}) AND {str_b} = {_borrow_out}'
    )

    return (int(_difference), int(_borrow_out))
