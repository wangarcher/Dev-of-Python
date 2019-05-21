import pandas as pd
import numpy as np


wt = pd.read_csv('test1.csv')
print(wt)
data1 = pd.read_csv('qtmd.csv')
data2 = pd.read_csv('test.csv')
res = pd.merge(data1, data2, on=['time','_ARML_UPPER_ROLL', '_ARML_UPPER_YAW', '_ARML_MIDDLE_PITCH', '_ARML_MIDDLE_YAW', '_ARML_EDGE_ROLL', '_ARMR_UPPER_ROLL', '_ARMR_UPPER_YAW', '_ARMR_MIDDLE_PITCH', '_ARMR_MIDDLE_YAW', '_ARMR_EDGE_ROLL', '_HANDL_THUMB_PITCH', '_HANDL_INDEX_PITCH', '_HANDL_MIDDLE_PITCH', '_HANDL_RING_PITCH', '_HANDL_LITTLE_PITCH', '_HANDR_THUMB_PITCH', '_HANDR_INDEX_PITCH', '_HANDR_MIDDLE_PITCH', '_HANDR_RING_PITCH', '_HANDR_LITTLE_PITCH', '_HEADC_EYEBROWR_VERT', '_HEADC_EYEBROWL_VERT', '_HEADC_EYER_YAW', '_HEADC_EYEL_YAW', '_HEADC_EYES_PITCH'], how='outer')
res.to_csv('test1.csv',index=False,sep=',')


