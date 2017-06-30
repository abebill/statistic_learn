#--*-- coding:utf-8 --*--
#初始化相关参数
w = [0, 0]
b = 0
setp = 0

#参数调整
def adjust(item, study_r=1): #学习率初始化为1
    global w, b, setp
    for i in range(len(item[0])):
        w[i] += study_r * item[1] * item[0][i]
    b += item[1]
    setp += 1

def mis_value(item):
    #误分类值计算，该值小于等于时表示当前存在误分类点
    value = 0
    for i in range(len(item[0])):
        value += item[0][i] * w[i]
    value += b
    value *= item[1]
    return value

def decide(datas):
    flag = False
    for item in datas:
        mis = mis_value(item)
        if mis <= 0:
            flag = True
            adjust(item)
            print setp, item, w, b,mis
    if not flag:
        print setp+1, item, w, b,mis
        print "\n最终得到超平面相关参数：\n w= " + str(w) + ",  b=" + str(b)
    return flag

if __name__ == "__main__":
    training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]  #以书本中的数据集为例
    print '迭代次数', '误分类值', '权值w', '截距b', '判断值'
    while decide(training_set):
        continue