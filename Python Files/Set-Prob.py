def intersection(set1, set2):
  differentValues = set()

  # Add Code to only add values that are not in both sets to the differentValues
  #   Hint: One need only cycle a value and check if it is in the other set

  return(differentValues)

def union(set1, set2):
  unionOfSets = set()

  # Add code to add both the values from set1 and set2 to the unionOfSets

  return(unionOfSets)

#############################################################################
# Problems to solve
#############################################################################

s1 = {1,3,5}
s2 = {1,2,3,4,5}
print(intersection(s1,s2))  # Should show {1, 3, 5}
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5}

s1 = {1,2,3,100}
s2 = {6,7,8,100}
print(intersection(s1,s2))  # Should show {100}
print(union(s1,s2)) # Should show {1, 2, 3, 100, 6, 7, 8}