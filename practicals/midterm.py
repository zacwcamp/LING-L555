import sys
  
x = ['NOUN', 'VERB', 'ADJ', 'ADV', 'ADP']
y = ['cat', 'biscuit', 'run', 'at', 'through']

print('\t' + '\t'.join(x))
for yy in y:
	print(yy, end='\t')
	for xx in x:
     	print('_',end='\t')
print()

