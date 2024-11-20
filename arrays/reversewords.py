# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained
def reverse(string):
    reversed = []
    for word in string.split(" "):
        reversed.append(word[::-1])
    return " ".join(reversed)