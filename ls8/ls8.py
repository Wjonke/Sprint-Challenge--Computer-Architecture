#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# NORMAL state of affairs is this line
# filename = sys.argv[1]

# BUT we want to debug, so we have to hard set it.

filename = "C:\\Users\\wjonk\\PycharmProjects\\Sprint-Challenge--Computer-Architecture\\sctest.ls8"

print("\n\n")
cpu = CPU()
cpu.load(filename)
cpu.run()

