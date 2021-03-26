import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('infile')
parser.add_argument('outfile')
args = parser.parse_args()

with open(args.infile, 'rb') as fh:
    data = list(fh.read())

rise_time = 3 * 10
dec_time = 1 * 10

data[36] = rise_time & 0xff
data[37] = (rise_time >> 8) & 0xff

data[38] = dec_time & 0xff
data[39] = (dec_time >> 8) & 0xff

with open(args.outfile, 'wb') as fh:
    fh.write(bytes(data))
