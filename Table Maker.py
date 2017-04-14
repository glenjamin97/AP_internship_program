import os #for debugging current filepath
from prettytable import PrettyTable

f = open('ap_input_file.txt','r') #opens file


def get_full_header(line): #finds the header of the line
    x = line.rfind(':')
    return line[1:x];
def get_sub_header(line):
    x = line.find(':')
    return line[1:x];
def getdata(line): #gets the data from the line
    x = line.rfind(':')
    return line[(x+1):];
def getnamedata(line): #had to make a few of these in order to extract the info correctly (curse you colons!)
    x = line.find(':')
    return line[(x+1):];

ql_list = []
av_list = []
type_list = []

def list_setup(): #finds important items in datafile and extracts info into lists
    av = 0
    n = 0
    for line in f:
        subheader = get_sub_header(line)
        fullheader = get_full_header(line)
        if subheader == "name":
            ql_list.append(getnamedata(line))
            n += 1
        if fullheader == "answer_names" or fullheader == "additionaldata:result":
            av_list.append(getdata(line))
            av += 1
        if subheader == "type":
            type_list.append(getdata(line));
        if n > av:
            av_list.append('  ')
            av += 1


table = PrettyTable()

list_setup()

table.add_column("Question Label", ql_list)
table.add_column("Answer Value", av_list)
table.add_column("Type", type_list)
table.align = 'l'
print(table)

f.close()

#print(ql_list)
#print(av_list)
#print(type_list)
