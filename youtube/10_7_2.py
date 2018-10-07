import os
import glob
os.chdir('/home/kyoo/capstone_project/youtube/sub_data')
for files in glob.glob("*.vtt"):
    os.remove(files)