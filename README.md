Amber: The Function Partner

"Don't just show me the graph. Tell me the story of gravity."

**Amber** is an AI agent designed to explain mathematical functions not via formulas, but through visual analogies.

Purpose:
Most math tools show you *what* (e.g., Desmos graphs). Amber explains **why**.
- Why is x^2 a U-shape? (Because it's a ball thrown in the air).
- Why does sin(x) wave? (Because it's a circle unrolled over time).

Tech Stack?
- **Core:** Python 3.10+
- **Brain:** OpenAI GPT something
- **Framework:** prob langgraph

Roadmap (30-Day Build)
We are building this agent from scratch to learn the fundmentals of AI engineering.

- [x] Tier 1: The Chatter (Single-file connection to LLM)
- [ ] Tier 2: The Architect (Basically broke it down in parts)
- [ ] Tier 3: The Historian (Context/Memory Management)
- [ ] Tier 4: The Tool User (Calculator & Function Calling)
- [ ] Use langgraph
- [ ] Finish
- [ ] Test eh

How to Run:
1. Clone the repo.

2. Add your API Key to `.env`:
   OPENAI_API_KEY=sk-proj-...

3. Install dependencies:
   pip install -r requirements.txt

4. Run:
   python simple_bot.py

*Built by Anh Duc*
Btw this project serve the purpose of earning shoolarship and proving my visual thinking ability.