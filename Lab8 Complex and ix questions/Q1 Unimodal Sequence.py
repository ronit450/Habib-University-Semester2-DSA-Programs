unimodel_sequence = input().split(" ")
unimodel_sequence = [int(i) for i in unimodel_sequence]


def getTopIndex_UnimodelSequence(unimodel_sequence):
    lower = 0
    higher = len(unimodel_sequence)
    while lower < higher:
        index = int((lower + higher) / 2)
        if unimodel_sequence[index] > unimodel_sequence[index - 1] and unimodel_sequence[index] > unimodel_sequence[
            index + 1]:
            index_found = index
            break
        elif unimodel_sequence[index] > unimodel_sequence[index + 1] and unimodel_sequence[index] < unimodel_sequence[
            index - 1]:
            higher = index + 1
        elif unimodel_sequence[index] > unimodel_sequence[index - 1] and unimodel_sequence[index] < unimodel_sequence[
            index + 1]:
            lower = index - 1

    return index_found


print(getTopIndex_UnimodelSequence(unimodel_sequence))