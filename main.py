import tkinter
import requests
from timeit import default_timer as timer

secs=60
rep=0
counter=None
start_time=0.0
def start_test():
    welcome_txt.destroy()
    go_btn.destroy()

    writeAble=True

    response=requests.get(url="https://random-word-api.vercel.app/api?words=25")
    response.raise_for_status()
    data=response.json()

    timer_txt=tkinter.Label(text="60 Seconds", fg="#F9EFDB", bg="#638889", font=("Arial",20))
    timer_txt.grid(row=0,column=0)

    display_txt=tkinter.Label(text=data,font=("Times New Roman",12,"italic"),padx=12,pady=12,bg="#638889",fg="#EBD9B4")
    display_txt.grid(row=1,column=0)

    def countdown(secs):
        global counter

        if secs>1:
            timer_txt.config(text=f"{secs} seconds")
        else:
            timer_txt.config(text=f"{secs} second")

        if writeAble:
            counter=window.after(1000, countdown, secs - 1)

    def keypress(event):
        global rep,counter

        key = event.char
        rep+=1

        if rep == 1:
            start_time = timer()
            counter=window.after(1000, countdown, secs - 1)
            window.after(60000, stop_test)

    def stop_test():
        global counter,start_time

        end_time=timer()
        window.after_cancel(counter)
        timer_txt.destroy()
        display_txt.destroy()
        btn1.destroy()

        total_keys=len(txt.get("1.0","end-1c"))
        txt.destroy()

        words=total_keys/5
        time_elapsed=end_time-start_time
        minutes=time_elapsed/60
        wpm=words/minutes
        wpm="{:.2f}".format(wpm)

        def restart():
            global rep

            result.destroy()
            btn_retry.destroy()

            rep=0
            start_test()

        result=tkinter.Label(text=f"{wpm} WPM",font=("Arial",30,"bold"),bg="#638889",fg="#F9EFDB",padx=10,pady=10)
        result.grid(row=0,column=0)
        btn_retry=tkinter.Button(text="Retry",padx=10,pady=10,font=("Arial",12),command=restart,bg="#EBD9B4",fg="black")
        btn_retry.grid(row=1,column=0)

    window.bind("<Key>", keypress)

    txt=tkinter.Text(width=80,height=2, bg="white",fg="black")
    txt.grid(row=2,column=0)

    btn1=tkinter.Button(text="Done",font=("Arial",12),command=stop_test,padx=10,pady=10,bg="#EBD9B4",fg="black")
    btn1.grid(row=3,column=0,padx=10,pady=10)

window=tkinter.Tk()
window.config(width=450,height=200,bg="#638889",padx=20,pady=20)
window.title("")
welcome_txt=tkinter.Label(text="Welcome To Speed Typing Test",font=("Arial",20,"bold"),bg="#638889",fg="#F9EFDB",padx=10,pady=10)
welcome_txt.grid(row=0,column=0)

go_btn=tkinter.Button(text="Go",bg="#EBD9B4",fg="black",padx=10,pady=10,width=12,font=("Arial",12),command=start_test)
go_btn.grid(row=1,column=0)

window.mainloop()