def compute_flag():
    parts = ["FLAG{", "silent", "_", "catch", "}"]
    total = 0
    for i in range(len(parts) + 1):   # BUG: goes one index too far
        total += len(parts[i])
    return "".join(parts)

try:
    result = compute_flag()
except Exception:
    pass   # BUG: this hides the real error - remove it to see what's wrong

print(result)
