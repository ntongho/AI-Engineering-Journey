scores = [45, 72, 88, 34, 91, 67, 50, 83]

# Using list comprehension
new_score = [score * 2 for score in scores if score >= 70]
print(new_score)



# Using filter + map
big_scores_filtered = filter(lambda score: score >= 70, scores)
result = list(big_scores_filtered)

big_scores_filtered_and_multiplied = map(lambda score: score*2 ,result)
print(list(big_scores_filtered_and_multiplied))