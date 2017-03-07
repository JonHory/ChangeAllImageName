import os
import re
import sys

pattern = '([\w\W]*?)(@[0-9]+x)?(\.png|\.jpg)'
dic = {}
count = 0

def changeName(path, nPrefix):
    global count
    global dic
    global pattern
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if os.path.isfile(path + '/' + filename):
                matched = re.search(pattern, filename)
                if matched != None:
                    prefix = matched.group(1)
                    suffix = matched.group(2)
                    enffix = matched.group(3)
                    if suffix == None:
                        suffix = ''
                    if not dic.has_key(prefix):
                        dic[prefix] = nPrefix + "_" + prefix
                        count += 1
                    newName = dic[prefix] + suffix + enffix
                    os.rename(path + '/' + filename, path + '/' + newName)
            else:
                changeName(path + '/' + filename, nPrefix)

if __name__ == "__main__":
    path = sys.argv[1]
    nPrefix = sys.argv[2]
    changeName(path, nPrefix)
    print '===>>> addPrefixName with %s finish' % nPrefix
