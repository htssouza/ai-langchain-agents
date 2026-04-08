# LangChain Agent Tests

Personal experiments and tests with LangChain agents, tools, and patterns.

Based on [LangChain Academy's foundations course](https://academy.langchain.com/courses/foundation-introduction-to-langchain-python).

---

## Setup

### Prerequisites

- [uv](https://docs.astral.sh/uv/) (recommended) or [pip](https://pypi.org/project/pip/)
  - `uv` is also required in Module 2 to run the MCP server with `uvx`
- Python >=3.12, <3.14 (`uv sync` handles this automatically)

### Installation

```bash
cp example.env .env
```

Edit `.env` with your API keys:

```bash
# Required
OPENAI_API_KEY='your_openai_api_key_here'
TAVILY_API_KEY='your_tavily_api_key_here'

# Optional
ANTHROPIC_API_KEY='your_anthropic_api_key_here'
GOOGLE_API_KEY='your_google_api_key_here'

# Optional - LangSmith tracing
LANGSMITH_API_KEY='your_langsmith_api_key_here'
#LANGSMITH_TRACING=true
LANGSMITH_PROJECT=lca-lc-foundation
```

Install dependencies:

<details open>
<summary>Using uv (recommended)</summary>

```bash
uv sync
```

</details>

<details>
<summary>Using pip</summary>

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

</details>

### Verify Setup

<details open>
<summary>Using uv</summary>

```bash
uv run python env_utils.py
```

</details>

<details>
<summary>Using pip</summary>

```bash
source .venv/bin/activate
python env_utils.py
```

</details>

### Run Notebooks

<details open>
<summary>Using uv (recommended)</summary>

```bash
uv run jupyter lab
```

</details>

<details>
<summary>Using pip</summary>

```bash
source .venv/bin/activate
jupyter lab
```

</details>

### Run LangGraph Studio (optional)

From `notebooks/module-1` or `notebooks/module-3`:

<details open>
<summary>Using uv (recommended)</summary>

```bash
uv run langgraph dev
```

</details>

<details>
<summary>Using pip</summary>

```bash
source .venv/bin/activate
langgraph dev
```

</details>

## Notebooks

### Module 1: Create Agent

- Foundational models
- Tools
- Short-Term Memory
- Multimodal Messages
- Personal Chef agent

### Module 2: Advanced Agent

- Model Context Protocol (MCP)
- Context and State
- Multi-Agent Systems
- Wedding Planner agent

### Module 3: Production-Ready Agent

- Managing Long Conversations
- Human In The Loop (HITL)
- Dynamic Agents
- Email Assistant agent
- Agent Chat UI

## API Keys

- [OpenAI](https://openai.com/index/openai-api/) — primary model provider (gpt-5-nano)
- [Anthropic](https://console.anthropic.com) — optional
- [Google](https://ai.google.dev/gemini-api/docs/quickstart) — optional
- [Tavily](https://tavily.com) — search provider (free tier available)
- [LangSmith](https://smith.langchain.com/) — optional tracing and evaluation