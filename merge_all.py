import os

# creates a new file with all the kangyur in a single file. All \n are deleted.
path = './ekangyur_raw/'
with open('merged_ekangyur.txt', 'a', -1, 'utf-8') as f:
    for F in os.listdir(path):
        with open(path+F, 'r', -1, 'utf-8-sig') as g:
            f.write(g.read().replace('\n', ''))