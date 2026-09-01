encoded = [77, 83, 72, 78, 130, 121, 108, 106, 124, 121, 122, 112, 125, 108, 102, 115, 118, 106, 114, 132]
offset = 7

def reveal(n):
    # BUG: missing base case - this walks past the end of 'encoded' (IndexError)
    return chr(encoded[n] - offset) + reveal(n + 1)

print(reveal(0))
