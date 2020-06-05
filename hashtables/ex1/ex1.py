def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    list_of_weights = {}
    answer = []
    # compliment_index = None
    for w in range(length):
        result = limit - weights[w]
        if result in list_of_weights.keys():
            second_index = weights.index(result)
            if w != second_index:
                return [w, second_index]

        list_of_weights.update({weights[w]: w})
    

# https://levelup.gitconnected.com/two-sum-interview-problem-in-python-c1d84b029d35
l = [ 4, 6, 10, 15, 16 ]

print(get_indices_of_item_weights(l, 5, 21))
# weights list of ints
# lenth is number of weights in length
# limit is target
# use a dict to store values
    # array of values

"""
Example:
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""