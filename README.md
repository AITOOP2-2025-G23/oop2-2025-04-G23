# oop2-2025-04-G23

## リポジトリの目的
このリポジトリは、音声データを録音し、文字起こしを行い、その結果を保存する一連の処理を提供するPythonプログラムを管理するためのものです。以下の機能を実現します。

1. 音声録音
2. 音声データの前処理
3. 文字起こし
4. 文字起こし結果の保存

## 実行するのに必要なモジュール

- `numpy`: 音声データの数値処理
- `mlx_whisper`: Whisperモデルを使用した文字起こし
- `ffmpeg-python`: FFmpegを使用した音声録音

## 実行手順 (lecture04_main.pyで実行可能)
1. **音声録音**:
   - `ffmpeg-python.py` を実行して音声を録音する
   - 録音した音声ファイルは `python-audio-output.wav` として保存される

2. **音声データの前処理と文字起こし**:
   - `whisper＿python.py` を実行して音声データを前処理し、文字起こしを行う

3. **文字起こし結果の保存**:
   - `save.py` を実行して文字起こし結果を `transcription.txt` に保存する


## 作成者情報

- リーダー: 塚田渓太
- 作業者1: 岡村光莉
- 作業者2: 岩﨑陽大
- 作業者3: 近藤稟桜

## ディレクトリ構成
```
oop2-2025-04-G23/
├── README.md
├── lecture04_main.py
├── ffmpeg_python.py
├── whisper_python.py
|-- whisper_base-mlx
├── save.py
|-- python-audio-output.wav
|-- transcription.txt
└── tests/
    ├── test_ffmpeg.py
    ├── test_pydub.py
    └── test_save.py
```
