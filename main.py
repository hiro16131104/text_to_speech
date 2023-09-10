from datetime import datetime

# オリジナルのクラスをインポート
from models.text_to_speech import TextToSpeech


# 外部ファイルのテキストから音声ファイルを生成する
def create_audio_from_file(input_path: str, output_path: str) -> None:
    text2speech = TextToSpeech()

    # 外部ファイルからテキストを取得する
    text2speech.get_text_from_file(input_path)
    # 音声ファイルを生成する
    text2speech.create_audio_file(output_path)


if __name__ == "__main__":
    # 出力ファイル名を現在時刻から生成する
    datetime_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    input_file: dict[str, str] = {}
    output_file: dict[str, str] = {}

    # 入力ファイルの名前はユーザーが指定する
    input_file["name"] = input("入力ファイルの名前を入力してください: ")
    input_file["path"] = f"./resources/input/{input_file['name']}"
    output_file["name"] = f"{datetime_str}_output.mp3"
    output_file["path"] = f"./resources/output/{output_file['name']}"

    # 外部ファイルからテキストを取得し、音声ファイルを生成する
    create_audio_from_file(input_file["path"], output_file["path"])
