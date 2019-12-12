#!/usr/bin/python3
import sys
from computer import computer

if __name__ == "__main__":
	c = computer()
	c.load(sys.argv[1])
	c.showStatus()
	c.execute()
