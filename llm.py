import asyncio


class LLM:

    async def generate(self, text):

        print("Generating response")

        await asyncio.sleep(1)

        return "Your account balance is $5,000."
