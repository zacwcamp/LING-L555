import sys

# read in
Segoutput = sys.stdin.read()

for c in Segoutput:
	if c in Segoutput:
		Newspaces = Segoutput.replace(',',' , ').replace('.',' . ').replace(';',' ; ').replace(':',' : ').replace('?',' ? ').replace('"',' " ').replace('(',' ( ').replace(')',' ) ').replace('/',' / ').replace('-',' - ')
for b in Newspaces:
	if b in Newspaces:
		Newlines = Newspaces.replace(' ', '\n')
counter  = 0
for a in Newspaces:
	if a == '\n':
		counter = counter + 1
sys.stdout.write(counter + Newlines)
