num_score  = int(input())


arr1_score = list(map(int, input().split()))

max_score = max(arr1_score)

adjusted_scores = [(score / max_score) * 100 for score in arr1_score]
new_average = sum(adjusted_scores) / len(adjusted_scores)

print(new_average)