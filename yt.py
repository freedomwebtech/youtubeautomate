from apiclient.discovery import build 
import subprocess
#import speech_recognition as sr


#api_key = "AIzaSyDXbwWlSfWuT0NwDSvMeli3jMKfv-WskMI"

#api_key = "your api key"
youtube = build('youtube','v3', developerKey = api_key)
 

s = "Mountkid - Jellyfish Party [NCS Release]"


#print (youtube)


#request = youtube.search().list(q='Countless Storeys',part='snippet',type='video')
a = youtube.search().list(q= s,part='snippet',type='audio', maxResults=1)






res = a.execute()

from pprint import PrettyPrinter
pp = PrettyPrinter()
pp.pprint(res)

print (res)

#for item in res['items']:
#    a=(item['id']['videoId'])
   


#print (a)



#p1 = subprocess.run(['youtube-dl','-q', '-o-', a], capture_output=True)


#p2 = subprocess.run(['mplayer','-cache', '8192',  '-'],
#                      capture_output=True, input=p1.stdout)

