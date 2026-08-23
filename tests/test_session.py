import pytest

from session import Session


@pytest.mark.asyncio
async def test_session_components():

    session = Session()

    assert session.room is not None
    assert session.audio is not None
    assert session.stt is not None
    assert session.llm is not None
    assert session.tts is not None
