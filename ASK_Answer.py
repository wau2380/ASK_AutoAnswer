'''

ASK_AutoAnswer(KR_School) - Python
Copyright 2021 yijung park(wau2380) All Rights Reserved.

https://github.com/wau2380

본 프로그램의 사용으로 발생한 문제에 대해서는 책임을 지지 않습니다.

위에 규칙에 동의하신다면, False를 True 로 변경해 주세요.

Agree = False
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('')
URL="https://asked.kr/"
driver.get(URL)

def ask_login(): #로그인
    ID = '#' #아이디를 입력해주세요
    PassWord = '#' #패스워드를 입력해 주세요
    login = driver.find_element_by_name("id") 
    login.send_keys(ID)
    login = driver.find_element_by_name("pw")
    login.send_keys(PassWord) 
    login.send_keys(Keys.ENTER) 
def ask_new_question(): #질문 모아오기
    new_ask_number= driver.find_element_by_id("new_count")
    counts = int(new_ask_number.text) 
    return counts
def ask_new(): #새질문 클릭
    elem = driver.find_elements_by_class_name("a_child")[1]
    elem.click()
def Sleep_05(): #쉬기
    time.sleep(0.5)
def 팝업창_처리(): 
    time.sleep(1)
    팝업창 = Alert(driver)
    팝업창.accept()
    Sleep_05()
def Refresh_web(): #새로고침
    driver.refresh()
    time.sleep(3)

answer_contents=[]

try:
    ask_login()
    time.sleep(1)
    ask_new()
    Count=ask_new_question()

    while Count!=0:
        for i in range(0,Count+1): #정수로 변환
            answer = driver.find_elements_by_class_name("card_ask")[0]#질문 불러오기
            answer_contents.append(answer.text) #문자열 전환
            
            if any( '키워드' in s for s in answer_contents): #특정 키워드 겹치는 질문 구별하기
                elem = driver.find_elements_by_class_name("ask_answer_btn")[0].send_keys(Keys.ENTER)
                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'input_answer'))) 
                elem = driver.find_elements_by_class_name("input_answer")[0].send_keys('대답') 
                elem = driver.find_elements_by_class_name("ask_asnwer_bottom_btn")[0]
                Sleep_05()
                elem.send_keys(Keys.ENTER)
                팝업창_처리()
                Refresh_web()
                Count=Count-1
           
            else:
                elem = driver.find_elements_by_class_name("reject_btn")[i].send_keys(Keys.ENTER)
                팝업창_처리()
                Refresh_web()
                Count=Count-1   
                
except:
    print("오류 발생")


