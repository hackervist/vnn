import os


#  get the list of image names
lists = os.listdir("/home/thanos/.keras/datasets/faceless/validation/saneh/saneh2")
classes = "saneh"
str_arry = []

width = 600
height = 600
x1 = 100
x2 = 500
y1 = 100
y2 = 500
header = "filename, width, height, class, xmin, ymin, xmax, ymax \n"

text_file = open("../workspace/training_demo/annotations/test_labels.csv", "a")
text_file.write(header)
# generate CSV structure
for i in lists:
    stringi = i +  ", {}, {}, {}, {}, {}, {}, {} \n".format(width, height, classes, x1, y1, x2, y2)
    # print("strigni ", stringi)
    str_arry.append(stringi)
    
    # output into a CSV FILE
    text_file.write(  stringi )

text_file.close()
print("CSV created!")