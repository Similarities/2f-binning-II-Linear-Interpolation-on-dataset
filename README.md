# 2f-binning-II-Linear-Interpolation-on-dataset
linear interpolation between datapoints with constant binsize in x-axis 


Origin is a .txt file consisting of 2 coloumms (first: x, second: y, decimal in ".", separation " ", first row is skipped, data points sorted ascending). The x coloumn should have aequidistant binsize (constant binsinze, see example file). The programm interpolates linearly for a given new binsize (new binsize < orginal binsize) between the neighboured datapoints. This leads to accordingling new datapoints. Example: if the original binsize is 1, and the new binsize 0.1, the resulting dataset consist of 10x more datapoints. 

Python (x,y) 2.7, open file dialog (tk), sorts dataset by x-axis if not done in original file, numpy, makes a plot (matplotlib), saves the result in a .txt file. Runs only one time through the dataset.

Missing: OOD, Tests analysis of input data, if input data has wrong format might cause problems.
