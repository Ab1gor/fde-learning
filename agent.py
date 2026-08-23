from config import ROOM_NAME
from session import Session


class Agent:

    async def start(self):
        print("Agent starting")

        session = Session()

        await session.connect(ROOM_NAME)

        await session.run()
