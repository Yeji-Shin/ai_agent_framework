# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow.core import tool
from promptflow.tracing import trace, start_trace

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

@tool
@trace
def my_python_tool(input1: str) -> str:
    return "Prompt: " + input1

if __name__ == "__main__":
    input1 = "안녕하세요. tracing test 입니다."

    start_trace()

    result = my_python_tool(input1)
    print(result)