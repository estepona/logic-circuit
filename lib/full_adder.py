from typing import Set


class FullAdder():

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

    @staticmethod
    def is_binary(n: str) -> bool:
        if n == '0' or n == '1':
            return True
        else:
            return False
    
    def _pad_start(self, n: str, size: int = 0, pad_with: str = '0') -> str:
        return size * pad_with + n
    
    def _pad_end(self, n: str, size: int = 0, pad_with: str = '0') -> str:
        return n + size * pad_with
    
    def _pad_two_to_same_len(self, a: str, b: str, pad_with: str = '0', pad_to: str = 'start') -> Set[str]:
        l_a = len(a)
        l_b = len(b)
        dl = abs(l_a - l_b)

        if pad_to == 'start':
            if l_a > l_b:
                b = self._pad_start(b, dl, pad_with)
            elif l_a < l_b:
                a = self._pad_start(a, dl, pad_with)

        elif pad_to == 'end':
            if l_a > l_b:
                b = self._pad_end(b, dl, pad_with)
            elif l_a < l_b:
                a = self._pad_end(a, dl, pad_with)
        
        return (a, b)

    def _trim_start(self, n: str) -> str:
        for i in range(len(n)):
            if n[i] == '1':
                pos = i
                break

        return n[pos:]

    def _and(self, a: str, b: str) -> str:
        assert FullAdder.is_binary(a), ValueError('input should be 0 or 1')
        assert FullAdder.is_binary(b), ValueError('input should be 0 or 1')

        if a == '1' and b == '1':
            return '1'
        else:
            return '0'

    def _xor(self, a: str, b: str) -> str:
        assert FullAdder.is_binary(a), ValueError('input should be 0 or 1')
        assert FullAdder.is_binary(b), ValueError('input should be 0 or 1')

        if a != b:
            return '1'
        else:
            return '0'
