import sys

## '. ' period and space change to '\n' ##
Oritext = sys.stdin.read()

Oritext.replace('. ','.\n')

sys.stdout.write(Oritext)
