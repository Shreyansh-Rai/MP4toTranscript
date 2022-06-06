import os
from os import path
from moviepy.editor import AudioFileClip
def fn():
    file_list=os.listdir(r"D:\Internships\MPL_PR\VideoFolder") #change to your directory
    return file_list
l = fn()
count = 1
for v in l :
    # files
    if(v[len(v)-3:len(v)] != 'mp4') :
        continue
    src = v
    dst = 'vid'+str(count)+ v[len(v)-4:len(v)-1] + '3'
    count= count +1
    audioclip = AudioFileClip(src) 
    audioclip.write_audiofile(dst)
    # convert mp3 to wav
#The file nomenclature is vid1 vid2 vid3.mp3 and so on for automation of stt in cloud