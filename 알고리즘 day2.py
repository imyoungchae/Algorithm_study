'''
#알고리즘 2일차 수업


#pop과 append
score=[88,89,98,97,85,33,22,45,66,55]
print(score.pop()) #55: 제일 뒤에 있는 값

x=score.pop()
print(x)#55앞의 값: 66

print(score)#55와 66이 튀어나오고 남은 값들
print(score.pop(-1))#(-1)은 ()과 같음 즉, 가장 마지막 값이 튀어나옴 즉 45
print(score.pop(-1))#45앞의 값 22
score.append(77) #77을 추가하세여
print(score)#77이 끝에 들어가도록 출력이 된다

#list내의 값 찾기
score=[88,89,98,97,85,33,100,22,45,66,55]
perfect=score.index(100)
print("만점받은 학생은 "+str(perfect)+"번입니다.")
pernum=score.count(100)
print("만점자 수는 "+str(pernum)+"명입니다.")

#len, max, min
score=[88,89,98,97,85,33,100,22,45,66,55]
print("학생 수는 %d명입니다."%len(score))
print("최고 점수는 %d입니다."%max(score))
print("최저 점수는 %d입니다."%min(score))

#함수와 메서드의 차이
#함수: 함수 이름을 통해 함수를 사용할 수 있다
#ex) print(),type(),int()
#함수의 값을 변수에 대입 가능

#메소드: 객체와 연관되어 사용된다 사용하고자하는 대상이 .으로 연결되어 있어야 함
#ex) .append(), .slpit() 등

#매소드는 클래스 내에서 정의되므로 해당 클래스에 종속되며 함수가 매소드보다 더 포괄적인 의미를 가진다
ans=input('결제 하시겠습니까?')
if ans in['yes','y','ok','예','당근']:
    print('구입해주셔서 감사합니다')
else:
    print('안녕히가세요')

#sort/정렬

score=[88,95,70,100,99]

score.sort()
print(score)

score.reverse()
print(score)
#sort의 단점: 원래 list의 순서가 바뀌어버림 

#sort의 대안 sorted : 아예 새로은 list를 만듬(sorted: 메소드 아니고 함수)
score=[88,95,70,100,99]
score2=sorted(score)
print(score2)#정렬되어 70 88 95 99 100
print(score)#그대로 88 95 70 100 99

country=["Korea",'japan','China','america']
country.sort()#대문자, 소문자 구분하여 알파벳순으로 배열
print(country)
country.sort()#대문자소문자 구분없이 정렬하는 법
country.sort(key=str.lower)#대문자, 소문자 구분하지 않고 알파벳순으로 배열
print(country)

#onetuple
tu=2,#튜플임
value=2#튜플아님
value1=(2)#튜플아님
value2=(2,)#튜플임
value3=2,3#튜플임
print(tu)#출력하면 괄호를 열어 튜플임을 표시해준다.
print(value)

#unpacking
tu='이순신','김유신','강감찬'
lee,kim,kang=tu
print('lee')
print('kim')
print('kang')

#swap
a,b,c=12,34,29
print(a,b,c)
a,b,c=b,a,c
print(a,b,c)#파이썬은 별도의 temp없이 둘이 바로 교환 가능


#Tuple 바꾸기(list를 사용하여 가능)
score=[88,95,70,100,99]
tu=tuple(score)
print(tu)
li=list(tu)
li[0]=100
print(li)

#divmod
d,m=divmod(7,3)
print('몫',d)
print('나머지',m)

#딕셔너리
dic={'boy':'소년','school':'학교','book':'책'}
print(dic)
print(dic['boy'])
print(dic['school'])
print(dic.get('student'))#방법1.없는 단어를 None 이라고 출려되게 설정하기
print(dic.get('student','사전에 없는 단어입니다.'))#방법2.없는 단어를 원하늠 문장이 출력되게 설정하기
if 'student' in dic:#방법3. 없는 단어를 if문에 따라 출력되게 하기
    print('사전에 있는 단어입니다')
else:
    print('이 단어는 사전에 없습니다')

#딕셔너리 값 바꾸기
dic={'boy':'소년','school':'학교','book':'책'}
dic['boy']='남자애'
dic['girl']='소녀'
del dic['book']
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

#딕셔너리 값 합치기 dicupdate
dic={'boy':'소년','school':'학교','book':'책'}
dic2={'student':'학생','teacher':'선생님','book':'서적'}
dic.update(dic2)
print(dic)
   #-------------------------------------------------------------
'''
#list to dic
li=[['boy','소년'],['school','학교'],['book','책']]
dic=dict(li)
print(dic)
li1=list(dic)
print(li1)