d = int(input("change owed: "))
while (d < 0):
    d = int(input("change owed: "))
y = round(d * 100);
h = (y/25)
i = (y-(25 * h))
x = (i/10)
w = (i-(10 * x))
p = (w/5)
t = (w-(5 * p))
r = (t/1)
v = (h + x + p + r)
print(f"{v}")

