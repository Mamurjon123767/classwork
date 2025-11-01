import random
prize = ["coumputer", "Iphone", "airpods", "book"]
collect_prize = []
for i in range(3):
    prize = random.choices(prize)
    collect_prize.append(prize)

print(f"The collected prizes are {collect_prize}")