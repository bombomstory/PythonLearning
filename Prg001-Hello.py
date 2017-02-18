#Program name: Prg001-Hello.py
#This program looks like the expert system, you can talk with this computer.
#How to run this program:
#In MS-DOS prompt, you should type: python name.py your_name
#For example : python exam3_1.py Paitoon
#Version 1.0
#Written by Mr.Paitoon Thipsanthia
#GNU License : You can modify and publish this software everywhere

import sys
if len(sys.argv) == 2:
    if sys.argv[1] != '':
        print("คอมพิวเตอร์: สวัสดีครับ ผมชื่อไพธอน!!!")
        print("คอมพิวเตอร์: คุณ", sys.argv[1], " เป็นอย่างไรบ้างครับวันนี้")
        feeling = input("คุณ: ผมรู้สึก ")
        print("คอมพิวเตอร์: โอ้!! คุณรู้สึก", feeling, "!!")
        print("คุณ: แล้วไพธอนล่ะ เป็นไงบ้าง")
        print("คอมพิวเตอร์: เยี่ยมมากครับ!!")
    else:
        print("คอมพิวเตอร์: ผมไม่คุยกับคนแปลกหน้า กรุณาระบุ argv หลังชื่อโปรแกรมด้วยครับ")
