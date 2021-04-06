from letters import getLetterFromNumber

import fnmatch
import os

pattern = '*.js'
rootPath = '.'


def getSpecialPathMark(string_to_check):
    marker = ""

    if r"_\common\constants" in string_to_check:
        marker = 1
    elif r"_\common\util" in string_to_check:
        marker = 1

    return marker


def makeStringDotMarkupSafe(s):
    x = s.replace(".", "_")  # Ironic that a lang called 'Dot' does not like .
    x = x.replace("-", "_")
    # I am on a windows machine - linux
    x = x.replace("/", os.sep)

    return x


def readFS_makeDotGraph(show_both_files_and_dirs):
    leafnodes = {}
    edges = []
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            x = root
            x = makeStringDotMarkupSafe(x)
            mark = getSpecialPathMark(x)
            tmp = x.split(os.sep)
            ary = []
            i = 0
            for item in tmp:
                i += 1
                if i > 2:
                    item += str(mark)
                ary.append(item)

            # filename = "{}_{}".format(
            #     ary[-1], makeStringDotMarkupSafe(filename))
            # ary.append(filename)
            # leafnodes[filename] = "finch"
            filename = filename.replace(".js", "")
            filename = makeStringDotMarkupSafe(filename)
            fullname = "{}_{}".format(
                ary[-1], filename)
            ary.append(fullname)
            leafnodes[fullname] = filename

            for i in range(1, len(ary)):
                j = i - 1
                a = ary[j]
                b = ary[i]
                edge = "{} -> {}".format(a, b)
                if edge not in edges:
                    edges.append(edge)
                    # print(edge)
        if show_both_files_and_dirs == False:
            leafnodes = {}
    return edges, leafnodes


def emitDotGraph(edges, leafnodes):
    print("""digraph D {
    rankdir = LR
    node [shape=plaintext fontname="Sans serif" fontsize="8"]
    node[color="black", shape="rectangle", overlap=false]""")
    for x in edges:
        print(x)
    for k in leafnodes:
        v = leafnodes[k]
        print("{} [style=filled, fillcolor=green, label={}]".format(k, v))
    print("}")


if __name__ == "__main__":
    show_both_files_and_dirs = True
    edges, leafnodes = readFS_makeDotGraph(show_both_files_and_dirs)
    emitDotGraph(edges, leafnodes)
