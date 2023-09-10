import chardet
from langdetect import detect
from gtts import gTTS
from gtts.lang import tts_langs


class TextToSpeech:
    # Google Text-to-Speech APIのサポート言語と文字コード
    SUPPORTED_ENCODINGS: list[str] = ["utf-8", "iso-8859-1", "shift_jis", "euc-jp"]
    SUPPORTED_LANGUAGES: dict = tts_langs()

    def __init__(self, text: str = "") -> None:
        self.text = text

    # 外部ファイルの文字コードを判定する
    def __detect_encoding(self, file_path: str) -> str:
        with open(file_path, "rb") as file:
            result = chardet.detect(file.read())
            return result["encoding"]

    # テキストの言語を判定する
    def __detect_language(self) -> str:
        return detect(self.text)

    # 文字コードがサポートされているかを検証する
    def __validate_encoding(self, encoding: str) -> None:
        if encoding.lower() not in self.SUPPORTED_ENCODINGS:
            raise ValueError(f"この文字コードはサポートされていません: {encoding}")

    # 言語がサポートされているかを検証する
    def __validate_language(self, language: str) -> None:
        if language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"この言語はサポートされていません: {language}")

    # 外部ファイルからテキストを取得する
    def get_text_from_file(self, file_path: str) -> None:
        # 外部ファイルの文字コードを判定する
        encoding = self.__detect_encoding(file_path)

        # 文字コードがサポートされているかを検証する
        self.__validate_encoding(encoding)
        # 外部ファイルを読み込み、テキストを取得する
        with open(file_path, "r", encoding=encoding) as file:
            self.text = file.read()

    # テキストから音声を生成し、mp3ファイルとして保存する
    def create_audio_file(self, file_path: str) -> None:
        # テキストの言語を判定する
        language = self.__detect_language()
        text2speech: gTTS = None

        # 言語がサポートされているかを検証する
        self.__validate_language(language)
        # テキストから音声を生成する
        text2speech = gTTS(text=self.text, lang=language)
        # mp3ファイルとして保存する
        text2speech.save(file_path)
