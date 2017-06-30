#--*-- coding:utf-8 --*--
#初始化相关参数
w = [0, 0]
b = 0
setp = 0

#参数调整
def charge(item, study_r=1): #学习率初始化为1
    global w, b, setp
    for i in range(len(item[0])):
        w[i] += study_r * item[1] * item[0][i]
    b += item[1]
    setp += 1

def cal(item):
    """
    calculate the functional distance between 'item' an the dicision surface. output yi(w*xi+b).
    """
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res

def check():
    """
    check if the hyperplane can classify the examples correctly
    """
    flag = False
    for item in training_set:
        if cal(item) <= 0:
            res = cal(item)
            flag = True
            charge(item)
            print setp, item, w, b,res
    if not flag:
        print setp, item, w, b
        print "最终得到超平面相关参数： w= " + str(w) + ",  b=" + str(b)
    return flag

if __name__ == "__main__":
    training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]
    print '迭代次数', '误分类值', '权值w', '截距b'
    while check():
        pass