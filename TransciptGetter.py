import wave, math, contextlib
import os
from moviepy.editor import AudioFileClip
# transcribed_audio_file_name = "transcribed_speech.wav"
# video_file_name = input("Enter the file name: ")
# audioclip = AudioFileClip(video_file_name)

from pydub import AudioSegment
import math

class SplitWavAudio():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_file(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
    def numsplit(self):
        total_mins = math.ceil(self.get_duration() / 60)
        return total_mins 
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        print(total_mins)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')

class SplitWavAudioSec():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_file(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec  * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
    def numsplit(self,seconds_per_split):
        total_seconds = math.ceil(self.get_duration())
        num=0
        for i in range(0, total_seconds, seconds_per_split):
            num=num+1
            if i == total_seconds - seconds_per_split:
                print('All splited successfully')
        return num
    def multiple_split(self, seconds_per_split):
        total_seconds = math.ceil(self.get_duration())
        num = 0
        print(total_seconds)
        for i in range(0, total_seconds, seconds_per_split):
            split_fn = str(num) + '_' + self.filename
            num+=1
            self.single_split(i, i+seconds_per_split, split_fn)
            print(str(i) + ' Done')
            
        print('All splited successfully')
