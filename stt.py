import asyncio


class SpeechToText:

    async def transcribe(self, audio):

        print("Transcribing audio")

        await asyncio.sleep(0.3)

        return "What's my account balance?"
