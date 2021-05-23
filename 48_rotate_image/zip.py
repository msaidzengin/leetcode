name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]
  
# using zip() to map values
mapped = zip(name, roll_no, marks)
  
# converting values to print as set
mapped = set(mapped)
print(mapped)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(set(zip(*matrix)))
