#!/usr/local/bin/python3 

import sys

print(sys.argv[1:])

infile = sys.argv[1]
outfile = infile + ".out"

f = open(infile,'r')
out=open(outfile,'w')

res_list = []
index=0
for line in f.readlines():
    index=index+1
    if line in res_list:
        print('{0} line duplication: {1}'.format(index, line))
    else:
        out.write(line)
        res_list.append(line)
