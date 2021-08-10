#개발자 wau2380(박이정)

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import schedule
driver = webdriver.Chrome('')
URL="https://asked.kr/"
driver.get(URL)

def ask_login():
    ID = '#'
    PassWord = '#'
    login = driver.find_element_by_name("id") # 로그인 
    login.send_keys(ID)
    login = driver.find_element_by_name("pw")
    login.send_keys(PassWord) 
    login.send_keys(Keys.ENTER) #로그인
def ask_new_question(): #질문 모아오기
    new_ask_number= driver.find_element_by_id("new_count")#새질문 갯수 구하기  
    counts = int(new_ask_number.text) #정수로 전환
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
    time.sleep(1) # 한턴 쉬고
    ask_new()
    Count=ask_new_question()

    while Count!=0:
        for i in range(0,Count+1): #정수로 변환
            answer = driver.find_elements_by_class_name("card_ask")[0]#질문 불러오기
            answer_contents.append(answer.text)#문자열 전환
            
            if any( '키워드' in s for s in answer_contents): #특정 키워드 겹치는 질문 구별하기
                elem = driver.find_elements_by_class_name("ask_answer_btn")[0].send_keys(Keys.ENTER)
                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'input_answer'))) #요소보일때까지 기다리기
                elem = driver.find_elements_by_class_name("input_answer")[0].send_keys('대답')#대답창 
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


