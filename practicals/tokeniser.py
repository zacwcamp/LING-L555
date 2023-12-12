import sys

#input
Segoutput = sys.stdin.read()
  
# replace 'punctuation' with ' '
Newlines = Segoutput.replace(',',' , ').replace('.',' . ').replace(';',' ; ').replace(':',' : ').replace('?',' ? ').replace('"',' " ').replace('(',' ( ').replace(')',' ) ').replace('/',' / ').replace('-',' - ')

#counter
counter = 1

# replace spaces with new lines
# format output
Spacetoline = Newlines.split()
for token in Spacetoline:
	print(f"{counter}\t{token}\t_\t_\t_\t_\t_\t_\t_\t_")
	counter += 1

