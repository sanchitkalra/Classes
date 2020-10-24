def countVarious(string):
    count = {} # using a dict to store counts for all types of characters
    for k in string: # for ASCII values refer table at end of file
        if (ord(k) <= 47) or (ord(k) >= 58 and ord(k) <= 64) or (ord(k) >= 91 and ord(k) <= 96) or (ord(k) >= 123 and ord(k) <= 127):
            count["special"] = count.get("special", 0) + 1
        elif (k in "AEIOU") or (k in "aeiou"):
            count["vowels"] = count.get("vowels", 0) + 1
        elif k in "0123456789":
            count["digits"] = count.get("digits", 0) + 1
        else:
            count["consonants"] = count.get("consonants", 0) + 1
    return count

print(countVarious("kjasdkjahs8721683@#$$%BAJBJK    DB"))

'''

The ASCII values, in decimal.

     +-------+-------+-------+-------+-------+-------+-------+-------+
     |  0 NUL|  1 SOH|  2 STX|  3 ETX|  4 EOT|  5 ENQ|  6 ACK|  7 BEL|
     |  8 BS |  9 HT | 10 NL | 11 VT | 12 NP | 13 CR | 14 SO | 15 SI |
     | 16 DLE| 17 DC1| 18 DC2| 19 DC3| 20 DC4| 21 NAK| 22 SYN| 23 ETB|
     | 24 CAN| 25 EM | 26 SUB| 27 ESC| 28 FS | 29 GS | 30 RS | 31 US |
     | 32 SP | 33  ! | 34  " | 35  # | 36  $ | 37  % | 38  & | 39  ' |
     | 40  ( | 41  ) | 42  * | 43  + | 44  , | 45  - | 46  . | 47  / |
     | 48  0 | 49  1 | 50  2 | 51  3 | 52  4 | 53  5 | 54  6 | 55  7 |
     | 56  8 | 57  9 | 58  : | 59  ; | 60  < | 61  = | 62  > | 63  ? |
     | 64  @ | 65  A | 66  B | 67  C | 68  D | 69  E | 70  F | 71  G |
     | 72  H | 73  I | 74  J | 75  K | 76  L | 77  M | 78  N | 79  O |
     | 80  P | 81  Q | 82  R | 83  S | 84  T | 85  U | 86  V | 87  W |
     | 88  X | 89  Y | 90  Z | 91  [ | 92  \ | 93  ] | 94  ^ | 95  _ |
     | 96  ` | 97  a | 98  b | 99  c |100  d |101  e |102  f |103  g |
     |104  h |105  i |106  j |107  k |108  l |109  m |110  n |111  o |
     |112  p |113  q |114  r |115  s |116  t |117  u |118  v |119  w |
     |120  x |121  y |122  z |123  { |124  | |125  } |126  ~ |127 DEL|
     +-------+-------+-------+-------+-------+-------+-------+-------+

Source: https://cs.nyu.edu/courses/spring99/A22.0002.002/lecture_notes/lecture5/node16.html#:~:text=The%20ASCII%20table%20assigns%20an,is%20higher%20than%20its%20predecssor.

'''