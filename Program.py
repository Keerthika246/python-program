def calculate_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    total = sum(scores) - lowest - highest
    average = total / 6
    return lowest, highest, total, average
    
scores = list(map(float, input().split()))

lowest, highest, total, average = calculate_scores(scores)

print(f"Lowest score: {lowest:.2f}")
print(f"Highest score: {highest:.2f}")
print(f"Total point: {total:.2f}")
print(f"Average: {average:.2f}")
