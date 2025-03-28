# gemini-async
An asynchronous, static-typed library for interacting with the [Gemini] API, built with aiohttp.

Its primary excellence is the use of msgspec, providing fast serialisation and deserialisation for efficient usage of the API. The library follows a clean and consistent structure, closely aligned with the API's design, while offering simplifications, shortcuts, and enhancements for a smoother developer experience.

# Resources
- [Examples]
- Documentation

# Installation
> [!WARNING]
> gemini-async is not yet available on PyPI. You'll need to install it manually from source.
```sh
> pip install gemini-async
# or
> python3 -m pip install gemini-async
```

# Issues & Suggestions
Any feedback is welcome! If you encounter any bugs or have suggestions, feel free to submit them on our [issues page].

You can also help implement your idea by submitting a pull request, but please check the [Contributing] section first.

# Contributing

Please familiarize yourself with our [contributing guidelines] before contributing.

We recommend:
- Since we use [uv](https://astral.sh/uv), we suggest you do as well.

## Getting Started

1. Fork the repository from the `staging` branch.
2. Clone your fork.
3. Start coding!

## Working on Changes

- For new features, create a branch named `feature-<name>`, and once complete, open a pull request to the `staging` branch of the main repository.
- For patches or fixes, follow the same process, but use the `patch-<name>` naming convention.

Happy coding!

* * *

[Gemini]: https://deepmind.google/technologies/gemini/
[issues page]: https://github.com/stefanlight8/gemini-async/issues
[contributing guidelines]: ./CONTRIBUTING.md
[Examples]: ./examples
