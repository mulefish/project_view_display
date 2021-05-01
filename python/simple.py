import fnmatch
import os
import json
from letters import getLetterFromNumber

pattern = "*.js"
rootPath = "../src/"
ignore = ["", ".."]

seen = {}


def step1_gatherData():
    results = []
    i = 0
    j = 0
    for root, dirs, files in os.walk(rootPath):
        # root = root.replace(os.sep, "|")
        root = root.replace(os.sep, "|")

        parent = "_{}".format(getLetterFromNumber(i))
        if parent not in seen:
            ary = root.split("|")
            seen[parent] = root
        i += 1
        for filename in fnmatch.filter(files, pattern):
            x = "{}|{}".format(root, filename)
            x = x.replace(os.sep, "|")
            x = x.replace("||", "|")
            # print("{} {}".format(l, x ))
            obj = {}
            obj["path"] = x
            obj["parent"] = parent
            obj["id"] = getLetterFromNumber(j)
            obj["angle"] = 0
            obj["x"] = 0
            obj["y"] = 0
            obj["sx"] = 0
            obj["sy"] = 0
            j += 1
            results.append(obj)

    for x in results:
        print("{},".format(x))
    # print(results)
    # for s in seen:
    #     print("{}    {} ".format(s, seen[s]))


if __name__ == "__main__":
    step1_gatherData()
