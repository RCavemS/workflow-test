"""A small hello-world script."""

import sys


def get_greeting(name: str = "world") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    """Print greeting message to standard output."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(get_greeting(name))


if __name__ == "__main__":
    main()
