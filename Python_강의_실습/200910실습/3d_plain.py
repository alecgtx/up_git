
# vpython 라이브러리 사용
# 3차원 평면을 생성하여 향후 자이로 센서와 연동, 3차원 평면의 기울기 회전 등을 동기화 시킬 예정임

from visual import *
from math import *
 
ball = sphere(pos=(0,0,0), radius=3, color=color.green)
xz_plan = box(pos=(0,0,0), size=(50,0.1,50), color=color.red, opacity=0.8)
xz_plan_b = box(pos=(0,-25,0), size=(50,0.1,50), color=color.red, opacity=0.3)
xz_plan_t = box(pos=(0,25,0), size=(50,0.1,50), color=color.red, opacity=0.3)
xy_plan = box(pos=(0,0,0), size=(50,50,0.1), color=color.green, opacity=0.8)
xy_plan_b = box(pos=(0,0,-25), size=(50,50,0.1), color=color.green, opacity=0.3)
xy_plan_t = box(pos=(0,0,25), size=(50,50,0.1), color=color.green, opacity=0.3)
yz_plan = box(pos=(0,0,0), size=(0.1,50,50), color=color.blue, opacity=0.8)
yz_plan = box(pos=(-25,0,0), size=(0.1,50,50), color=color.blue, opacity=0.3)
yz_plan = box(pos=(25,0,0), size=(0.1,50,50), color=color.blue, opacity=0.3)
pointer1 = arrow(pos=vector(-12,0,0), axis=vector(25,0,0), shaftwidth=1.5, shininess=1.5, color=color.red)
pointer2 = arrow(pos=vector(0,-12,0), axis=vector(0,25,0), shaftwidth=1.5, shininess=1.5, color=color.green)
pointer3 = arrow(pos=vector(0,0,-12), axis=vector(0,0,25), shaftwidth=1.5, shininess=1.5, color=color.blue)
