import ast
rectangle_records = input()
rectangle_records = ast.literal_eval(rectangle_records)
record_title = input()
def sort_rectangles(rectangle_records, record_title):
    for i in range(1,len(rectangle_records)):
        for j in range (i,0,-1):
            if rectangle_records[j][record_title] < rectangle_records[j-1][record_title]:
                temp = rectangle_records[j]
                rectangle_records[j] = rectangle_records[j-1]
                rectangle_records[j-1] = temp
            else :
                break
    return rectangle_records
print(sort_rectangles(rectangle_records, record_title))