'''
We need to remove all elements from list y in list x and print it
'''

x = ['a', 'b', 'c', 'd', 't', 'y', 's']
y = ['c', 't', 's']

print('Given list is: ' + str(x))
print('Filter list is: ' + str(y) + '\n')

for i in x:
  for j in y:
    if i == j:
      print(f'removing {i}')
#      print('Removing ' + i + ' from the list')
      x.remove(i)

print('\nResulting list is: ' + str(x))
