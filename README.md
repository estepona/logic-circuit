# logic circuit
simulation of essential combinational logic circuits with boolean algebra

# Examples

## Half Adder
```console
$ python main.py --half-add --nums 1 1
Half Adder adding 1 and 1...

Operators:
    & = AND
    ^ = XOR

Equations:
    Sum = A ^ B
    Carry-Out = A & B

  1
  1
+ ^
 --
  0 (1)
sum       = 1 XOR 1 = 0
carry-out = 1 AND 1 = 1
```

## Full Adder

```console
$ python main.py --full-add --nums 5 11
Full Adder adding 5 and 11...
    binary of  5: 0101
    binary of 11: 1011

Operators:
    & = AND
    ^ = XOR
    | = OR

Equations:
    Sum = A ^ B ^ Carry-In
    Carry-Out = (A & B) | ((A ^ B) & Carry-In)

step 1:
      0101
      1011
    +    ^
     -----
         0 (1)
    sum       = 1 ^ 1 ^ 0 = 0
    carry-out = (1 & 1) | ((1 ^ 1) & 0) = 1
step 2:
      0101
      1011
    +   ^
     -----
        00 (1)
    sum       = 0 ^ 1 ^ 1 = 0
    carry-out = (0 & 1) | ((0 ^ 1) & 1) = 1
step 3:
      0101
      1011
    +  ^
     -----
       000 (1)
    sum       = 1 ^ 0 ^ 1 = 0
    carry-out = (1 & 0) | ((1 ^ 0) & 1) = 1
step 4:
      0101
      1011
    + ^
     -----
     10000 (1)
    sum       = 0 ^ 1 ^ 1 = 0
    carry-out = (0 & 1) | ((0 ^ 1) & 1) = 1

final reslut: adding 5 and 11 in binary is 10000, converted to integer is 16
```