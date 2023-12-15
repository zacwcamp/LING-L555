import sys

# dict
IPAchart = {}
#open transcriber key (made from "https://handwiki.org/wiki/Help:IPA/M%C4%81ori")
scribekey = open('transcribekey.txt','r')

## using frequency.py code 
for line in scribekey:
    # strip excess "\n"
	#split line @ tab; two variables result 
    reg, ipa = line.strip('\n').split('\t')
    # define variables to IPAchart
    IPAchart[reg] = ipa
	
# for each of the lines of input
for line in sys.stdin.readlines(): 
    # strip any excess newlines
    line = line.strip('\n')
    # if there is no tab character, skip the line
    if '\t' not in line:
        print(line)
        continue
    #if tab, alter row/line
    if '\t' in line:
    # make a list of the cells in the row
        row = line.split('\t')
    # form is the value of the second cell
        # define form
        transcribe = form = row[1]
 ### the form is the value of the second cell
# ##    form = row[1]
# ##    # if we haven't seen it yet, set the frequency count to 0
# ##    if form not in IPAchart:
# ##        IPAchart[form] = 0
# ##    IPAchart[form] = IPAchart[form] + 1
    # change form to IPA form
        for letter in IPAchart:
            #add redefine form for output
            new = form.replace(letter, IPAchart[letter])
    # slot 10 is "row[9]"
        row[9] = 'IPA: ' + new
        # print with new slot and join
        print('\t'.join(row))
        
    ## from freq.py - change to insert transribe
    # form to IPA form
    # if form not in IPAchart:
    #     IPAchart[form] = 0
    # IPAchart[form] = IPAchart[form] + 1




########################################### BEGIN TRASH BIN  ###########################################
	 # skip "no tab" lines
#     if '\t' not in line:
#         #print the line
#         print(line)
#         continue 
#     #list cells in row
#     row = line.split('\t') !!!
#     #skip non 10-cell rows!!!
#     if len(row) != 10:!!
#         continue!!
#     # form = second cell
#     form = row[1]!!!
    # if '\t' in line:
    #     #strip line
    #     line = line.strip('\n')
    #     (f, w) = line.split('\t')
    #     #print it
    #     print()
# ###### rank.py code #########
#    # For each of the lines in the file
# for line in fd.readlines():
#     # Strip the newline
#     line = line.strip('\n')
#     # Split the line on the tab character and put the 
#     # resulting two values in a tuple
#     (f, w) = line.split('\t')
#     # Append the tuple to the list
#     freq.append((int(f), w))
########### end rank.py code ##########
#########   frequency.py code   ########
# import sys

# IPAchart = {} # dict to store frequency list

# # for each of the lines of input
# for line in sys.stdin.readlines(): 
#     # strip any excess newlines
#     line = line.strip('\n')
#     # if there is no tab character, skip the line
#     if '\t' not in line:
#         print(line)
#         continue
#     # make a list of the cells in the row
#     row = line.split('\t')
#     # if there are not 10 cells, skip the line
#     if len(row) != 10:
#         continue
#     # the form is the value of the second cell
#     form = row[1]
#     # if we haven't seen it yet, set the frequency count to 0
#     if form not in IPAchart:
#         IPAchart[form] = 0
#     IPAchart[form] = IPAchart[form] + 1

# # print out the frequency list
# for w in vocab:
#     print('%d\t%s' % (vocab[w], w))
######## END frequency.py code    #########