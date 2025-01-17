![Banner](static/banner.png)

# About
Gemini-async is an async and static-typed library for working with [Gemini] built for asyncio and Python 3.

# Installation
> [!WARNING]
> Gemini-async is not available on PyPI yet.
```sh
> pip install gemini-async
# or
> python3 -m pip install gemini-async
```

# Basic usage
```py
import asyncio

from gemini import Gemini
from gemini.structs import Content, Part

gemini = Gemini("<your api token>")

async def main() -> None:
    response = await gemini.generate_content(
        Content(parts=[Part(text="Hello, Gemini!")])
    )
    if not response:
        print("No response")
        return
    print(response.candidates[0].content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
```

# Issues & Suggestions
Any feedback is welcome! If you encounter any bugs or have suggestions, feel free to submit them on our [issues page].

Also, you can help with implementation of your idea through pull request, but check [#Contributing] guidelines before.

# Contributing
Not available yet.

[Gemini]: https://deepmind.google/technologies/gemini/
[issues page]: https://github.com/stefanlight8/gemini-async/issues
