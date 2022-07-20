import printData as pd
import listGen
from Insertion import insertion


unsorted_list = listGen.generateRandomIntList(size=50, min_max=(99, 100))

pd.printData(unsorted_list, False)
insertion.insertionSort(unsorted_list)
pd.printData(unsorted_list, True)