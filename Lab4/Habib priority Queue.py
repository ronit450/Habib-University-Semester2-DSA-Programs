issues = [["AC Not working in Tariq Rafi", 5],["Password Change Issue",4],["Need Installation on laptop",3],["Need license",1],["Lab PCs Setup",3],["Login Issue",4]]
def arrangment(queue):
    i = 0
    length = length1(queue)
    while i < length:
        j = length - 1
        while j > 0 :
            if top(queue,j) > top(queue,j-1):
                queue[j] , queue[j-1] = queue[j-1] , queue[j]
            j -=1
        i += 1
    return queue
def top(queue,counter):
    if is_empty(queue) == False:
        return queue[counter][1]
    else: return 0
def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
def length1(lst):
    counter = 0
    for i in lst:
        counter += 1
    return counter

temp = arrangment(issues)
for i in range(len(temp)):
    print(temp[i][0])