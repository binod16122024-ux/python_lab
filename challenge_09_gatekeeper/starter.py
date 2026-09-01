value = "0000"   # TODO: change this to a 4-digit code that passes every check below

if len(value) != 4:
    print("Access denied: code must be exactly 4 characters")
elif not value.isdigit():
    print("Access denied: code must be numeric")
elif int(value) % 7 != 0:
    print("Access denied: failed checksum")
elif value[0] == value[-1]:
    print("Access denied: first and last digit cannot match")
elif value[1] != value[2]:
    print("Access denied: middle two digits must match")
elif sum(int(d) for d in value) != 6:
    print("Access denied: digit sum mismatch")
else:
    print(f"FLAG{{gatekeeper_{value}}}")
