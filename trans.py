import csv
import numpy as np

length = 0
i = 0
preout = []

def seprate(string):
    output = np.array(['time', '_HEADC_EYEBROWR_VERT', '_HEADC_EYEBROWL_VERT', '_HEADC_EYER_YAW', '_HEADC_EYEL_YAW', '_HEADC_EYES_PITCH'])
    file = open(string+'.ysq','r')
    contents = file.readlines()

    for item in contents:
        x = []
        cont = item.split()
        command = cont[1]
        x.append(cont[0])
        length = len(command)
        if (length % 5 != 0 ):
            print('Wrong number, redial please.')
        else:
            preout = ([command[i:i + 4] for i in range(0, len(command), 5)])
            for i in preout:
                x.append(i)
            output = np.row_stack((output, x))
    print(output)
    return output

def writers(string, array):
    writer = csv.writer(open(string+'.csv', 'w'))
    writer.writerows(array)
def all(string):
    form = seprate(string)
    writers(string, form)


all('motion_headcc')