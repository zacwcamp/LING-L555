import sys
# import string functions
import string

Punct = ['.', ',', ':', ';', '?', '!', '-', '/']

Segout = sys.stdin.read()
for c in Segout:
	if c in Punct:
		Newspaces = Segout.sub(Punct,' ' + Punct + ' ')
		print(Newspaces)




# read in text
# Segoutput = sys.stdin.read()
# for p in Segoutput:
#	if p in string.punctuation:
#		Nopunct = Segoutput.replace(p, ' ')
# sys.stdout.write(Nopunct)

## print it all out
## sys.stdout.write(Spacetoline)



