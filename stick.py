#   a
# f   b
#   g
# e   c
#   d
import json

# Load matchstick moves once
with open("matchstick_moves.json") as f:
    grouped = json.load(f)

def valid_equation(a, b, c):
    return a + b == c

def apply_move(digit, move):
    """Apply a move dict on a digit and get the new digit if move is valid."""
    if move["from"] == digit:
        return move["to"]
    return None

def check_type0_fix(i, j, z):
    # Try moving one stick on i, j, or z and see if equation fixes
    fixes = []
    for move in grouped["0"]:
        # Try changing i
        new_i = apply_move(i, move)
        if new_i is not None and valid_equation(new_i, j, z):
            fixes.append((f"Change i from {i} to {new_i} by moving {move['remove']}→{move['add']}"))
        # Try changing j
        new_j = apply_move(j, move)
        if new_j is not None and valid_equation(i, new_j, z):
            fixes.append((f"Change j from {j} to {new_j} by moving {move['remove']}→{move['add']}"))
        # Try changing z
        new_z = apply_move(z, move)
        if new_z is not None and valid_equation(i, j, new_z):
            fixes.append((f"Change z from {z} to {new_z} by moving {move['remove']}→{move['add']}"))
    return fixes

def check_type1_2_fix(i, j, z):
    fixes = []
    for move1 in grouped["1"]:  # remove moves
        for move2 in grouped["2"]:  # add moves
            # i remove, j add
            new_i = apply_move(i, move1)
            new_j = apply_move(j, move2)
            if new_i is not None and new_j is not None and valid_equation(new_i, new_j, z):
                fixes.append(f"Remove {move1['remove']} from i, Add {move2['add']} to j, equation fixed")
            
            # i remove, z add
            new_z = apply_move(z, move2)
            if new_i is not None and new_z is not None and valid_equation(new_i, j, new_z):
                fixes.append(f"Remove {move1['remove']} from i, Add {move2['add']} to z, equation fixed")
            
            # j remove, z add
            new_j2 = apply_move(j, move1)
            if new_j2 is not None and new_z is not None and valid_equation(i, new_j2, new_z):
                fixes.append(f"Remove {move1['remove']} from j, Add {move2['add']} to z, equation fixed")
            
            # j remove, i add
            new_i2 = apply_move(i, move2)
            if new_j2 is not None and new_i2 is not None and valid_equation(new_i2, new_j2, z):
                fixes.append(f"Remove {move1['remove']} from j, Add {move2['add']} to i, equation fixed")
            
            # z remove, i add
            new_z2 = apply_move(z, move1)
            if new_z2 is not None and new_i2 is not None and valid_equation(new_i2, j, new_z2):
                fixes.append(f"Remove {move1['remove']} from z, Add {move2['add']} to i, equation fixed")
            
            # z remove, j add
            new_j3 = apply_move(j, move2)
            if new_z2 is not None and new_j3 is not None and valid_equation(i, new_j3, new_z2):
                fixes.append(f"Remove {move1['remove']} from z, Add {move2['add']} to j, equation fixed")

    return fixes

# Main loop
with open("math_quiz_output.txt", "w", encoding="utf-8") as f:
    for i in range(10):
        for j in range(10):
            for z in range(10):
                if valid_equation(i, j, z):
                    continue  # Already true, skip

                fixes0 = check_type0_fix(i, j, z)
                fixes12 = check_type1_2_fix(i, j, z)

                if fixes0 or fixes12:
                    line = f"Equation: {i} + {j} = {z}\n"
                    print(line, end="")
                    f.write(line)

                    if fixes0:
                        line = " Fixes by moving one stick (type 0):\n"
                        print(line, end="")
                        f.write(line)
                        for fix in fixes0:
                            line = f"  {fix}\n"
                            print(line, end="")
                            f.write(line)

                    if fixes12:
                        line = " Fixes by removing & adding sticks (type 1 & 2):\n"
                        print(line, end="")
                        f.write(line)
                        for fix in fixes12:
                            line = f"  {fix}\n"
                            print(line, end="")
                            f.write(line)

                    print()
                    f.write("\n")
