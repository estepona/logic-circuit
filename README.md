# logic circuit

Simulation of essential combinational logic circuits with boolean algebra:
- half adder
- full adder
- half subtractor
- full subtractor

Supports adding and subtracting integers >= 0

## Examples

### Half Adder
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

### Full Adder

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

### Half Subtractor
```console
$ python main.py --half-subtract --nums 0 1
Half Subtractor subtracting 0 and 1...

Operators:
    & = AND
    ^ = XOR

Equations:
    Difference = A ^ B
    Borrow-Out = (1 - A) & B

  0
  1
- ^
 --
  1 (1)
difference = 0 XOR 1 = 1
borrow-out = (1 - 0) AND 1 = 1
```

### Full Subtractor
```console
$ python main.py --full-subtract --nums 16 5
Full Subtractor subtracting 16 and 5...
    binary of 16: 10000
    binary of  5: 00101

Operators:
    & = AND
    ^ = XOR
    | = OR

Equations:
    Difference = A ^ B ^ Borrow-In
    Borrow-Out = ((1 - A) & B) | ((1 - (A ^ B)) & Borrow-In)

step 1:
      10000
      00101
    -     ^
     ------
          1 (1)
    difference = 0 ^ 1 ^ 0 = 1
    borrow-out = (1 - (0 & 1)) | ((1 - (0 ^ 1)) & 0) = 1
step 2:
      10000
      00101
    -    ^
     ------
         11 (1)
    difference = 0 ^ 0 ^ 1 = 1
    borrow-out = (1 - (0 & 0)) | ((1 - (0 ^ 0)) & 1) = 1
step 3:
      10000
      00101
    -   ^
     ------
        011 (1)
    difference = 0 ^ 1 ^ 1 = 0
    borrow-out = (1 - (0 & 1)) | ((1 - (0 ^ 1)) & 1) = 1
step 4:
      10000
      00101
    -  ^
     ------
       1011 (1)
    difference = 0 ^ 0 ^ 1 = 1
    borrow-out = (1 - (0 & 0)) | ((1 - (0 ^ 0)) & 1) = 1
step 5:
      10000
      00101
    - ^
     ------
      01011 (0)
    difference = 1 ^ 0 ^ 1 = 0
    borrow-out = (1 - (1 & 0)) | ((1 - (1 ^ 0)) & 1) = 0

final reslut: subtracting 16 and 5 in binary is 1011, converted to integer is 11
```
