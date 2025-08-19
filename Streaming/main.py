from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import rich


load_dotenv()

set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")


client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

agent = Agent(
    name="My agent",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

async def main():
    result = Runner.run_streamed(agent, "Hi")

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            rich.print(event.data.delta, end="*", flush=True)

asyncio.run(main())
