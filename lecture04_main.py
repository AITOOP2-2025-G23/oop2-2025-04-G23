import subprocess
import pydub_python
import save

def ffmpeg_python():
    # ffmpeg_python.py を呼び出して音声を録音
    subprocess.run(["python", "ffmpeg_python.py"], check=True)

def whisper_python():
    # pydub_python.py を呼び出して音声データを前処理し、文字起こし
    transcription = pydub_python.process_audio("recorded_audio.wav")
    return transcription

def save_transcription(transcription):
    # save.py を呼び出して文字起こし結果を保存
    save.save_to_file(transcription, "transcription.txt")

if __name__ == "__main__":
    print("音声録音を開始します...\n")
    ffmpeg_python()
    
    print("音声データを処理しています...\n")
    transcription = whisper_python()

    print("文字起こし結果を保存しています...\n")
    save_transcription(transcription)
    
    print("処理が完了しました！")