count = "7"
total = count + 3           # BUG: can't concatenate str and int like this
label = "round_" + str(total)
print(f"FLAG{{type_{label}}}")
