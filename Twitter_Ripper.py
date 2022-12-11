#twitter성인인증 우회기

import tkinter
from tkinter import *


def Openit():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    # 크롬 드라이버 자동 업데이트
    from webdriver_manager.chrome import ChromeDriverManager

    # 브라우저 꺼짐 방지
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)


    # 브라우저 기타 설정
    chrome_options.add_argument('incognito')
    chrome_options.add_argument('--start-maximized')


    # 불필요한 에러 로깅 끄기
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    tabs = driver.window_handles
 
    # TAB_1
    driver.switch_to.window(tabs[0])
    driver.get(f'{str(nitterlink)}')

    driver.switch_to.window(driver.window_handles[0])
    
    
def confirm():
    twitlink = userlink.get()
    
    if "twitter.com" in twitlink:
        global nitterlink
        nitterlink = twitlink.replace("twitter.com","nitter.net")
        
        Openit()
        
            
    else:
        print("Twitter.com의 링크가 아닌 것 같습니다! \nI think that this is a not twitter link!")



twitrip = tkinter.Tk()

twitrip.title("Twitter Ripper")
twitrip.geometry("350x180+900+430") #창크기 및 위치 지정 : 가로x세로+x축위치+y축위치 근데 기준이 뭔지 잘 모르겠음,,, ㅆㅂ
twitrip.resizable(False, False) #창 x방향 y방향 크기 조절 가능 여부 설정 (x, y)



label = tkinter.Label(twitrip, text = "'Twitter Ripper'에 오신 것을 환영합니다. \n 아래에 twitter.com주소를 붙여넣기 해주세요. \n Made By XiBBaL", height = 5)
label.place(x=50, y=4)

userlink = tkinter.Entry(twitrip, width=40)
userlink.place(x=32, y=80)

gobutton = tkinter.Button(twitrip, width=8, command = confirm, text= "Rip it!", borderwidth=2)
gobutton.place(x=142, y=120)

twitrip.mainloop()