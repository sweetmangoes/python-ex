# Recursive exercises 

def sum(list):
  if list == []:
      return 0
  return list[0] + sum(list[1:])

# print (sum([])) # 0
# print (sum([2,4,6])) # 12

# counting the number of items in a list

def count(list):
  if list == []:
    return 0
  return 1 + count(list[1:])

# print (count([])) # 0
# print (count([2,4,6])) #3

# find the max number

def max(list):
   if len(list) ==1:
      return list[0]
   if len(list) == 2:
      return list[0] if list[0] > list[1] else list[1]
   sub_max = max(list[1:])
   return list[0] if list[0] > sub_max else sub_max

print (max([1,5])) # 5
print (max([2,4,6])) #6