import os
import shutil

import re

directory = old_directory
directory1 = new_directory

p = re.compile('R18_[A-Za-z]+_[A-Za-z]+')

for filename in os.listdir(directory):
    result = p.search(filename)
    if result:
        for filename1 in os.listdir(directory1):
            result1 = p.search(filename1)
            if result1:
                if result.group() == result1.group():
                    os.remove(directory1 + "/" + filename1)
                    newpath = shutil.copy(
                        directory + "/" + filename,
                        directory1 + "/" + filename)
                    os.remove(directory + "/" + filename)
                    break
