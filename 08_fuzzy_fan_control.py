# Fuzzy-style Fan Speed Control based on Temperature
tem = float(input("enter the temperature in C:"))

if tem < 20:
    low = 1
else:
    low = 0

if 20 <= tem <= 30:
    med = 1
else:
    med = 0

if tem > 30:
    high = 1
else:
    high = 0

if low == 1:
    fan = "slow"
elif med == 1:
    fan = "medium"
else:
    fan = "fast"

print("Temperature:", tem, "C")
print("Fan speed:", fan)

# Output:
# enter the temperature in C:100
# Temperature: 100.0 C
# Fan speed: fast
