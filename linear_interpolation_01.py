# -*- coding: utf-8 -*-
"""
Spyder Editor
#, usecols=(2,0)
#delimiter='\t'  # for tab, default: whitespace
This is a temporary script file.
"""
import numpy as np
import Tkinter, tkFileDialog
#import os


import ntpath
import matplotlib.pyplot as plt
root = Tkinter.Tk()
root.withdraw()

ntpath.basename("a/b/c")

file_path = tkFileDialog.askopenfilename()
#open(file_path)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
print path_leaf(file_path)
#newname=os.splitext(path_leaf)[0]
#print newname
#filename = "%s.csv" % name
#f = open(filename , 'wb')


print ("subsampling - mean approximation with reading  .txt data")
print ('.......................................Zombie.SoC// similarities --- 2017')
print ('needs: 2D array, deciaml as "." separation "space", values sorted')
print ('script interpolates between two successive values')
increment= input("size of bin (float):")

def loadarray():
    #reads coloumn1 from txt / skips first rows (3), 
    liste1=np.loadtxt(file_path, skiprows=(3), usecols=(0,))
    #reads coloumn2 from txt / skips first rows (3), 
    liste=np.loadtxt(file_path, skiprows=(3), usecols=(1,))
    #converts loaded coloumn1 to an numpy array:
    matrix1 = np.array((liste1))
    #converts loaded coloumn2 to an numpy array:
    aa = np.array((liste))
    #joins the arrays into a 2xN array 
    submatrix1= np.column_stack((matrix1, aa))
    #plot input
    #plot_xy(submatrix1,"r")
    return submatrix1

def plot_xy(array,colour,name):
    x = array[:,0]
    y = array[:,1]
    plot=plt.scatter(x, y, color=colour,label=name)
    plt.legend(handles=[plot])
    plt.ylabel("input")
    plt.show()
   
   

def checkbinsize(newmatrix, increment):
    i=0
    N=len(newmatrix)
    print N,"datenpunkte"
    #empty array for submatrix 1x1
    ss=np.empty([1, 2])
    while i<N-1:
       binsize=newmatrix[i+1]-newmatrix[i]
       #print i, binsize, binsize[0,]
       if binsize[0,]==increment:
           i=i
       elif binsize[0,]>increment:
           # number of subbins - make integer/ round
           ratio = binsize[0,]/increment
           binnumber=int(round(ratio))
           # smallstep, value increase per sub bin
           smallstep=binsize[1,]/ratio 
           #extract submatrix (upper point)
           excerpt=newmatrix[i]
           #print "matrix wird rausgeschickt", i
           # calls "subbarray" - that gives a new subarray with number "ratio"
           # elements, values are increasing per "increment" with "smallstep"
           matrix2=subarray(binnumber,increment,excerpt,smallstep)
           #joins new subbarrays (and these include the original points)
           ss=np.concatenate((matrix2,ss))
           #ss.view('i8,i8').sort(order=['f0'], axis=0) 
           #print matrix2, ss         
       else: 
           print "please sort the table before putting..."
           ss.view('i8,i8').sort(order=['f0'], axis=0)
           i=0
       #result=np.concatenate((matrix2,ss))   
       i=i+1
       #return ss
    #last entry (missing otherwise) - complicated, since newmatrix[N-1] 
       # is not understand in the correct dimension (although it has)
    lastentry=np.empty([1, 2])
    lastentry[0,0]=newmatrix[N-1,0]
    lastentry[0,1]=newmatrix[N-1,1]
    print lastentry, "last entry",np.shape(lastentry),np.shape(ss)
    ss=np.concatenate((lastentry,ss))   
    ss.view('i8,i8').sort(order=['f0'], axis=0)
    plot_xy(ss[2:],"c","interpolation")
    plot_xy(newmatrix,"y","input_data")
    # save as textfile: with name, matrix (without first and last entry),
    #precision (.3 digits), coloumn separation Tab 
    np.savetxt("interpolation_binsize"+"_"+ repr(increment) +".txt", ss[1:],fmt='%.3E', delimiter='\t')
    print "neue Länge arry 2x", len(ss)
    print "alte länge array 2x", N
    #print ss

def subarray(binnumber,increment,excerpt,value):
    #ratio = int, increment = float (binsize that should be reached), 
    #excerpt= matrixelement  to be started (lower limit), 2D
    i=0
    zwischen=np.empty([binnumber, 2])
    x=excerpt[0,]
    v=excerpt[1,]
    #print x,v
    while i<=binnumber-1:
        zwischen[i,0]=x+i*increment
        zwischen[i,1]=v+i*value
       # round(ss[i,0],3)
       # round(ss[i,1],3)
        i=i+1
    return zwischen
    


newmatrix=loadarray()
#print newmatrix   
newmatrix=checkbinsize(loadarray(), increment)       
        