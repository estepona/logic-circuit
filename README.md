# logic circuit
simulation of essential combinational logic circuits with boolean algebra

# Examples

## Full Adder

```console
$ python main.py -a -n 5 11
adding 5 and 11...
    binary of  5: 0101
    binary of 11: 1011

step 1:
      0101
      1011
    +    ^
     -----
         0 (1)
    calculating sum digit:
        XOR of 1 and 1 as s1 is 0,
        XOR of s1 0 and carry-in 0 as sum digit is 0
    calculating carry-out digit:
        AND of 1 and 1 is o1 1,
        AND of s1 0 and carry-in 0 as o2 is 0,
        XOR of o1 1 and o2 0 as carry-out digit is 1
step 2:
      0101
      1011
    +   ^
     -----
        00 (1)
    calculating sum digit:
        XOR of 0 and 1 as s1 is 1,
        XOR of s1 1 and carry-in 1 as sum digit is 0
    calculating carry-out digit:
        AND of 0 and 1 is o1 0,
        AND of s1 1 and carry-in 1 as o2 is 1,
        XOR of o1 0 and o2 1 as carry-out digit is 1
step 3:
      0101
      1011
    +  ^
     -----
       000 (1)
    calculating sum digit:
        XOR of 1 and 0 as s1 is 1,
        XOR of s1 1 and carry-in 1 as sum digit is 0
    calculating carry-out digit:
        AND of 1 and 0 is o1 0,
        AND of s1 1 and carry-in 1 as o2 is 1,
        XOR of o1 0 and o2 1 as carry-out digit is 1
step 4:
      0101
      1011
    + ^
     -----
     10000 (1)
    calculating sum digit:
        XOR of 0 and 1 as s1 is 1,
        XOR of s1 1 and carry-in 1 as sum digit is 0
    calculating carry-out digit:
        AND of 0 and 1 is o1 0,
        AND of s1 1 and carry-in 1 as o2 is 1,
        XOR of o1 0 and o2 1 as carry-out digit is 1

final reslut: adding 5 and 11 in binary is 10000, converted to integer is 16
```