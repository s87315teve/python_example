from PIL import Image
import os

while True:
    img_list=os.listdir(os.path.abspath(os.getcwd()))
    for i, img_file in enumerate(img_list):
        print("{}: {}".format(i, img_file))
    img_index=int(input("choose file (-1 = exit) : "))
    if img_index==-1:
        exit()
    img = Image.open(img_list[img_index])
    print(img.mode)
    fig = img.convert('RGB')
    print(fig.mode)
    temp=img_list[img_index].find(".") 
    filename=img_list[img_index][:temp]
    filename=filename+".eps"
    print(filename)
    fig.save(filename, lossless = True)
    print("finished: covert {} to {} ".format(img_list[img_index], filename))


