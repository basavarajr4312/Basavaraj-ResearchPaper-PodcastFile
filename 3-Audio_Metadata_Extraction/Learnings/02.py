from mutagen.mp3 import MP3
import json

audio = MP3("podcast.mp3")

result={}

# print(audio.__doc__)

# print(audio.info.__doc__)

result["length"] = audio.info.length
result["Bitrate"]= audio.info.bitrate
result["Sample rate"] = audio.info.sample_rate
result["channels"] = audio.info.channels
result["encoder_info"] = audio.info.encoder_info
result["encoder_settings"] = audio.info.encoder_settings
result["bitrate_mode"] = audio.info.bitrate_mode
result["track_gain"] = audio.info.track_gain
result["track_peak"] = audio.info.track_peak
result["album_gain"] = audio.info.album_gain

print(audio.tags.__doc__)
result["version"] = audio.tags.version
result["size"] = audio.tags.size
result["frames"] = audio.tags.unknown_frames

print(result)

for key in result:
    print(f"{key} : {result[key]}")

with open("data.json",'w') as f:
    json.dump(result, f)