"""
Construct array:
    1. Each element is an integer different from 0.
    2. sum(adjacent elements) = sum(array)
        S[i] + S[i+1] == S[1] + S[2] + ... + S[n]
"""

def find_array(length: int):
    if length % 2 == 0:
        proof = [1+(i%2)*(-2) for i in range(1, length+1)]
        return proof, "YES"
    elif length > 3:
        proof = [-(int(length/2))+(i%2)*(int(length/2)*2-1) for i in range(1, length+1)]
        return proof, "YES"
    
    return None, "NO"


tests = int(input())
for case in range(tests):
    result, str_res = find_array(int(input()))
    print(str_res)
    if result:
        print(" ".join(str(item) for item in result))

