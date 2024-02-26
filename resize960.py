import sys
import PIL
import os
import os.path
from PIL import Image
from pathlib import Path


if len(sys.argv) < 3:
    print("%s resize pictures width to 960.\n" % sys.argv[0])
    print("Usage: %s [picture dir to resize] [output dir] <new width>\n" % sys.argv[0])
    sys.exit(0)

# f = r'../coco/images'
# f_new = r'../coco/images-960'
f = sys.argv[1]
f_new = sys.argv[2]
# new_width = int(sys.argv[3]) or 960
# print(len(sys.argv))
# if len(sys.argv) > 3:
#     print(960) 
# else:
#     print(int(sys.argv[3]))
new_width = 960 if len(sys.argv) <= 3 else int(sys.argv[3])

if not Path(f_new).is_dir():
    Path(f_new).mkdir(parents=True, exist_ok=True)

for file in os.listdir(f):
    f_img = f+"/"+file
    f_img_new = f_new+"/"+Path(f_img).stem+"-960"+Path(f_img).suffix
    img = Image.open(f_img)
    size_ratio = new_width / img.width
    new_height = int(img.height*size_ratio)
    # print(f_img,img.width,img.height, f_img_new,new_width,new_height)
    img = img.resize((new_width,new_height))
    if not Path(f_img_new).is_file():
        print("Saving",f_img_new,"...")
        img.save(f_img_new)
    else:
        print("File Already Existed:",f_img_new)
