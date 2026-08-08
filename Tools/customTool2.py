from typing import Type
from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool

# Define Pydantic schema for inputs (V2 clean format)
class MultiplyInput(BaseModel):
    a: int = Field(description="The first number to multiply")
    b: int = Field(description="The second number to multiply")

# Plain function doing the core logic
def multiply_func(a: int, b: int) -> int:
    return a * b

# Create the StructuredTool from function
multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

# Test execution and properties
result = multiply_tool.invoke({'a': 3, 'b': 3})

print("Result:", result)
print("Name:", multiply_tool.name)
print("Description:", multiply_tool.description)
print("Args Schema:", multiply_tool.args)