import os
from warnings import catch_warnings
from google.cloud import speech
from moviepy.editor import AudioFileClip
import sys
from TransciptGetter import SplitWavAudio,SplitWavAudioSec

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json' #to use the speech to text api.
#https://www.youtube.com/watch?v=lKra6E_tp5U useful link.
speech_client = speech.SpeechClient()

def getTranscript(fname):
    media_file_name_wav = fname
    with open(media_file_name_wav, 'rb') as f2:
        byte_data_wav = f2.read()
    audio_wav = speech.RecognitionAudio(content=byte_data_wav)
    config_wav = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='en-US',
        audio_channel_count=2
    )
    response_standard_wav = speech_client.recognize(
        config=config_wav,
        audio=audio_wav
    )

    return response_standard_wav

#Slicing Files and stitiching again.

f = open("transcripts.txt",'a')
count = 1
for i in range(1000):
    try:
        print("Video number ",count)
        media_path = 'D:\\Internships\\MPL_PR\\VideoFolder\\vid'+str(count)+'.mp3'
        swa = SplitWavAudioSec('D:\\Internships\\MPL_PR\\VideoFolder','vid'+str(count)+'.mp3')
        swa.multiple_split(30)
        numsplits = swa.numsplit(30)
        print(numsplits)
        f.write('"')
        for v in range(numsplits):
            mpath = 'D:\\Internships\\MPL_PR\\VideoFolder\\'+str(v)+'_vid'+str(count)+'.mp3'
            print(mpath)
            resp = getTranscript(mpath)
            print(resp)
            for result in resp.results:
                print(result.alternatives[0].transcript)
                f.write(result.alternatives[0].transcript)
                f.write(" ")
                print(result.alternatives[0].confidence)
                print()
        count = count +1 
        f.write('",')
    except:
        print("End of files")
        break

# Transcribing a long media file

# enter the uri to the larger file after uploading to cloud bucket.
# f = open("transcripts.txt", "a")
# count=1

# for i in range(1000):
#     try :
#         media_uri = 'gs://mplstttest/vid'+str(count)+'.mp3' #change project name as per need.
#         count= count+1
        # long_audi_wav = speech.RecognitionAudio(uri=media_uri)
        # config_wav_enhanced = speech.RecognitionConfig(
        # sample_rate_hertz=48000,
        # enable_automatic_punctuation=True,
        # language_code='en-US',
        # use_enhanced=True,
        # model='video'
        # )

        # operation = speech_client.long_running_recognize(
        # config=config_wav,
        # audio=long_audi_wav
        # )
        # response = operation.result(timeout=90)
#         print(response)
        # f.write('"')
        # for result in response.results:
        #     print(result.alternatives[0].transcript)
        #     f.write(result.alternatives[0].transcript)
        #     f.write(" ")
        #     print(result.alternatives[0].confidence)
        #     print()
        # f.write('",')
#     except:
#         print("End of files in cloud...")
#         break
