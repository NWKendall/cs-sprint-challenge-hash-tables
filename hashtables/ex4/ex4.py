def has_negatives(array):
    """
    YOUR CODE HERE
    """
    # Your code here
    tally = {}
    answers = []
    for num in array:
        if abs(num) in tally:
            tally[abs(num)] += 1
            if tally[abs(num)] > 1:
                answers.append(abs(num))
        else:
            tally[abs(num)] = 1
        
    return answers


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    # [1, 2, 4]


# UPER
# declare dict
# iterate over array
# store vals in dict