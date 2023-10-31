import os
#連結歌單
music = ['0:abc','1:cba','2:qwe'] 
print(music)

user_data = input('第幾首:')
user_data = int(user_data)

print(music[user_data])
if user_data == 0:
    os.system('start https://youtu.be/FMruNSjHOzQ?si=WAGXeaYkz9a2kHxd')
elif user_data == 1:
    os.system('start https://youtu.be/JLU5oc4_VtA?si=Dd1psrw7npfDCyGH')
else:
    os.system('start https://youtu.be/bLRa4TZ99aY?si=ScpxWLDKdPCW4CMz')
