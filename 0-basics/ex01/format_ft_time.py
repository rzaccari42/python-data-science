import time

current_sec = time.time()             # seconds since epoch representation of the date
current = time.localtime(current_sec) # struct_time (named tuple) representation of the date

print(f"Seconds since January 1, 1970: {current_sec:,.4f} or {current_sec:.2e} in scientific notation")
print(time.strftime("%b %d %Y", current))
