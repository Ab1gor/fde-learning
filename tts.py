import asyncio


class TextToSpeech:

    async def speak(self, text):

        print("Speaking:", text)

        await asyncio.sleep(0.5)
