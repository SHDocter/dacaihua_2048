import numpy as np
import random as rd
def Up(GameList):#向上移动
    NewList1=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])#用两个零矩阵过渡
    NewList2=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])#懒得用zeros了
    for j in range(4):#先储存非零量在赋值给新列表
        NoneZeroList = []
        for i in range(4):
            if GameList[i,j]!=0:
                NoneZeroList.append(GameList[i,j])
        for k in range(len(NoneZeroList)):
            NewList1[k,j]=NoneZeroList[k]
    for j in range(4):#相同值合并
        for i in range(3):
            if NewList1[i,j]==NewList1[i+1,j]:
                NewList1[i,j]=NewList1[i,j]*2
                NewList1[i+1,j]=0
    for j in range(4):#合并后再移动
        NoneZeroList=[]
        for i in range(4):
            if NewList1[i,j]!=0:
                NoneZeroList.append(NewList1[i,j])
        for k in range(len(NoneZeroList)):
            NewList2[k,j]=NoneZeroList[k]
    NoneSame=0
    for i in range(4):
        for j in range(4):
            if GameList[i,j]!=NewList2[i,j]:
                NoneSame=1
                break
    if NoneSame==1:
        for i in range(4):
            for j in range(4):
                GameList[i,j]=NewList2[i,j]
        return 1
    else:
        return 0
def Down(GameList):
    NewList1=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    NewList2=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    for j in range(4):
        NoneZeroList = []
        for i in range(-1,-5,-1):
            if GameList[i,j]!=0:
                NoneZeroList.append(GameList[i,j])
        for k in range(len(NoneZeroList)):
            NewList1[3-k,j]=NoneZeroList[k]
    for j in range(4):
        for i in range(-1,-4,-1):
            if NewList1[i,j]==NewList1[i-1,j]:
                NewList1[i,j]=NewList1[i,j]*2
                NewList1[i-1,j]=0
    for j in range(4):
        NoneZeroList=[]
        for i in range(-1,-5,-1):
            if NewList1[i,j]!=0:
                NoneZeroList.append(NewList1[i,j])
        for k in range(len(NoneZeroList)):
            NewList2[3-k,j]=NoneZeroList[k]
    NoneSame=0
    for i in range(4):
        for j in range(4):
            if GameList[i,j]!=NewList2[i,j]:
                NoneSame=1
                break
    if NoneSame==1:
        for i in range(4):
            for j in range(4):
                GameList[i,j]=NewList2[i,j]
        return 1
    else:
        return 0
def Left(GameList):
    NewList1 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    NewList2 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    for i in range(4):
        NoneZeroList=[]
        for j in range(4):
            if GameList[i,j]!=0:
                NoneZeroList.append(GameList[i,j])
        for k in range(len(NoneZeroList)):
            NewList1[i,k]=NoneZeroList[k]
    for i in range(4):
        for j in range(3):
            if NewList1[i,j]==NewList1[i,j+1]:
                NewList1[i,j]*=2
                NewList1[i,j+1]=0
    for i in range(4):
        NoneZeroList=[]
        for j in range(4):
            if NewList1[i,j]!=0:
                NoneZeroList.append(NewList1[i,j])
        for k in range(len(NoneZeroList)):
            NewList2[i,k]=NoneZeroList[k]
    NoneSame=0
    for i in range(4):
        for j in range(4):
            if GameList[i,j]!=NewList2[i,j]:
                NoneSame=1
                break
    if NoneSame==1:
        for i in range(4):
            for j in range(4):
                GameList[i,j]=NewList2[i,j]
        return 1
    else:
        return 0
def Right(GameList):
    NewList1 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    NewList2 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    for i in range(4):
        NoneZeroList=[]
        for j in range(-1,-5,-1):
            if GameList[i,j]!=0:
                NoneZeroList.append(GameList[i,j])
        for k in range(len(NoneZeroList)):
            NewList1[i,3-k]=NoneZeroList[k]
    for i in range(4):
        for j in range(-1,-4,-1):
            if NewList1[i,j]==NewList1[i,j-1]:
                NewList1[i,j]*=2
                NewList1[i,j-1]=0
    for i in range(4):
        NoneZeroList=[]
        for j in range(-1,-5,-1):
            if NewList1[i,j]!=0:
                NoneZeroList.append(NewList1[i,j])
        for k in range(len(NoneZeroList)):
            NewList2[i,3-k]=NoneZeroList[k]
    NoneSame=0
    for i in range(4):
        for j in range(4):
            if GameList[i,j]!=NewList2[i,j]:
                NoneSame=1
                break
    if NoneSame==1:
        for i in range(4):
            for j in range(4):
                GameList[i,j]=NewList2[i,j]
        return 1
    else:
        return 0
def Random2or4(GameList):
    ZeroList = []
    Count4 = 0
    for i in range(4):
        for j in range(4):
            if GameList[i, j] == 0:
                ZeroList.append([i, j])
    for i in range(4):
        for j in range(4):
            if GameList[i, j] == 4:
                Count4 = 1
    if Count4 == 0:
        RandomNum = rd.choice(ZeroList)
        GameList[RandomNum[0], RandomNum[1]] = 2
    else:
        RandomNum = rd.choice(ZeroList)
        GameList[RandomNum[0], RandomNum[1]] = rd.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
def Rule(GameList):
    Temp2048 = np.sum(GameList == 2048)
    Temp0 = np.sum(GameList == 0)
    if Temp2048 != 0:
        return 1
    if Temp0!=0:
        return 2
    elif Temp0==0:
        TempSame=0
        for i in range(4):
            for j in range(3):
                if GameList[i, j] == GameList[i,j+1]:
                    TempSame = 1
                    break
        for j in range(4):
            for i in range(3):
                if GameList[i,j]==GameList[i+1,j]:
                    TempSame = 1
                    break
        if TempSame==0:
            return 0
        else:
            return 3

