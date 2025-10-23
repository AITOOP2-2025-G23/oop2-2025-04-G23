import os
from datetime import datetime

def ffmpeg_python(text: str, output_dir: str = "outputs") -> str:
    """
    文字起こし結果をテキストファイルとして保存する（上書きしない）。

    Parameters
    ----------
    text : str
        文字起こしされた文字列。
    output_dir : str, optional
        保存先ディレクトリ（デフォルト: "outputs"）

    Returns
    -------
    str
        保存したファイルのパス。
    """
    # 保存先ディレクトリが存在しなければ作成
    os.makedirs(output_dir, exist_ok=True)

    # 重複しないファイル名を作成（日時＋連番）
    base_name = datetime.now().strftime("transcript_%Y%m%d_%H%M%S")
    file_path = os.path.join(output_dir, f"{base_name}.txt")
    counter = 1

    while os.path.exists(file_path):
        file_path = os.path.join(output_dir, f"{base_name}_{counter}.txt")
        counter += 1

    # テキストを書き込み
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"文字起こし結果を保存しました: {file_path}")
    return file_path

if __name__ == "__main__":
    # テスト用の文字起こしテキスト
    test_text = "これはテスト保存です。"
    ffmpeg_python(test_text)

