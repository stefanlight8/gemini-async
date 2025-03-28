import asyncio

from gemini import Client

gemini: Client = Client("<your api token>")


async def main() -> None:
    response = await gemini.generate_content(text="Hello, Gemini!")
    if not response:
        print("No response")
        return
    print(response.candidates[0].content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
