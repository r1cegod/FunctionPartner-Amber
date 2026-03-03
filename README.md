Amber: The Function Partner v0.3

"Don't just explain the formular, show me how that shit look like."
**Amber** is an AI agent designed to explain mathematical functions not via formulas, but through visual intuition.

### Purpose:
Most of you don't even use any graph tools (e.g., Desmos graphs). Amber explains the formula and show you the graph.
- Why is x^2 a U-shape? (Because it's a ball thrown in the air).
- Why does sin(x) wave? (Because it's a circle unrolled over time).

### Tech Stack?
- **Brain:** OpenAI GPT + LangGraph agent
- **Backend:** FastAPI (Python)
- **Frontend:** React + Vite + Tailwind CSS + Plotly.js

### Roadmap (Maybe not 30-Day Build)
We are building this agent from scratch to learn the fundmentals of AI engineering.
- [x] Tier 1: The Chatter
- [x] Tier 2: The Architect  
- [x] Tier 3: The Historian
- [x] Tier 4: The Tool User
- [x] LangGraph rebuild
- [x] Simple Amber v0 
Days 1-2 (21-22/2): MVP
- [x] v0.1: Plotly graph tool + basic prompt
- [x] v0.2: Deploy, test live
   - [x] Simple deloy
   - [x] Graph 
   - [x] Clean UI
Days 3-13 (23/2-5/3): Upgrades & Polish (2h/day)
Full frontend setup!
- [x] Phase 1: The api shell (backend)
- [x] Phase 2: The dashboard (frontend)
Then...
Build whatever makes it better
- [x] Better UI
- [x] More function types

### Important: Amber project stoped, pivoting to new project

### How to Run:

**Requirements:** Python 3.10+, Node.js 18+

**Terminal 1 — Backend:**
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Add OPENAI_API_KEY=sk-... to .env first
python -m uvicorn main:app --reload
```
→ API runs at `http://localhost:8000`

**Terminal 2 — Frontend:**
```
cd amber-frontend
npm install
npm run dev
```
→ UI runs at `http://localhost:5173`

Type a formula (e.g. `x^3 - 3x + 2`) in the chat. Watch the graph update.


### Q&A:
Why?  
I want to use this to futher streghthen my schoolarship portfolio. Related to my statement "I want to help visual thinker like me"  
TF are you doing?  
Clone, break, learn how it works, recreate, move on, repeat until I know how raw AI agent works and not using framework is holding me back then use framework, finish the project, apply, win (maybe)

### Logs:
- Holy shit I thought I need to learn everything turn out I can just adapt while building
- Understand how a tier 4 raw python bot works and build it myself in 4 day??? shi, I was blessed with a visual brain
- Understand deep enough to upgrade it with langgraph in 1 day! time to start Amber
- I thought upgrading simple bot with langgraph in under 1 hour with the right doc is easy mode so I tried to recreate from starch. Turn out its a trap, just keep doing what my brain wants!
- Time to pivot.

*Built by Anh Duc*