# Enter your code here. Read input from STDIN. Print output to STDOUT
def popular_author(b):
    new_dic = {}
    temp_list = []
    maximum = 0
    final_lst = []
    for i in range(len(b)):
        temp_list.append(b[i]['author'])
    for j in temp_list:
        if j in new_dic:
            new_dic[j] += 1
        else:
            new_dic[j] = 1
    for i in new_dic:
        key = new_dic[i]
        if int(key) > maximum:
            maximum = key
    for j in new_dic:
        key = new_dic[j]
        if int(key) == maximum:
            final_lst.append(j)
    final_lst.sort()
    return ", ".join(final_lst)


b = eval(input().strip())
print(popular_author(b))