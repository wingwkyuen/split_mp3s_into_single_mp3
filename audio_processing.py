import json
import time
from pydub import AudioSegment


file_path = "./play_list_file_2.txt" 

jsondata = []
playlist = []
is_start = False
end_time = ""
album = ""
comments = ""

with open(file_path, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line.startswith("start"):
        is_start = True
    elif line.startswith("album"):
        album = line.split("  ")[1]
    elif line.startswith("comments"):
        comments = line.split("  ")[1]        
    elif line.startswith("end"):
        is_start = False
        end_time = line.split("  ")[1]
    elif line and is_start:
        parts = line.split("  ", maxsplit=1)
        if len(parts) > 1:
            start_time = parts[0]
            if len(start_time)<6:
                start_time="0:"+start_time
            title = parts[1].strip()
            jsondata.append({"start": start_time, "end": "", "title": title})
            jsondata[len(jsondata)-2]["end"] = start_time

if jsondata:
    jsondata[-1]["end"] = end_time
print(jsondata[0])


audio = AudioSegment.from_file("../../long_audio_2.mp3", format="mp3")

for i in range(0,len(jsondata)):
    print(jsondata[i])
    start_time = jsondata[i]["start"]
    end_time = jsondata[i]["end"]
    title = jsondata[i]["title"]

    start = (int(start_time.split(":")[0]) * 3600 + int(start_time.split(":")[1]) * 60 + int(start_time.split(":")[2])) * 1000
    end = (int(end_time.split(":")[0]) * 3600 + int(end_time.split(":")[1]) * 60 + int(end_time.split(":")[2])) * 1000
    track_audio = audio[start:end]
    print(f"/app/output/{i+1}_{title}.mp3")

    track_audio.export(f"./output/{i+1}_{title}.mp3", format="mp3", tags={'artist': title , 'album': album, 'comments': comments})
    time.sleep(5)