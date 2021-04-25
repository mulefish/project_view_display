import fnmatch
import os
import json
from letters import getLetterFromNumber

pattern = "*.js"
rootPath = "../src/"
ignore = ["", ".."]


def step1_gatherData():
    results = []
    i = 0
    j = 0
    for root, dirs, files in os.walk(rootPath):
        # root = root.replace(os.sep, "|")
        familyName = "_{}".format(getLetterFromNumber(i))
        i += 1
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            x = x.replace(os.sep, "|")
            x = x.replace("||", "|")
            # print("{} {}".format(l, x ))
            obj = {}
            obj["path"] = x
            obj["familyId"] = familyName
            obj["id"] = getLetterFromNumber(j)
            obj["angle"] = 0
            obj["x"] = 0
            obj["y"] = 0
            obj["sx"] = 0
            obj["sy"] = 0
            j += 1
            results.append(obj)
        for x in results:
            print(x)
        # print(results)


if __name__ == "__main__":
    step1_gatherData()
