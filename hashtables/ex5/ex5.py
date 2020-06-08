# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    # q_dict = {}
    result = []
    # for f in files:
    #     dictionary[f] = f.split("/")
    #     print(dictionary[f])

    # for q in queries:
    #     q_dict[q] = q
    #     print(q_dict[q])
    #     for f in dictionary:
    #         print(f)
    #         if q_dict[q] in dictionary[f]:
    #             print("q", q)

    #             print("FIRE!", f)
    #             result.append(f)

    for f in files:
        dictionary[f.split("/")[-1]] = f


    for q in queries:
        print("1", q)
        if q in dictionary:
            print("2", dictionary[q])
            result.append(dictionary[q])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/fooo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo", 
        "qux",
        "baz"
    ]
    print(finder(files, queries))


# declare dict to store files
# iterate through files
# return array of strings with file name



#  queries += [
#             "file3490",
#             "file256",
#             "file999999",
#             "file8192"
#         ]

#         result = finder(files, queries)
#         result.sort()

#         self.assertTrue(result == ['/dir256/dirb256/file256',
#             '/dir256/file256', '/dir3490/dirb3490/file3490',
#             '/dir3490/file3490', '/dir8192/dirb8192/file8192',
#             '/dir8192/file8192'])
