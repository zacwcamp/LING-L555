import sys

#input
Segoutput = sys.stdin.read()
  
# replace 'punctuation' with ' '
Newlines = Segoutput.replace(',',' , ').replace('.',' . ').replace(';',' ; ').replace(':',' : ').replace('?',' ? ').replace('"',' " ').replace('(',' ( ').replace(')',' ) ').replace('/',' / ').replace('-',' - ')

#counter add here
#test replacements
#print(Newlines)

# replace spaces with new lines
Spacetoline = Newlines.replace(' ','\n')

#print it all out
sys.stdout.write(Spacetoline)

