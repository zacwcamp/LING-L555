import sys

## '. ' period and space change to '\n' ##
# read in text
Oritext = sys.stdin.read()

# replace \n with ' '
NoOldLines = Oritext.replace('\n',' ')
NoOldLines.replace('. ','.\n')
FinalWriteOut = NoOldLines.replace('. ','.\n')

sys.stdout.write(FinalWriteOut)
