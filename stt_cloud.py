import os
from google.cloud import speech
from moviepy.editor import AudioFileClip

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json' #to use the speech to text api.
#https://www.youtube.com/watch?v=lKra6E_tp5U useful link.
speech_client = speech.SpeechClient()

transcribed_audio_file_name = "transcribed_speech.wav"
video_file_name = input("Enter the file name: ") #Takes the MP4 file name as input.
audioclip = AudioFileClip(video_file_name) 
audioclip.write_audiofile(transcribed_audio_file_name) #Creates the wav file
# Transcribe Local Media File 
# File Size: < 10mbs, length < 1 minute
# Step 1. Load the media files

media_file_name_wav = 'transcribed_speech.wav' #the wav that we created was called transcribed_speech.wav


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

print(response_standard_wav)


# Transcribing a long media file

#enter the uri to the larger file after uploading to cloud bucket.


# media_uri = ''
# long_audi_wav = speech.RecognitionAudio(uri=media_uri)

# config_wav_enhanced = speech.RecognitionConfig(
#     sample_rate_hertz=48000,
#     enable_automatic_punctuation=True,
#     language_code='en-US',
#     use_enhanced=True,
#     model='video'
# )

# operation = speech_client.long_running_recognize(
#     config=config_wav,
#     audio=long_audi_wav
# )
# response = operation.result(timeout=90)
# print(response)

# for result in response.results:
#     print(result.alternatives[0].transcript)
#     print(result.alternatives[0].confidence)
#     print()