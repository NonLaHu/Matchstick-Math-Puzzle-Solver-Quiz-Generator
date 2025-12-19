import json
#   a
# f   b
#   g
# e   c
#   d

# ---------------------------------------
# Matchstick digit definitions (7-segment)
# ---------------------------------------
digits = {
    0: {"a", "b", "c", "d", "e", "f"},
    1: {"b", "c"},
    2: {"a", "b", "g", "e", "d"},
    3: {"a", "b", "c", "d", "g"},
    4: {"f", "g", "b", "c"},
    5: {"a", "f", "g", "c", "d"},
    6: {"a", "f", "e", "d", "c", "g"},
    7: {"a", "b", "c"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}

segment_to_digit = {
    frozenset(v): k for k, v in digits.items()
}

# ---------------------------------------
# Generate one-stick problems
# ---------------------------------------

def generate_one_stick_moves():
    all_segments = {"a", "b", "c", "d", "e", "f", "g"}
    results = []

    for digit, segs in digits.items():

        # TYPE 0: move one stick (remove + add)
        for removed in segs:
            for added in all_segments - segs:
                new_segs = (segs - {removed}) | {added}
                fs = frozenset(new_segs)

                if fs in segment_to_digit:
                    new_digit = segment_to_digit[fs]
                    if new_digit != digit:
                        results.append({
                            "type": 0,
                            "from": digit,
                            "to": new_digit,
                            "remove": removed,
                            "add": added
                        })

        # TYPE 1: remove one stick only
        for removed in segs:
            new_segs = segs - {removed}
            fs = frozenset(new_segs)

            if fs in segment_to_digit:
                new_digit = segment_to_digit[fs]
                if new_digit != digit:
                    results.append({
                        "type": 1,
                        "from": digit,
                        "to": new_digit,
                        "remove": removed,
                        "add": None
                    })

        # TYPE 2: add one stick only
        for added in all_segments - segs:
            new_segs = segs | {added}
            fs = frozenset(new_segs)

            if fs in segment_to_digit:
                new_digit = segment_to_digit[fs]
                if new_digit != digit:
                    results.append({
                        "type": 2,
                        "from": digit,
                        "to": new_digit,
                        "remove": None,
                        "add": added
                    })

    return results

# ---------------------------------------
# MAIN
# ---------------------------------------

if __name__ == "__main__":
    moves = generate_one_stick_moves()

    grouped = {0: [], 1: [], 2: []}
    for m in moves:
        grouped[m["type"]].append(m)

    print(f"Type 0 moves: {len(grouped[0])} entries")
    print(f"Type 1 removes: {len(grouped[1])} entries")
    print(f"Type 2 adds: {len(grouped[2])} entries")
    
    with open("matchstick_moves.json", "w") as f:
        json.dump(grouped, f)


