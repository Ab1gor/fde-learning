from room import Room
from audio import AudioInput
from stt import SpeechToText
from llm import LLM
from tts import TextToSpeech


class Session:

    def __init__(self):
        self.room = Room()
        self.audio = AudioInput()
        self.stt = SpeechToText()
        self.llm = LLM()
        self.tts = TextToSpeech()

    async def connect(self, room_name):
        await self.room.connect(room_name)

    async def run(self):

        track = await self.room.wait_for_audio_track()

        print("Subscribing to:", track)

        async for audio in self.audio.consume(track):

            text = await self.stt.transcribe(audio)

            if not text:
                continue

            response = await self.llm.generate(text)

            await self.tts.speak(response)
