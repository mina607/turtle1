import turtle
import math

# 시작점과 끝점의 거리 계산 함수
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y2)**2)

#스크린 생성
s = turtle.getscreen()

#거북이변수 지정
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

#시작점
start_x, start_y = -200, -200

t.penup()
t.goto(start_x, start_y)
t.pendown()
t.circle(10)

t.penup()
t.goto(-50, -125)
t.pendown()
t.pencolor("red")
for _ in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(150, 150)
t.pendown()
t.pencolor("green")
t.circle(10)

t.penup()
t.goto(start_x, start_y)
t.setheading(0)
t.pencolor("blue")
t.pendown()

t.forward(100)
t.left(90)
t.forward(200)
t.right(90)
t.forward(200)
t.left(90)
t.forward(150)
t.right(90)
t.forward(50)

# 끝점 좌표 저장
end_x, end_y = t.pos()

# 거리 계산
distance = calculate_distance(start_x, start_y, end_x, end_y)
print(f"시작점과 끝점 사이의 거리: {distance:.2f}")

t.hideturtle()
screen.mainloop()