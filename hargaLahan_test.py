from matplotlib import pyplot
import pandas as pd
dataPath= 'E:\\[SHP]\\RDTR Tenayan\\temp\\Harga Lahan\\hargaTanah3.csv'
# generate a univariate data sample
data =pd.read_csv(dataPath)
# histogram
pyplot.hist(data)
pyplot.show()