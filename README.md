Split the music files downloaded from YouTube into single audio files according to the playlist
## Build and Reploy
sh redeploy.sh

```
docker stop audio-processing
docker rm audio-processing
docker rmi audio-processing
docker build -t audio-processing .
docker run --rm --name audio-processing -v ./long_audio.mp3:/app/long_audio.mp3 -v ./play_list_file.txt:/app/play_list_file.txt -v ./output:/app/output audio-processing

```

## Process a long Audion file 
sh process.sh
```
docker run --rm --name audio-processing -v /Users/wing/long_audio.mp3:/app/long_audio.mp3 -v ./play_list_file.txt:/app/play_list_file.txt -v ./output:/app/output audio-processing
```



## Play list DEMO
Use two spaces to separate the time and song title, in order to be compatible with the format included in the song title

```
album  Best English Songs of 2023
comments  This album is awesome!
start  00:00
00:00  Don’t wanna know—Maroon 5
03:05  Flowers—Miley Cyrus
06:35  Easy on me—Adele
10:14  Work from home—Fifth harmony
12:41  Old town road—Lil Nas X
15:09  Anti-Hero—Taylor Swift
18:30  New Rules—Dua Lipa
21:58  Stylin’—Batchelor
25:10  Bad habits—Ed Sheeran
28:09  Dandelions—Ruth•B
32:06  Dusk till dawn—ZAYN ft.Sia
35:17  Shape of you—Ed Sheeran
38:37  Shivers—Ed Sheeran
42:05  Stay—The kid LAROI,Justin Bieber 
44:25  This is what you came for—Calvin harris,Rihanna
48:21  Peaches—Justin Bieber ft. Daniel Caesar, Giveon
50:48  see you again—Wiz Khalifa ft. Charlie Puth
53:38  Treat You better—Shawn Mendes
56:27  Old town road—Lil Nas X
58:56  Blinding lights—The weekend
1:01:04  unknow0
1:04:49  Monster—Katie Sky
1:06:14  2002–Anne-Marie
1:09:21  We don't talk anymore—Charlie Puth
1:12:21  What are words—Chris Medina
1:15:28  Bad liar—Imagine Dragons 
1:20:16  unknow1
1:23:20  Someone like you—Adele
1:30:19  Flowers—Miley Cyrus
end  1:33:33
```

![image info](./screenshot.jpg)