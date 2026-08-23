import pytest

from audio import AudioInput


@pytest.mark.asyncio
async def test_audio_consumer():

    audio = AudioInput()

    frame = await audio.receive_frame("track")

    assert frame == b"audio-frame"
