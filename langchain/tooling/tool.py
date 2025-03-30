from langchain_openai import ChatOpenAI

def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

tools = [multiply]

llm = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)

response = llm.invoke("What is 2 times 3?")

print(response.content)
