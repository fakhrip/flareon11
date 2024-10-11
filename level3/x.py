import re

yara = open("aray.yara", "r").read().splitlines()

test = ""
for x in yara:
    if ("uint8" in x) or ("uint32" in x):
        test += x + "\n"

# matches = re.findall(r'uint8\((\d+)\)', test)
# print(sorted(set([int(m) for m in matches])))

print(
    """
from z3 import *
from cvc5.pythonic import *

# Define filesize as a constant value of 85
filesize = 85

# Create symbolic variables for each byte value
"""
)

for x in range(85):
    print(f"uint8_{x} = BitVec('uint8_{x}', 8)")

for x in test.split("\n")[:-1]:
    if "uint32" in x:
        index = int(re.findall(r"uint32\((\d+)\)", x)[0])
        print(
            f"uint32_{index} = Concat(uint8_{index + 3}, uint8_{index + 2}, uint8_{index + 1}, uint8_{index})"
        )

print(
    """
# Create solver instance
solver = Solver()

# coming from hash brute result
solver.add(uint8_8 == 114)
solver.add(uint8_9 == 101)
solver.add(uint8_34 == 101)
solver.add(uint8_35 == 65)
solver.add(uint8_63 == 110)
solver.add(uint8_64 == 46)
solver.add(uint8_78 == 110)
solver.add(uint8_79 == 58)
solver.add(uint8_14 == 32)
solver.add(uint8_15 == 115)
solver.add(uint8_56 == 102)
solver.add(uint8_57 == 108)
solver.add(uint8_0 == 114)
solver.add(uint8_1 == 117)
solver.add(uint8_76 == 105)
solver.add(uint8_77 == 111)
solver.add(uint8_50 == 51)
solver.add(uint8_51 == 65)
solver.add(uint8_32 == 117)
solver.add(uint8_33 == 108)

# Add the conditions to the solver
"""
)

for x in test.split("\n")[:-1]:
    try:
        if (
            ("uint8" in x)
            and (
                int(re.findall(r"uint8\((\d+)\)", x)[0])
                not in [
                    0,
                    1,
                    8,
                    9,
                    14,
                    15,
                    32,
                    33,
                    34,
                    35,
                    50,
                    51,
                    56,
                    57,
                    63,
                    64,
                    76,
                    77,
                    78,
                    79,
                ]
            )
            # and int(re.findall(r"uint8\((\d+)\)", x)[0]) in [4]
        ):
            pattern = r"uint8\((\d+)\)"
            replace = r"uint8_\1"
            op1, op2 = re.findall(r"(.+)\s+(.+\s+\d+) and", x)[0]
            op1 = re.sub(pattern, replace, op1)

            if ("<" in op2) and len(op1) <= len(" uint8_XX"):
                continue

            print(f"solver.add(({op1}) {op2})")
        if "uint32" in x:
            pattern = r"uint32\((\d+)\)"
            replace = r"uint32_\1"
            op1, op2 = re.findall(r"(.+)\s+(.+\s+\d+) and", x)[0]
            print(f"solver.add(({re.sub(pattern, replace, op1)}) {op2})")
    except:  # hardcode the last bit
        print(f"solver.add(( uint8_8) > 3)")

print(
    """

# Check for satisfiability and print results
if solver.check() == sat:
    model = solver.model()
"""
)

for x in range(85):
    print(f'    print(f"{{chr(int(model[uint8_{x}].as_long()))}}", end = "")')

print(
    """
else:
    print("No solution exists that satisfies all conditions.")
"""
)
