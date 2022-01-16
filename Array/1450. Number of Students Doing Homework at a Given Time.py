
def NumOfStudents(start,end,query):
    c = 0
    if len(start) != len(end):
        return None

    for i ,j in zip(start,end):
        print("i",i)
        print("j",j)
        if i<=query<=j:
            c +=1
    return c

s = [1,2,3]
e =  [3,2,7]
print(NumOfStudents(s,e,4))