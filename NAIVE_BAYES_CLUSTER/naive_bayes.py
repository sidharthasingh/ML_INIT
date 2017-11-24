#!/usr/bin/python

import json
from pprint import pprint

def take_input(file_path):
	inp = json.load(open(file_path))
	return inp

print(take_input("data.json")['maps']);
