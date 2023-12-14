# import sys

# # read in
# Segoutput = sys.stdin.read()

# for c in Segoutput:
# 	if c in Segoutput:
# 		Newspaces = Segoutput.replace(',',' , ').replace('.',' . ').replace(';',' ; ').replace(':',' : ').replace('?',' ? ').replace('"',' " ').replace('(',' ( ').replace(')',' ) ').replace('/',' / ').replace('-',' - ')
# for b in Newspaces:
# 	if b in Newspaces:
# 		Newlines = Newspaces.replace(' ', '\n')
# counter  = 0
# for a in Newspaces:
# 	if a == '\n':
# 		counter = counter + 1
# sys.stdout.write(counter + Newlines)

import sys
#read in all text
textlines = sys.stdin.read()
# sent_id = # counter
idcounter = 1
# Read in a each line
# \n for each punct
# headers sent_id = #
# header text = "each line read in"
for line in textlines.splitlines():
    newlines = line.replace(',', '\n,').replace(':', '\n:').replace('(', '\n(').replace(')', '\n)').replace('.', '\n.')
    print("# sent_id = %d" % idcounter)
    print("# text = %s" % line.strip())
    # each line start counter
    counter = 1
    # tokeniser 
    things = newlines.split()
    for t in things:
        # print ID#, text/word, _, ...
        print("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_" % (counter, t))
        #each line counter +1
        counter += 1
    # each sent_id = #+1
    idcounter += 1
