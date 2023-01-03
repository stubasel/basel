def mySelectionSort(list):
          #Outer Loop controls the current position!
          for i in range(len(list)):
                    min = i 
                    #inner loop control the comparison!
                    for j in range (i+1, len(list)):
                              if list[min] > list[j]:
                                        min = j
                    # Without Temp Variable you can swap two numbers
                    list[i],list[min] = list[min], list[i]           
list = [3,5,2,1,6]
mySelectionSort(list)
print(list)