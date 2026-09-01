target_sum = 55
total = 0

for i in range(1, 10):      # BUG: doesn't reach the intended sum
    total += i

if total == target_sum:
    print(f"FLAG{{loop_sum_{total}}}")
else:
    print(f"Sum was {total}, expected {target_sum}. Try again.")
