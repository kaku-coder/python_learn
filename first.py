a = [1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7]

map = {} #this is dictionary  but work like js map 

for i in a:
  if i in map.keys():
    map[i]+=1
  else:
    map[i]=1

  print(map)