#A cada 10 seg abre um link no browser
import webbrowser
import time

total_breaks = 3
break_count=0

print("Aguarde, timer executando:"+time.ctime())
while(break_count < total_breaks):
        time.sleep(10)
        
        if break_count==0:
                s="https://youtu.be/CsGYh8AacgY?t=4"
        elif break_count==1:
                s="https://youtu.be/KaqC5FnvAEc?t=14"
        elif break_count==2:
                s="https://www.youtube.com/watch?v=ZZ5LpwO-An4"


        webbrowser.open(s)
        #https://youtu.be/KaqC5FnvAEc?t=14
        #https://www.youtube.com/watch?v=ZZ5LpwO-An4
        break_count = break_count+1
