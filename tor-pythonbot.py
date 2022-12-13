import time
import os, signal
import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
import webbrowser

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

print("Youtube ViewBot v0.1")
print("Changing IP Address for every video play....\n")

def killprocess():
     
    # Ask user for the name of process
    name = "opera"
    try:
         
        # iterating through each instance of the process
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()
             
            # extracting Process ID from the output
            pid = fields[0]
             
            # terminating process
            os.kill(int(pid), signal.SIGKILL)
        print("Process Opera Successfully terminated")
         
    except:
        print("Error Encountered while running script")
  
it = 1
while True:
    headers = { 'User-Agent': UserAgent().random }
    time.sleep(1)
    with Controller.from_port(port = 9051) as c:
        c.authenticate('welcome')
        c.signal(Signal.NEWNYM)
        time.sleep(5)
        print("Iteration : ", it , end=' * ')
        #webbrowser.open('https://api64.ipify.org?format=json')
        webbrowser.open('https://www.youtube.com/watch?v=YQyXZYxb85Q')
        time.sleep(5)
        webbrowser.open('https://www.youtube.com/watch?v=amJkNmVGXhg')
        print(f"IP : {requests.get('https://ident.me', proxies=proxies, headers=headers).text}", end =' * ')
        time.sleep(140)
        killprocess()
        it = it + 1