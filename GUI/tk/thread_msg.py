import tkinter as tk
from tkinter import ttk
import time
from threading import Thread

from queue import Queue
from enum import Enum, auto

class TKMessageType(Enum):
    UPDATE_PROGRESS_TYPE = auto()  ## auto just crate a value
    EXIT_TYPE = auto()

class TKMessage:
    def __init__(self, msg_type : TKMessageType, msg_value: str) -> None:
        self.msg_type = msg_type
        self.msg_value = msg_value

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.create_widget()
        self.queue_msg = Queue()
        self.bind( "<<CheckMsgQ>>" , self.check_queue)

    def check_queue(self, event):
        msg: TKMessage

        msg = self.queue_msg.get()
        if msg.msg_type == TKMessageType.UPDATE_PROGRESS_TYPE:
            self.label_msg.configure(text = msg.msg_value)

    def create_widget(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True)

        self.btn_exit = ttk.Button(self.main_frame, text="Exit", command=self.destroy) 
        self.btn_exit.pack(pady=10,) 

        self.label_msg = ttk.Label(self.main_frame)
        self.label_msg.pack(padx=15)

        self.btn_download = ttk.Button(self.main_frame, text = "Donwload", command= self.on_download_click)
        self.btn_download.pack(pady=10)

        self.progressbar = ttk.Progressbar(self.main_frame, orient=tk.HORIZONTAL,length=100,mode="determinate")
        self.progressbar.pack(padx=25, pady=20, side=tk.LEFT)

        self.label_progress = ttk.Label(self.main_frame)
        self.label_progress.pack(padx=5, side=tk.LEFT)

    def on_download_click(self):
        d_thread = Thread(target=self.downlad_file, args=("report.csv",), daemon = True)
        d_thread.start()
        self.progressbar.configure(maximum=5)
        self.progressbar.step(1)

        self.label_msg.configure(text = "")

    def downlad_file(self, file_name: str):
        for p in range(1, 6):
            self.label_progress.configure(text = f"Downloading {file_name}  {p * 20}% .....", foreground="green" )
            self.progressbar['value'] = p
            ticket = TKMessage(msg_type=TKMessageType.UPDATE_PROGRESS_TYPE, msg_value= f"Downloading {file_name} at {p * 20}% ....." ) 
            self.queue_msg.put(ticket)
            time.sleep(1)
            self.event_generate("<<CheckMsgQ>>")

        self.label_progress.configure(text = f"Downloading {file_name}  completed", foreground="black")    

        ticket = TKMessage(msg_type=TKMessageType.EXIT_TYPE, msg_value= f"Downloading {file_name}  completed after 5 seconds" ) 
        self.queue_msg.put(ticket)

        self.event_generate("<<CheckMsgQ>>", when="tail")  ## make sure this is the last message


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()

