list=[]
def devide(l1):
    x=0
    y=1
    while x<len(l1)-1:
        while y<len(l1)-1:
            if l1[x]==l1[y]:
                x+=1
                y+=1
            else:
                list.append(l1[x])
                x+=1
                y+=1
        list.append(l1[len(l1)-1])
        return list
    
print(devide([1,1,1,2,3,4,4,4,5,6,6,7,7,8,8,8]))
