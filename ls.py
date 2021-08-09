import sys,os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('path', metavar='path', type=str, help='the path to list')
parser.add_argument('-l', '--long', action='store_true', help="enable the long listing")
args=parser.parse_args()
input_path=args.path

if not os.path.isdir(input_path):
    print ('The path does not exist')
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        size=os.stat(os.path.join(input_path, line)).st_size
        line='%10d %s' % (size, line)
    print (line)
