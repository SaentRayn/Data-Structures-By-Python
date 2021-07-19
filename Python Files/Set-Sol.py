def intersection(set1, set2):
  differentValues = set()
  
  # Solution
  for number in set1:
    if number in set2:
      differentValues.add(number)

  return(differentValues)

def union(set1, set2):
  unionOfSets = set()
  
  # Solution
  for valueFrom1 in set1:
    unionOfSets.add(valueFrom1)
  for valueFrom2 in set2:
    unionOfSets.add(valueFrom2)
  
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
print(intersection(s1,s2))  # Should show {100}7
print("Before Sort: ")
print(union(s1,s2)) # Should show {1, 2, 3, 100, 6, 7, 8}
print("After Sort: ")
print(sorted(union(s1,s2)))