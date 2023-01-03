"""
The only requirement for illuminating all trophies is that "RL" is a sub-string
of the lamps. If not, only the 1st and last trophies are problematic.
    - Find the first occurrence of the substring "RL" and swap the characters.
    - Check again and, if still not valid, return -1.
"""
def faster(lamps) -> int:
    i = 0
    while i + 1 < len(lamps):
        if lamps[i] == "R" and lamps[i+1] == "L":
            return 0
        i += 1

    return -1

tests = int(input())
for case in range(tests):
    trophies = int(input())
    lamps = str(input())
    # L: 1, 2, ..., i-1
    # R: i+1, i+2, ..., n
    illuminated = faster(lamps)
    if illuminated == -1:
        first_r = lamps.find("R")
        if 0 < first_r < trophies and lamps[first_r-1] == "L":
            new_lamps = "".join([lamps[:first_r-1], "R", "L", lamps[first_r+1:]])
            illuminated = first_r if faster(new_lamps) == 0 else -1

    print(illuminated)
