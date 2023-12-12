import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt. subplots()
c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('점의 모양을 선택하시오',['o', '^', 's', 'p'])

a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)


x = []
y1 = []
y2 = []
for i in range(-29, 30, 3):
    x.append(i)
    y1.append(a*i*i + b*i + c)
    y2.append(d/i)

plt.plot(x, y1, color = c1, linestyle = s1, marker = m1)
st.pyplot(fig)

# a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
# b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
# c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
# d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)

# x = []
# y = []
# for i in range(-20,21,1):
#     x.append(i)
#     y.append(-2*i*i+ + 3*i +5)

# plt.plot(x,y,color = 'red', linestyle = '--', marker = 'p')
















# import sys
# sys. exit()
# import streamlit as st
# # import time 
# # import random as r
# import matplotlib.pyplot as plt
# import numpy as np


# col1, col2, col3 = st. columns(3)

# with col1:
#     c1 = st. radio('선을 색을 선택하세요!',['red','green','blue','black'])
# with col2:
#     s1 = st. radio('선을 형태를 선택하세요~',['-',':','-.','--'])
# with col3:
#     t1 = st. radio('점의 모양을 선택하새요',['o','h','s','p','^'])
# fig, ax = plt.subplots()


# x=[]
# y=[]
# for i in range(-20,21,2):
#     x.append(i)
#     y.append(-2*i*i +3*i +5)

# plt.plot(x,y,color = c1, linestyle = s1, marker = t1)
# st.pyplot(fig)


# fig, ax = plt. subplots()

# plt. plot(x, y)
# st.pyplot(fig)

# x =[]
# for i in range(-100, 101):
#     i
# #     x.append(i)
# # x

# x = []
# y=[]
# for i in range(-100, 101):
#     x.append(1/10.0)
#     y.apprend(2*i*i+5*i+3)



# y = []
# # s = [7, 1, 9, -3, 3, 10]
# # s
# # a = sum(s)
# # 'sum', a
# # mx = max(s)
# # 'max', mx
# # mn = min(s)
# # 'min', mn

# # mx = -1e10
# # mx
# # for i in s:
# #     if i > mx:
# #         mx = i
# # mx



# # s1 = 1
# # s2 = 2
# # s3 = 3
# # s4 = 4
# # s5 = 5
# # s1, s2, s3, s4, s5

# # s = ['a', 'b', 'c', 'd', 'e']
# # s[-1]

# # if 'r' not in s:
# #     '1'
# # else:
# #     '2'

# # import turtle
# # t = turtle.Turtle()
# # t.shape("turtle")



# # def square(x, y, lx, ly ):
# #     t.up()
# #     t.goto(x, y)
# #     t.down()
# #     for i in range(2):
# #         t.forward(lx)
# #         t.left(90)
# #         t.forward(ly)
# #         t.left(90)

# # square(-200, 0, 100, 50)
# # square(0, 0, 100, 150)
# # square(200, 0, 100, 100)

# # turtle.done()

# # import time

# # def user_sum(n):
# #     s = 0
# #     for i in range(1, n+1):
# #         s = s + i
# #     s

# # user_sum(100)
# # user_sum(200)

# # s = 0
# # for i in range(10, 21):
# #     s = s + i
# # s


# # import turtle
# # t  = turtle.turtle()
# # t. shape('turtle')
# # t.speed(1)

# # length = 5
# # for i in range(8):
# #     t.forward(length)
# #     t.rigth(89)
# #     length += 5




# # s = 50
# # if s >= 90:
# #     st.write('귀하의 점수는' + str(s) + '점으로 :red[합격] 입니다')
# # elif s >=80:
# #     '귀하의 점수는' + str(s) + '점으로 불합격 입니다.'
# # elif s >=70:
# #     '귀하의 점수는' + str(s) + '점으로 불합격 입니다.'
# # elif s >=60:
# #     '귀하의 점수는' + str(s) + '점으로 불합격 입니다.'
# # else:
# #     '귀하의 점수는' + str(s) + '점으로 불합격 입니다.'



# # a = 1
# # b = '1'
# # c = "1"

# # print('a=',a)
# # 'a=', a
# # b
# # c



# # for i in range(3. 10, 2):
# #     's = ', s, 'i =', i
# #     s = s + i
# #     's + i = ', s
# # s = 1 + 2 + 3 + 4 + 5
# # s

# # '7과 4의 연산'

# # '덧셈', 7 + 4
# # '뺄셈', 7 - 4
# # '곱셈', 7 * 4
# # '몫', 7 // 4
# # '나눗셈', 7 / 4
# # '나머지', 7 % 4
# # '거듭제곱',7 ** 4

# # import turtle
# # t = turtle.Turtle()
# # t.shape('turtle')
# # t.speed(1)





# # turtle.done()

# # t.fillcolor("blue")
# # t.begin_fill()
# # t.circle(100)
# # t.end_fill()

# # t.forward(100)

# # t.fillcolor("orange")
# # t.begin_fil
# # )
# # r =20
# # area = 3.14*r*r
# # area

# # distance =150
# # angle =120
# # for i in range(3):
# #     t.forward(distance)
# #     t.left(angle)


# # t.forward(100)
# # t.right(90)
# # t.forward(100)
# # t.right(90)
# # t.forward(100)
# # t.right(90)
# # t.forward(100)
# # turtle.done()


# # a = 3.141592*10*10.0
# # b = (1/100)*1234*55

# # print("hello")

# # st.write("hello")

# # st.write("고양이 + 강아지")

# # st.write("반가워요")

# # print("파이썬")
# # a=2+3+8
# # a
# # print(a)
# # st.write('스트림릿')
# # st.title('streamlit image')
# # st.image('im.jfif')