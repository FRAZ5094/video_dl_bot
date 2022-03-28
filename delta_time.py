from datetime import datetime
from dateutil import parser
import sys

string=sys.argv[1]

now=datetime.now()

date = parser.parse(string)

delta=now-date

print(int(delta.total_seconds()))
