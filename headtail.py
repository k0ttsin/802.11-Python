import argparse
import random

parser=argparse.ArgumentParser()
parser.add_argument('-a', action='store', choices=['head','tail'], help="Set head or tail")
options=parser.parse_args()

ranint=random.randint(1,20)
if (ranint%2)==0:
    answer="head"
else:
    answer="tail"
print ("Your Answer\t:",options.a)
print ("Computer Answer\t:",answer)
if answer==options.a:
    print ("Correct")
else:
    print ("INCorrect")
