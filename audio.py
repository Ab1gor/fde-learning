import asyncio


class AudioInput:

    async def consume(self, track):

        print("Started consuming:", track)

        while True:

            frame = await self.receive_frame(track)

            print("Audio frame received")

            yield frame

    async def receive_frame(self, track):

        await asyncio.sleep(0.1)

        return b"audio-frame"
