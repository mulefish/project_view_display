import fnmatch
import os
import json
from letters import getLetterFromNumber

pattern = "*.js"
rootPath = "../src/"
ignore = ["", ".."]


def step1_gatherData():
    step1 = []
    i = 0
    for root, dirs, files in os.walk(rootPath):
        # root = root.replace(os.sep, "|")
        for filename in fnmatch.filter(files, pattern):
            x = "{} -------- {}".format(root, filename)
            print(x)


if __name__ == "__main__":
    step1_gatherData()
