'''
Intro
These arrays are too long! Let's reduce them!

Description
Write a function that takes in an array of integers from 0-9, and returns a new array:

Numbers with no identical numbers preceding or following it returns a 1: 2, 4, 9  => 1, 1, 1
Sequential groups of identical numbers return their count: 6, 6, 6, 6 => 4
'''

def analyze_array(arr):
    result = []
    count = 1

    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1 or arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
            result.append(1)
        elif arr[i] == arr[i - 1]:
            count += 1
        else:
            result.append(count)
            count = 1

    if count > 1:
        result.append(count)

    return result
