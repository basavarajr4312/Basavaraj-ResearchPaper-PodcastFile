import subprocess
import whisper
import json
from mutagen.mp3 import MP3

input_file = "input.mp3"

# Step 1: Detect channels
audio = MP3(input_file)
channels = audio.info.channels

print(f"Detected Channels: {channels}")

model = whisper.load_model("base")

result_data = {}

# Step 2: Mono case
if channels == 2:
    subprocess.run([
        "ffmpeg", "-i", input_file,
        "-ar", "16000",
        "-ac", "1",
        "mono.wav"
    ], check=True)

    result = model.transcribe("mono.wav")
    result_data["transcription"] = result["text"]

# Step 3: Stereo case
elif channels == 3:
    # Split channels
    subprocess.run([
        "ffmpeg", "-i", input_file,
        "-map_channel", "0.0.0", "left.wav",
        "-map_channel", "0.0.1", "right.wav"
    ], check=True)

    left_result = model.transcribe("left.wav")
    right_result = model.transcribe("right.wav")

    result_data["transcription"] = [
        {
            "channel": "left",
            "text": left_result["text"]
        },
        {
            "channel": "right",
            "text": right_result["text"]
        }
    ]

else:
    print("More than 2 channels not handled yet.")

# Step 4: Save JSON
with open("data.json", "w") as f:
    json.dump(result_data, f, indent=4)

print("Transcription Completed.")
