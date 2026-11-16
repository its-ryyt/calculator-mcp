# Calculator MCP Server

A lightweight Model Context Protocol (MCP) server for doing arithmetic and simple mathematical operations. The project exposes calculator tools, math constants, and prompt templates that can be used by MCP-compatible clients such as AI assistants and local tooling.

## Features

The server includes:

- Basic arithmetic tools:
  - `add`
  - `subtract`
  - `multiply`
  - `divide`
- Advanced calculation tools:
  - `power`
  - `square_root`
  - `percentage`
- Math constants resources:
  - `constants://math`
  - `constants://pi`
  - `constants://e`
- Helpful prompts:
  - `solve_equation`
  - `calculation_help`

## Project structure

```text
calculator-mcp/
├── calculator_server.py      # MCP server and tool definitions
├── pyproject.toml            # Python package metadata and dependencies
├── src/
│   └── calculator_mcp/
│       └── __init__.py      # Package entry point placeholder
└── README.md                # Project documentation
```

## Requirements

- Python 3.13 or newer
- `mcp[cli]`

## Getting started

1. Open a terminal in the project folder.
2. Create and activate a virtual environment if needed:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the project dependencies:

```bash
python -m pip install -U pip
python -m pip install -e .
```

4. Start the server:

```bash
python calculator_server.py
```

## Example tools

These tool functions are exposed by the server:

- `add(a, b)` -> returns a string like `"5 + 3 = 8"`
- `subtract(a, b)` -> returns a string like `"10 - 4 = 6"`
- `multiply(a, b)` -> returns a string like `"2 × 6 = 12"`
- `divide(a, b)` -> returns a safe error message if `b == 0`
- `power(base, exponent)` -> calculates the exponentiation result
- `square_root(number)` -> computes the square root of a non-negative number
- `percentage(percent, value)` -> calculates a percentage of a value

## Example resources

The MCP server also exposes math constants:

- `constants://pi` -> returns the value of pi
- `constants://e` -> returns Euler's number
- `constants://math` -> returns multiple constants in a single response

## Notes

This project is intended as a simple demonstration of an MCP server built around math operations. It is suitable for experimentation with tool calling, prompt design, and lightweight server integration with MCP-enabled clients.

## License

This project does not currently declare a license in the package metadata.
