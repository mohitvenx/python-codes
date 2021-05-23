#Given list of tuples, where each tuple takes pattern (name,marks) of a student, display only names.
score=[('akaash',85),('dhruv',90),('asha', 75),('aditya',95)]
name=zip(*score)      # * is used to unpack from a group
a=list(name)
print(a[0])
