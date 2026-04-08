from dotenv import load_dotenv

load_dotenv()

import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage

MCP_CONFIG = {
    "local_server": {
        "transport": "streamable_http",
        "url": "https://mcp.kiwi.com",
    }
}

SYSTEM_PROMPT = (
    "You are a helpful assistant that can use tools to answer questions about flights."
)

AGENT_CONFIG = {"configurable": {"thread_id": "1"}}


async def main():
    client = MultiServerMCPClient(MCP_CONFIG)
    tools = await client.get_tools()  # await here
    agent = create_agent(
        model="gpt-5-nano",
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent

    # use agent...
    # response = agent.invoke(
    #     {
    #         "messages": [
    #             HumanMessage(
    #                 content="Tell me about flights between Manchester and Lisbon?"
    #             )
    #         ]
    #     },
    #     config=AGENT_CONFIG,
    # )

    # print(response)


agent = asyncio.run(main())
