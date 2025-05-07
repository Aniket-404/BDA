#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    name, marks = line.split(",")
    print("{0}\t{1}".format(name, marks))
