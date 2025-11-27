n = int(input("Enter number of processes: "))

bt = []
at = []
pr = []

for i in range(n):
    b, a, p = map(int, input(f"P{i+1} (burst arrival priority): ").split())
    bt.append(b)
    at.append(a)
    pr.append(p)

ct = [0] * n
tat = [0] * n
wt = [0] * n
done = [0] * n

t = 0

for _ in range(n):
    avail = [i for i in range(n) if not done[i] and at[i] <= t]

    if not avail:
        t = min(at[i] for i in range(n) if not done[i])
        avail = [i for i in range(n) if at[i] <= t and not done[i]]

    i = min(avail, key=lambda x: pr[x])
    t += bt[i]
    ct[i] = t
    done[i] = 1

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nP\tBT\tAT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t{at[i]}\t{pr[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("\nAvg TAT =", round(sum(tat)/n, 2), " Avg WT =", round(sum(wt)/n, 2))
