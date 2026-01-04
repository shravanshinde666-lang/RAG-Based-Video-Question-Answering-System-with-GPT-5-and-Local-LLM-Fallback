import whisper
import os

print("Loading model...")
model = whisper.load_model("base")
print("Model loaded ✅")

audio_dir = "audios"
output_dir = "transcripts"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(audio_dir):
    if not file.endswith(".mp3"):
        continue

    print(f"\nTranscribing: {file}")

    audio_path = os.path.join(audio_dir, file)
    result = model.transcribe(audio_path, language="en")

    txt_name = file.replace(".mp3", ".txt")
    txt_path = os.path.join(output_dir, txt_name)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Saved → {txt_name}")

print("\n🎉 ALL FILES TRANSCRIBED SUCCESSFULLY")
