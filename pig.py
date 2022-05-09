import random
import tkinter # pip install tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * 
# 파일 찾는 창을 뛰우는 기능
from tkinter import filedialog # 서브 모듈은 따로 import를 해줘야 사용가능
from PIL import Image #pip install pillow

 
root = Tk()
root.title("Pig Game")

computer_points = 0

# ---------구동 함수------------
def game_computer(computer_points):
  while(computer_points<=100):
    choose = random.randrange(1, 3)  
    
    if choose == 1:
      print('컴퓨터는 도박을 합니다.')
    else:
      print('컴퓨터는 도박을 하지 않습니다')
      break;  
      
    value = dice()
    print(f'컴퓨터가 뽑은 숫자: {value}')
    
    if(value==1):
      computer_points = 0
      print('컴퓨터의 점수가 초기화되었습니다. Greedy')
      break;
    elif(computer_points>=100):
      print(f'컴퓨터가 승리하였습니다. {computer_points}')
      break;
    else:
      computer_points += value
      print(f'컴퓨터의 현재 점수: {computer_points} 점')




def add_dice():
    dir = dice()
    A_Player_score.config(text= "A Player Score : " + str(dir) )
    list_file.insert(END, dir)

# -----------버튼 함수-------------
# 폴더 선택
def dice():
    return random.randrange(1, 7)

# 비교 버튼
def stop():
    pass
    
# 시작
def start():    
    pass



# 파일 프레임 
file_frame = Frame(root)
file_frame.pack(fill= "x", padx=5, pady=5 ) #가로로 넓게

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="주사위를 굴린다", command=add_dice)
btn_add_file.pack(side="left")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="주사위를 멈춘다.", command=stop)
btn_add_file.pack(side="left")

# 리스트 프레임 A폴더
A_Player = LabelFrame(root, text="Player A Score")
A_Player.pack(fill="both", padx=5, pady=5)

# A player score
list_cframe = Frame(A_Player)
list_cframe.pack( fill="both")

A_Player_score = Label(list_cframe)
A_Player_score.pack(side="left", padx=5, pady=2)


# 리스트 프레임 B폴더
Bdir = LabelFrame(root, text="Player B Score")
Bdir.pack(fill="both", padx=5, pady=5)

Bdir_Route = Entry(Bdir) # 한줄일때 Entry
Bdir_Route.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)


# 리스트 프레임
list_frame = LabelFrame(root, text="진행사항")
list_frame.pack(fill="both", padx=5, pady=5, ipadx= 150)

scrollaber = Scrollbar(list_frame)
scrollaber.pack(side="right", fill= "y")

list_file = Listbox(list_frame, selectmode="extended", yscrollcommand=scrollaber.set)
list_file.pack(side="left", fill="both", expand=True)
scrollaber.config(command=list_file.yview)


# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="실행", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False,False)
root.mainloop()