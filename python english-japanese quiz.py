# -*- coding: utf-8 -*-
"""第七回課題.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N6EFmFzKgAz2qJER9HZjNT46iDwICCtw
"""

import random
import time

Dictionary = { 
'autonomous': '自治の，自立した，自主的な',
'autopsy':'米》検死，死体解剖',
'auxiliary':'補助の，補助的な ｜ 補助者',
'avid':'熱心な，貪欲な',
'blurb':'宣伝文',
'bogus':'偽の，いんちきの',
'bolster':'支持する，支える ｜ 長枕',
'bombard':'爆撃する，（質問などで）攻め立てる',
'bona fide':'真実の，正真正銘の',
'bourgeois':'中産階級の',
'brandish':'（剣など）を振り回す，振りかざす',
'cartilage':'軟骨',
'cash in on':'～に乗じる，を利用する',
'categorical':'断言的な，明確な',
'causative':'原因となる，《文法》使役の',
'celestial':'天の，天上の，神々しい',
'chasten':'懲らしめる',
}


for i in range(10):
    en = random.choice(list(Dictionary.keys()))
    jp = Dictionary[en]
    print(en)
    time.sleep(4)
    print('Answer: '+jp)
    time.sleep(2)