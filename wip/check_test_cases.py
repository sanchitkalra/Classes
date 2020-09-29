# This is an automated tool to check multiple test cases at once
# Use --help for more information on how to use the script or the README.md in the parent folder
# This tool is built on argparse, a Python standard library and requires no separate installation

import argparse
import sys

parser = argparse.ArgumentParser()

# parser.add_argument("--script", help = "Mandatory argument, add your script to test here", required = True)
# parser.add_argument("--time", help = "Print the time taken for each test case to execute", action = "store_true")
# parser.add_argument("--test_cases", help = "Add custom test cases in the form of an array", type = list)

parser.parse_args()

script = open("patterns_2_isoceles_star.py")
a_script = script.read()
sys.argv = ["patterns_2_isoceles_star.py", 1, 2, 3, 4]

exec(a_script)

script.close()