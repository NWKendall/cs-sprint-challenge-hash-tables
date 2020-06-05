def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    sets = iter(map(set, arrays))
    result = sets.next()
    for s in sets:
        result = result.intersection(s)
    return result




l = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

print(intersection(l))
"""
```python

```

And we need to compute the _intersection_, that is, numbers that exist
in all lists.

From the above input, the return value will be:

```
[1, 2]
"""
# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
