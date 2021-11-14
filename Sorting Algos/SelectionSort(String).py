#Program to sort an array of strings using Selection Sort

def SelectionSortString(arr,n):

    for i in range(n):
        min_index = i
        min_str = arr[min_index]

        for j in range(i+1,n):

            if min_str > arr[j]:

                #make arr[j] min string
                min_str = arr[j]
                min_index = j

        #Swap the found minimum element with the first element

        if min_index != i:

            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr


arr = ["GeeksforGeeks", "Practice.GeeksforGeeks", "GeeksQuiz"]

print("Given Array")

for i in range(len(arr)):
    print(i,":",arr[i])

print("\n Sorted Array")
for i in range(len(arr)):
    print(i,":",SelectionSortString(arr,len(arr))[i])