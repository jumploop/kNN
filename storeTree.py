#使用pickle模块存储决策树
import pickle
def storeTree(inputTree,filename):
    with open(filename,'w') as fw:
        pickle.dump(inputTree,fw)

def grabTree(filename):
    fr = open(filename)
    return pickle.load(fr)
