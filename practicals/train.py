import sys

# token counter
tokens = 0
# matrix and freq
matrix = []
tagfreq = {}

# read in the annotated .txt
with open('wiki.conllu', 'r') as text:
    for line in text:
        line = line.strip()

        # skip the #sent_id and #text lines
        if line.startswith('#'):
            continue
        row = line.split('\t')

        # token counter +1
        tokens += 1

        # word = cell 2
        word = row[1]
        # tag = cell 4
        tag = row[3]
        # form = cell 2
        form = row[1]

        # edit matrix
        matrix.append((word, tag, form))

        # count in tag freq dict
        if tag in tagfreq:
            tagfreq[tag] += 1
        else:
            tagfreq[tag] = 1

### Outputing it all ### 
# # P        count     tag        form
# 0.19        5        ADP        _
# 0.23        6        NOUN       _
# 0.04        1        AUX        _
# 0.08        2        DET        _
# Header 
print("\n# P\tcount\ttag\tform")
for tag, count in tagfreq.items():
    # ouput order [p] [count] [tag] [form]
    print(f"{count/tokens:.2f}\t{count}\t{tag}\t{form}")
