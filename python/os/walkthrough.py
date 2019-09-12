import os
os.chdir('<path to directory')

for root,dir,files in os.walk('<path>'):
  <do whatever>

# copy specific file extension files to a folder
# .mp4 in below example
for each in os.listdir("Path"):
    try:
        os.chdir("/path" + "/" + str(each))
        for file in glob.glob("*.mp4"):
            shutil.copy(os.getcwd() + "/" + str(file), "/folder_to_Copy/")
    except Exception:
        continue
