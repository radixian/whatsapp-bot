# -*- coding: UTF-8 -*-
import time
import sys
import pyautogui
import subprocess

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

flg = -1
countPass = 0
countFail = 0
countX = 0
name = 'no-one'

try:
    inputFile = open(r"input\input.txt","r")
    print("File Opened Successfully!")
except Exception as e:
    print("Input File not accessible, Program Ends")
    sys.exit()

try:
    outputFile = open(r"output\output.txt","r")
    print("Another Output File Exists, Closing Program")
    sys.exit()
except IOError:
    outputFile = open(r"output\output.txt","w")
except Exception as e:
    print("File not accessible, Program Ends")
    outputFile.close()
    inputFile.close()

chrome_browser = webdriver.Chrome(executable_path=r"driver\chromedriver.exe")
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(60)

for user_name in inputFile.readlines():

    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_1MdKA w-vsN"]')
    new_chat.click()

    new_user = chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name.strip())

    time.sleep(2)

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name.strip()))
        user.click()

    except NoSuchElementException:        
        countFail += 1
        flg = 0
        name = user_name.strip()
        outputFile.write('{},{}\n'.format(name.strip('P'),flg))
        print('{},{}'.format(user_name.strip(),flg))
        continue

    except Exception as e:
        chrome_browser.close()
        print('Whole Program cannot continue!')
        sys.exit()

    try:    
        
        clipButton = chrome_browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
        clipButton.click()

        time.sleep(1)

        docButton = chrome_browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]')
        docButton.click()

        time.sleep(2)

        subprocess.Popen(r'script\script.exe')

        time.sleep(4)
        send_button = chrome_browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
        send_button.click()


        message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
        
        message_box.send_keys(' අග්‍රාමාත්‍ය ගරු xxxx xxxx මැතිතුමන්ගේ මාධ්‍ය ප්‍රකාශක, සත්‍යය ගවේෂකයෝ සංවිධානයේ නිර්මාතෘ, කොළඹ 7 - *ඩී. එස්. සේනානායක විද්‍යාලයේ* ආදී ශිෂ්‍ය හා බෞදධ සංගමයේ හිටපු සභාපති, නීතීඥ *xxxx x. xxxx* මහතාගේ, *අංක 15 - පොහොට්ටුව* කොළඹ දිස්ත්‍රික් මැතිවරණ ව්‍යාපාරයේ, ජය තහවුරු  කරන සේනානායකීය ආදි ශිෂ්‍ය වට්ස්ඇප් සමූහයට එකතු වීමට +xxxxxxxxxx  අංකය ඔබගේ ජං. දු. save කර පහත link එක ඔබන්න.')
        pyautogui.hotkey('shift','enter')
        message_box.send_keys(' ')
        pyautogui.hotkey('shift','enter')
        message_box.send_keys(' https://chat.whatsapp.com/GzmmScFved59USd8IYLY4F')

        #include the code here*****
        send_button.click()
        

        countPass += 1
        flg = 1
        name = user_name.strip()
        outputFile.write('{},{}\n'.format(name.strip('P'),flg))
        print('{},{}'.format(user_name.strip(),flg))
    
    except Exception as e:
        print('{},x'.format(user_name.strip()))
        name = user_name.strip()
        outputFile.write('{},x\n'.format(name.strip('P'),flg))
        countX += 1
        continue

    flg = -1

print('Program Executed Successfully, with "{}" already exists, "{}" Pass and "{}" Fail'.format(countX, countPass, countFail))
outputFile.close()
inputFile.close()
#time.sleep(10)
#chrome_browser.close()
