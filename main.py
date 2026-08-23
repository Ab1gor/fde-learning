import asyncio

from agent import Agent


async def main():
    agent = Agent()
    await agent.start()


if __name__ == "__main__":
    asyncio.run(main())
