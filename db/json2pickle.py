#!/usr/bin/env python


import cPickle as pickle
import json
import os
import sys

with open(os.path.abspath(os.path.expanduser(sys.argv[1])), 'r') \
	as ifh:
	with open(os.path.abspath(os.path.expanduser(sys.argv[2])), 'wb') \
		as ofh:
		pickle.dump(json.load(ifh), ofh, protocol=pickle.HIGHEST_PROTOCOL)
