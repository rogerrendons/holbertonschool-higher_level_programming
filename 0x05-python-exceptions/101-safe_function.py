#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    
    try:
        return fct(*args)
    except Exception as ddd:
        print("Exception:", ddd, file=sys.stderr)
