import mlx_whisper

def whisper_python(audio_file_path: str) -> str:
    # 音声ファイルを指定して文字起こし
    result = mlx_whisper.transcribe(
        audio_file_path, path_or_hf_repo="whisper-base-mlx"
    )
    
    return result["text"]

print(whisper_python("python-audio-output.wav"))