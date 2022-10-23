import os
file_list=[f for f in os.listdir() if f.endswith("")]
#file_list=[f for f in os.listdir("dataset") if f.endswith(".csv")]
for i in range(0,len(file_list)):
    print("{} : {}".format(i+1, file_list[i]))