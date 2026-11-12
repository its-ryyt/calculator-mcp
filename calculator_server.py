import math
from mcp.server.mcpserver import MCPServer   # v1.x: from mcp.server.fastmcp import FastMCP

mcp = MCPServer("calculator_server")


# ================= Part 1: Basic Math Tools =================
@mcp.tool()
def add(a: float, b: float) -> str:
    """Add two numbers together."""
    return f"{a} + {b} = {a + b}"


@mcp.tool()
def subtract(a: float, b: float) -> str:
    """Subtract b from a."""
    return f"{a} - {b} = {a - b}"


@mcp.tool()
def multiply(a: float, b: float) -> str:
    """Multiply two numbers."""
    return f"{a} × {b} = {a * b}"


@mcp.tool()
def divide(a: float, b: float) -> str:
    """Divide a by b. Returns an error message if b is zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return f"{a} ÷ {b} = {a / b}"


# ================= Part 2: Advanced Tools =================
@mcp.tool()
def power(base: float, exponent: float) -> str:
    """Raise base to the power of exponent."""
    try:
        return f"{base} ^ {exponent} = {math.pow(base, exponent)}"
    except (OverflowError, ValueError) as e:
        return f"Error: {e}"


@mcp.tool()
def square_root(number: float) -> str:
    """Calculate the square root of a non-negative number."""
    if number < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return f"√{number} = {math.sqrt(number)}"


@mcp.tool()
def percentage(percent: float, value: float) -> str:
    """Calculate what percent% of value is (e.g. 15% of 230)."""
    result = (percent / 100) * value
    return f"{percent}% of {value} = {result}"


# ================= Part 3: Resources - Math Constants =================
@mcp.resource("constants://math")
def all_constants() -> str:
    """All common mathematical constants."""
    return (
        f"pi = {math.pi}\n"
        f"e = {math.e}\n"
        f"tau = {math.tau}\n"
        f"golden_ratio = {(1 + math.sqrt(5)) / 2}"
    )


@mcp.resource("constants://pi")
def pi_constant() -> str:
    """The value of pi (π)."""
    return str(math.pi)


@mcp.resource("constants://e")
def e_constant() -> str:
    """Euler's number (e)."""
    return str(math.e)


# ================= Part 4: Prompts =================
@mcp.prompt()
def solve_equation(problem: str) -> str:
    """Prompt to solve a math word problem step by step using the calculator tools."""
    return f"""You are a helpful math tutor. Solve this word problem:

{problem}

Steps:
1. Identify the known values and what needs to be found.
2. Write the equation(s) needed.
3. Use the calculator tools (add, subtract, multiply, divide, power, square_root, percentage) for every calculation.
4. Show each step clearly and give the final answer."""


@mcp.prompt()
def calculation_help(operation: str) -> str:
    """Prompt that explains how a math operation works, with examples."""
    return f"""Explain how the '{operation}' operation works in simple terms.

Include:
- A short definition
- When it is used in real life
- 2 worked examples using the calculator tools
- Common mistakes to avoid"""


if __name__ == "__main__":
    mcp.run()