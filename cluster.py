import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons

data  = pd.read_csv('students_sheet.csv')
data.head(40)

# Defining two vectors for my data clustering: GPA and ECA(Extra curricular activities)
X = data[['ECA','gpa']]
plt.scatter(X["ECA"],X["gpa"],c='black')
plt.xlabel('ECA(Exta curriculum acticities)')
plt.ylabel('GPA')

K = 2
Centroids = (X.sample(n=K))
def setK(label):
	global K
	K = int(label)
	global Centroids
	Centroids = (X.sample(n=K))



def makeCentroids(val):
	plt.close()
	plt.scatter(X["ECA"],X["gpa"],c='black')
	plt.scatter(Centroids["ECA"],Centroids["gpa"],c='red')
	plt.xlabel('ECA(Exta curriculum acticities)')
	plt.ylabel('GPA')
	plt.draw()



axcolor = 'yellow'
rax = plt.axes([0.02, 0.5, 0.04, 0.14], facecolor=axcolor)
radio = RadioButtons(rax, ('2','3', '4', '5'))

axnext = plt.axes([0.02, 0.3, 0.06, 0.15])
bnext = Button(axnext, 'SIMULATE')

bnext.on_clicked(makeCentroids)
radio.on_clicked(setK)
plt.show()
diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["ECA"]-row_d["ECA"])**2
            d2=(row_c["gpa"]-row_d["gpa"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["gpa","ECA"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['gpa'] - Centroids['gpa']).sum() + (Centroids_new['ECA'] - Centroids['ECA']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["gpa","ECA"]]

color=['blue','green','cyan','orange','purple']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["ECA"],data["gpa"],c=color[k])
plt.scatter(Centroids["ECA"],Centroids["gpa"],c='red')
plt.xlabel('ECA')
plt.ylabel('GPA')
plt.show()