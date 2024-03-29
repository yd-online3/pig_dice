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
nan_value = 0
computer_points = 0
a_dice_merge = 0
Aplay_total = 0
computer_first = 0

# ---------구동 함수------------
def choose_keep_playing():
    return random.randrange(0, 1)


def game_computer(computer_points):
  number = dice()
  temp_points = 0
  if(number==1):
    temp_points = 0
    return temp_points, 1 # reset Computer's score
  else:
    temp_points = number # Computer win this game

  while(computer_points<=100):

    value = choose_keep_playing()


    if value == 0:
      number = dice()
      if(number==1):
        temp_points = 0
        return temp_points# reset Computer's score
      else:
        temp_points += number # Computer win this game
        print(f'{temp_points},{number} 꼭')
    else:
      computer_points = computer_points + temp_points # stop game



# def game_computer():
#   number = dice()
#   temp_points = 0
#   if(number==1):
#     temp_points = 0
#     return temp_points, 1 # reset Computer's score
#   else:
#     temp_points = number # Computer win this game
    
#   while(point<=100):
  
#     value = choose_keep_playing()
#     print(f'컴퓨터 진행여부: {value}')
    
#     if value == 0:
#       number = dice()
#       if(number==1):
#         temp_points = 0
#         return temp_points, 1 # reset Computer's score
#       else:
#         temp_points += number
#         point += temp_points # Computer win this game
#     else:
#       return temp_points, 2 # stop game

  

# def add_dice():
#     number = dice()
#     if number != 1:
#         Play_A_Score_list_file.insert(END, number)
#     else:
#         string = 'Player turn is over'
#         Play_A_Score_list_file.insert(END, string)
       
#         computer_points, value = game_computer(computer_points)
#         if value == 1:
#           string = 'Computer turn is over'
#           Computer_list_file.insert(END, string)
      
#         elif value == 2:
#           Computer_list_file.insert(END, computer_points)
          
def add_dice():
    number = dice()
    if number != 1:
        Play_A_Score_list_file.insert(END, number)
    else:
        string = 'Player turn is over'
        Play_A_Score_list_file.insert(END, string)
        game_computer(computer_points) 
        string = 'Computer turn is over'
        Computer_list_file.insert(END, string)           

            



# -----------버튼 함수-------------
# 폴더 선택
def dice():
    return random.randrange(1, 7)


# 비교 버튼
def stop():
    total = Aplay_total
    total = sum(Play_A_Score_list_file.get(0,END))
    A_Player_score.config(text= "A Player Score : " + str(total))
    game_computer()

# 시작
def start():    
    pass


# 파일 프레임 
file_frame = Frame(root)
file_frame.pack(fill= "x", padx=5, pady=5 ) #가로로 넓게

roll_dice = Button(file_frame, padx=5, pady=5, width=12, text="주사위를 굴린다", command=add_dice)
roll_dice.pack(side="left")


btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="주사위를 멈춘다.", command=stop)
btn_add_file.pack(side="left")


# 리스트 프레임 A폴더
A_Player = LabelFrame(root, text="Player A Score")
A_Player.pack(fill="both", padx=5, pady=5)


# A player score
A_Player_list_frame = Frame(A_Player)
A_Player_list_frame.pack( fill="both")


A_Player_score = Label(A_Player_list_frame, text= "A Player Score : ")
A_Player_score.pack(side="left", padx=5, pady=2)

temp_A_Player_score = Label(A_Player_list_frame, text= "Temp Player Score : ")
temp_A_Player_score.pack(side="left", padx=5, pady=2)


# Computer score
Computer_score_list_frame = LabelFrame(root, text="Player B Score")
Computer_score_list_frame.pack(fill="both", padx=5, pady=5)

Computer_score = Label(Computer_score_list_frame)
Computer_score.pack(side="left", padx=5, pady=2)


# Play_A 리스트 프레임
Play_A_Score_list_frame = LabelFrame(root, text="Play_A")
Play_A_Score_list_frame.pack(fill="both", padx=5, pady=5, ipadx= 150)

scrollaber = Scrollbar(Play_A_Score_list_frame)
scrollaber.pack(side="right", fill= "y")

Play_A_Score_list_file = Listbox(Play_A_Score_list_frame, selectmode="extended", yscrollcommand=scrollaber.set)
Play_A_Score_list_file.pack(side="left", fill="both", expand=True)
scrollaber.config(command=Play_A_Score_list_file.yview)


# Computer 리스트 프레임
Computer_list_frame = LabelFrame(root, text="Computer")
Computer_list_frame.pack(fill="both", padx=5, pady=5, ipadx= 150)

scrollaber = Scrollbar(Computer_list_frame)
scrollaber.pack(side="right", fill= "y")

Computer_list_file = Listbox(Computer_list_frame, selectmode="extended", yscrollcommand=scrollaber.set)
Computer_list_file.pack(side="left", fill="both", expand=True)
scrollaber.config(command=Computer_list_file.yview)




# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="실행", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False,False)
root.mainloop()

