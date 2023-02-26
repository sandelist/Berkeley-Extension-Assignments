# This programme prints the filenames of zero length files and count them:

import os

empty_file_count = 0

for (root,dirs,files) in os.walk('.', topdown=True):
    
    for i in files:
        file_link = root + '/' + i
        
        if os.path.getsize(file_link) == 0:
            print('Zero length file:', i)
            empty_file_count = empty_file_count + 1

print('This folder and all its subfolders have ' + str(empty_file_count) + ' zero length files')