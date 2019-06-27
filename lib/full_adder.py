from typing import Set

from .logic_circuit import LogicCircuit


class FullAdder(LogicCircuit):

    def add(self, a: int, b: int) -> int:
        v1: str = bin(a)[2:]
        v2: str = bin(b)[2:]

        sa, sb = self._pad_two_to_same_len(str(a), str(b), ' ', 'start')
        v1, v2 = self._pad_two_to_same_len(v1, v2)
        v1_r, v2_r = v1[::-1], v2[::-1]
        
        print(f'adding {a} and {b}...\n'
              f'    binary of {sa}: {v1}\n'
              f'    binary of {sb}: {v2}\n')

        lv = len(v1)
        result = ''
        _i = '0'
        _o1 = '0'

        for i in range(lv):
            print(f'step {i+1}:\n'
                  f'    {"  " + v1}\n'
                  f'    {"  " + v2}\n'
                  f'    {"+ " + " " * (lv-i-1)}^')

            _s1 = self._xor(v1_r[i], v2_r[i])
            _s2 = self._xor(_s1, _i)

            _o1 = self._and(v1_r[i], v2_r[i])
            _o2 = self._and(_s1, _i)
            _o3 = self._xor(_o1, _o2)

            result += _s2
            if i == lv - 1 and _o3 != '0':
                result += _o3
            
            print(f'    {" " + "-" * (lv+1)}\n'
                  f'    {" " * (lv+2-len(result))}{result[::-1]} ({_o3})\n'
                  f'    calculating sum digit:\n'
                  f'        XOR of {v1_r[i]} and {v2_r[i]} as s1 is {_s1},\n'
                  f'        XOR of s1 {_s1} and carry-in {_i} as sum digit is {_s2}\n'
                  f'    calculating carry-out digit:\n'
                  f'        AND of {v1_r[i]} and {v2_r[i]} is o1 {_o1},\n'
                  f'        AND of s1 {_s1} and carry-in {_i} as o2 is {_o2},\n'
                  f'        XOR of o1 {_o1} and o2 {_o2} as carry-out digit is {_o3}')

            _i = _o3
        
        result_str = result[::-1]
        result_bin = self._trim_start(result_str)
        result_int = int('0b' + result_bin, 2)
        
        print(f'\nfinal reslut: adding {a} and {b} in binary is {result_bin}, converted to integer is {result_int}')

        return result_int
