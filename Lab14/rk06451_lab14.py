def insert(bst,key):
    if len(bst) == 0 :
        bst['value'] = key
        bst['left'] = {}
        bst['right'] = {}
    else:
        if bst['value'] < key:
            bst['right'] = insert(bst['right'],key)
        else:
            bst['left'] = insert(bst['left'],key)
    return bst
def exist(bst,key):
    if len(bst) == 0 :
        return False
    if bst['value'] == key:
        return True
    elif  key < bst['value']:
        return exist(bst['left'],key)
    else:
        return exist(bst['right'],key)
def minimum(bst,starting_node):
    if starting_node == bst['value']:
        def helper_of_min(bst):
            if bst['left'] == {}:
                return bst['value']
            else:
                return helper_of_min(bst['left'])
        return helper_of_min(bst)
    elif starting_node > bst['value']:
        return minimum(bst['right'],starting_node)
    else:
        return minimum(bst['left'],starting_node)
def maximum(bst,starting_node):
    if starting_node == bst['value']:
        def helper_of_max(bst):
            if bst['right'] == {}:
                return bst['value']
            else:
                return helper_of_max(bst['right'])
        return helper_of_max(bst)
    elif starting_node > bst['value']:
        return minimum(bst['right'],starting_node)
    else:
        return minimum(bst['left'],starting_node)
def inorder_traversal(bst):
    if bst['left'] != {}:
        inorder_traversal(bst['left'])
    print(bst['value'],end=", ")
    if bst['right'] != {}:
        inorder_traversal(bst['right'])
def postorder_traversal(bst):
    if bst['left'] != {}:
        postorder_traversal(bst['left'])
    if bst['right'] != {}:
        postorder_traversal(bst['right'])
    print(bst['value'], end=", ")
def preorder_traversal(bst):
    print(bst['value'], end=", ")
    if bst['left'] != {}:
        preorder_traversal(bst['left'])
    if bst['right'] != {}:
        preorder_traversal(bst['right'])





def question1():
    bst = {}
    key = [68, 88, 61, 89, 94, 50, 4, 76, 66, 82]
    for i in key:
        insert(bst, i)
    print(exist(bst, 50))
    print(exist(bst,49))
    print(minimum(bst, 68))
    print(minimum(bst, 88))
    print(maximum(bst,68))
    print(maximum(bst,61))
    print('Inorder_traversal:')
    inorder_traversal(bst)
    print()
    print('Post Order Traversal:')
    postorder_traversal(bst)
    print()
    print('Pre Order Traversal')
    preorder_traversal(bst)
def question2():
    bst = {}
    lst = ['begin','do','else','end','if','then','while']
    for i in lst:
        insert(bst,i)

question1()