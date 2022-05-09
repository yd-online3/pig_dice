
import tkinter # pip install tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * 
# 파일 찾는 창을 뛰우는 기능
from tkinter import filedialog # 서브 모듈은 따로 import를 해줘야 사용가능
from PIL import Image #pip install pillow


root = Tk()
root.title("Pig Game")

# A 폴더는 있고 B 폴더에는 없는 파일 찾기
def compare_files(Adir_R,Bdir_R):
    pass
    

# -----------버튼 함수-------------
# 폴더 선택
def dice():
    pass

# 비교 버튼
def stop():
    pass
    
# 시작
def start():    
    pass



# 파일 프레임 
file_frame = Frame(root)
file_frame.pack(fill= "x", padx=5, pady=5 ) #가로로 넓게

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="주사위를 굴린다", command=dice)
btn_add_file.pack(side="left")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="주사위를 멈춘다.", command=stop)
btn_add_file.pack(side="left")

# 리스트 프레임 A폴더
Adir = LabelFrame(root, text="Player A Score")
Adir.pack(fill="both", padx=5, pady=5)

Adir_Route = Entry(Adir) # 한줄일때 Entry
Adir_Route.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

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