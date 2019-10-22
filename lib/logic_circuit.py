from abc import ABC
from typing import Set, Tuple, Union


class LogicCircuit(ABC):
  @staticmethod
  def is_binary(n: str) -> bool:
    return True if n in ['0', '1'] else False

  def _pad_start(self, n: str, size: int = 0, pad_with: str = '0') -> str:
    return size*pad_with + n

  def _pad_end(self, n: str, size: int = 0, pad_with: str = '0') -> str:
    return n + size*pad_with

  def _pad_two_to_same_len(self, a: str, b: str, pad_with: str = '0', pad_to: str = 'start') -> Set[str]:
    la, lb = len(a), len(b)
    dl = abs(la - lb)

    if pad_to == 'start':
      if la > lb:
        b = self._pad_start(b, dl, pad_with)
      elif la < lb:
        a = self._pad_start(a, dl, pad_with)

    elif pad_to == 'end':
      if la > lb:
        b = self._pad_end(b, dl, pad_with)
      elif la < lb:
        a = self._pad_end(a, dl, pad_with)

    return (a, b)

  def _trim_start(self, n: str) -> str:
    pos = -1

    for i in range(len(n)):
      if n[i] == '1':
        pos = i
        break

    return n[pos:] if pos != -1 else '0'

  def _and(self, a: str, b: str) -> str:
    assert LogicCircuit.is_binary(a), ValueError('input should be 0 or 1')
    assert LogicCircuit.is_binary(b), ValueError('input should be 0 or 1')

    return str(int(a) & int(b))

  def _or(self, a: str, b: str) -> str:
    assert LogicCircuit.is_binary(a), ValueError('input should be 0 or 1')
    assert LogicCircuit.is_binary(b), ValueError('input should be 0 or 1')

    return str(int(a) | int(b))

  def _xor(self, a: str, b: str) -> str:
    assert LogicCircuit.is_binary(a), ValueError('input should be 0 or 1')
    assert LogicCircuit.is_binary(b), ValueError('input should be 0 or 1')

    return str(int(a) ^ int(b))
