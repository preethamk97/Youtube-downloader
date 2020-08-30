# Youtube-downloader
From the given youtube video url you will be able to download the video in 720p format

sample output :-

Welcome to preethams youtube downloader program
Enter the folder to save (eg C:/Users/Preetham/) : 

C:/Users/Preetham/Desktop/

Enter the file name for the download file (eg: my_video) : https://www.youtube.com/watch?v=3yR2ebQpIDE

Enter the youtube video url : https://www.youtube.com/watch?v=3yR2ebQpIDE

Enter the format VIDEO or AUDIO : VIDEO
Downloading......
Downloaded  VIDEO  at  C:/Users/Preetham/Desktop/

Note:-
If you see any error while downloading :- 
 parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)

KeyError: 'cipher

go to extract.py and change the key "cipher" to signatureCipher.
