'''
#알고리즘 1일차 수업

#tuple과 list의 차이: list는 수정 가능하고 tuple은 수정 불가능 연필과 볼펜이라고 생각하셈

nums=[0,1,2,3,4,5,6,7,8,9]
print(nums)
nums[2:5] = []
print(nums)
del nums[4]
print(nums)
===============================================================
list1=[1,2,3,4,5]
list2=[10,11]
listadd=list1+list2
print(listadd)
print(list1)
print(list2)
listmulti=list2*3
print(listmulti)
print("--"*40)
================================================================
listmulti1=[(list1[0]*3),(list1[1]*3),(list1[2]*3),(list1[3]*3),(list1[4]*3)] #이중리스트
print(listmulti1)
lol=[[1,2,3],[4,5],[6,7,8,9]]
print(lol[0])
print(lol[2][1])

for sub in lol:
    for item in sub:
        print(item,end='')
    print()#이중리스트에서 각각 리스트 출력하기
===================================================================
nums=[1,2,3,4]
nums.append(5)#append는 삽입할 위치 알려주지 않음
print(nums)
nums.insert(2,99)#index가 2인 곳에 들어가도록 한다
print(nums)
===================================================================
nums=[1,2,3,4]
nums[2:2]=[90,91,92]#끼워서 들어가는 개념
print(nums)

nums=[1,2,3,4]
nums[2]=[90,91,92]#[2]의 값과 바꿔치기 하는 개념
print(nums)
===================================================================
list1=[1,2,3,4,5]
list2=[10,11]
list1.extend(list2)
print(list1)
list3=list1+list2
print(list3)
print(list1)
===================================================================
#삭제하는 방법들
score=[88,95,70,100,99,80,78,50]
score.remove(100) #remove 만일 찾는 값이 없으면, 예외를 발생시킨다
print(score)

del(score[2])
print(score) #del

score[1:4]=[]
print(score) #=[]

score.clear()
print(score) #clear

score=[88,95,70,100,99,80,78,50]
score[:]=[]
print(score)#score.clear()와 같다

del score[:]#del [:]
print(score)
==================================================================='''