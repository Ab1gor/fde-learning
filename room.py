import asyncio


class Room:

    async def connect(self, room_name):
        print(f"Connecting to {room_name}")
        await asyncio.sleep(0.2)
        print("Connected")

    async def wait_for_audio_track(self):
        print("Waiting for participant audio track")
        await asyncio.sleep(0.5)
        print("Audio track published")
        return "user-audio-track"
