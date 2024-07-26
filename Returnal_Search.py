#4.1
def sum_list(list):
  if list== []:
    return 0
  return list[0]+sum(list[1:])
   

#4.2
def list_count(list):
  if list==[]:
    return 0
  return 1+ list_count(list[1:])


#4.3
def max_list(list):
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  sub_max=max(list[1:])
  return list[0] if list[0] > sub_max else sub_max

#4.4