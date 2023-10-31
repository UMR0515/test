import os
#連結歌單
music = ['0:abc','1:cba','2:qwe']
list = ['https://youtu.be/GC1igLEsa8I?si=_20h9b2zK78TXzWF','https://youtube.com/playlist?list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&si=BHIPDd7C0_1w_vd2','https://youtu.be/bLRa4TZ99aY?si=ScpxWLDKdPCW4CMz']
print(music)

user_data = input('第幾首:')
user_data = int(user_data)

print(music[user_data])
if user_data == 0:
    os.system('start '+list[0])
elif user_data == 1:
    os.system('start '+list[1])
else:
    os.system('start '+list[2])
