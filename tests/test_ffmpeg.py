from ffmpeg_python import ffmpeg_python
import os

def test_ffmpeg_python():
    text = "テストです。"
    output_dir = "outputs"
    path = ffmpeg_python(text, output_dir)
    assert os.path.exists(path)
    print(" 保存テスト成功！")
