# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:16:44 2020

@author: Preetham
"""
try :    
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Modules in the pytube are missing{}".format(e))

print("\n*****************Welcome to preethams youtube downloader program*****************\n")

def download_the_video():
    print("Enter the folder to save (eg C:/Users/Preetham/) : ")
    SAVE_PATH = input()
    file_name = input("Enter the file name for the download file (eg: my_video) : ")
    url = input("Enter the youtube video url : ")
    ytd = YouTube(url)
    t_type = input("Enter the format VIDEO or AUDIO : ")
    if(t_type=="VIDEO") :
        print("Downloading......")
        ytd.streams.filter(progressive=True,file_extension ='mp4').order_by('resolution').desc().first().download(SAVE_PATH,file_name,"PK_")
        
    if(t_type=="AUDIO") :
        print("Downloading......")
        ytd.streams.filter(only_audio=True).first().download(SAVE_PATH,file_name,"PK_")
   
    print("Downloaded ",t_type," at ",SAVE_PATH)


download_the_video() 
