import printData as pd
import listGen

from Insertion import insertion


# unsorted_list = listGen.generateRandomIntList(10, 0, 30)
unsorted_list = [9, 8, 7, 6]

pd.printData(unsorted_list, False)
insertion.insertionSort(unsorted_list)
pd.printData(unsorted_list, True)