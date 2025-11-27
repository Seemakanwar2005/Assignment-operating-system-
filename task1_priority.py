n = int(input("n: "))
bt, at = [], []

for i in range(n):
    b, a = map(int, input().split())
    bt.append(b)
    at.append(a)

q = int(input("q: "))

r = bt[:]
t = 0
ct = [0] * n
Q = []

while True:
    for i in range(n):
        if at[i] <= t and r[i] > 0 and i not in Q:
            Q.append(i)

    if not Q:
        if all(x == 0 for x in r):
            break
        t += 1
        continue

    i = Q.pop(0)
    x = min(q, r[i])
    r[i] -= x
    t += x

    for j in range(n):
        if at[j] <= t and r[j] > 0 and j not in Q:
            Q.append(j)

    if r[i] > 0:
        Q.append(i)
    else:
        ct[i] = t

tat = [ct[i] - at[i] for i in range(n)]
wt = [tat[i] - bt[i] for i in range(n)]

print("P\tCT\tTAT\tWT")
for i in range(n):
    print(f"{i+1}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("Avg TAT =", round(sum(tat)/n, 2), " Avg WT =", round(sum(wt)/n, 2))
