# insertion sort
def a_function(arr):
    output = []

    for num in arr:
        i = 0

        while i < len(output) and output[i] < num:
            i += 1

        output.insert(i, num)

    return output

print(a_function([4, 2, 7, 1, 5]))