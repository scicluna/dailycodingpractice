# Task :Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 
# for each index from the minimum value up to the maximum value (both included).

# Plan: We only really need to know first and last of the pipeList.
def pipes(pipeList):
    return list(range(pipeList[0], pipeList[-1]+1))