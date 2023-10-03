import json
from pydub import AudioSegment


file_path = "play_list_file.txt"  # 替换为实际文件路径

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

# 将最后一个 JSON 对象的结束时间赋值为播放列表文件中的最后一个结束时间
if jsondata:
    jsondata[-1]["end"] = end_time
#print(jsondata[0])


audio = AudioSegment.from_file("long_audio.mp3", format="mp3")

# 将音频文件按照播放列表分割
for i in range(0,len(jsondata)):
    print(jsondata[i])
    start_time = jsondata[i]["start"]
    end_time = jsondata[i]["end"]
    title = jsondata[i]["title"]

    start = (int(start_time.split(":")[0]) * 3600 + int(start_time.split(":")[1]) * 60 + int(start_time.split(":")[2])) * 1000
    end = (int(start_time.split(":")[0]) * 3600 + int(end_time.split(":")[1]) * 60 + int(end_time.split(":")[2])) * 1000

    # 分割音频文件
    track_audio = audio[start:end]
    #print(f"/app/output/Track_{i+1}_{title}.mp3")
    # 保存分割后的音频文件
    track_audio.export(f"/app/output/Track_{i+1}_{title}.mp3", format="mp3", tags={'artist': title , 'album': album, 'comments': comments})