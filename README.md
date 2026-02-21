Amber: The Function Partner

"Don't just explain the formular, show me how that shit look like."
**Amber** is an AI agent designed to explain mathematical functions not via formulas, but through visual intuition.

### Purpose:
Most math tools show you *what* (e.g., Desmos graphs). Amber explains **why** and animate the graph to show you how changes in formula affects it.
- Why is x^2 a U-shape? (Because it's a ball thrown in the air).
- Why does sin(x) wave? (Because it's a circle unrolled over time).

### Tech Stack?
- **Core:** Python 3.10+
- **Brain:** OpenAI GPT something
- **Framework:** Langgraph

### Roadmap (Maybe not 30-Day Build)
We are building this agent from scratch to learn the fundmentals of AI engineering.
- [x] Tier 1: The Chatter
- [x] Tier 2: The Architect  
- [x] Tier 3: The Historian
- [x] Tier 4: The Tool User
- [x] LangGraph rebuild
- [x] Simple Amber v0 
- [ ] Amber v0.1 (Finished graph tool, prompt audit) 21/2
- [ ] Amber v0.2 (make it use vietnamese, plan to upgrade tool/sysprompt to match goal "dạy đồ thị hàm số để thi htpt" basically finish the backend mvp work) 22/2
- [ ] Amber v0.3 (Wrap it in API so the website can talk to it, basically MAKE IT LIVE!!!)

## SUCCESS CRITERIA
Scholarship-ready when:
- Can explain y=x² spatially (visual learner approach)
- Interactive Plotly graph works (zoom, pan, hover, change values)
- Socratic question triggers thinking
- Works in Vietnamese
- Deployed at public URL
- Demo video recorded
- Your story connects (visual learner → built what I needed)
NOT required:
- User authentication
- Database
- Stress testing
- v1.0 perfection
- All edge cases handled

### How to Run:
1. Clone the repo.
2. Add your API Key to `.env`:
   OPENAI_API_KEY=sk-proj-...
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   python Amber.py

### Actual time line:
- Tier 1-4: 4 freaking day, I can totally rewrote the entire thing
- Rebuilt on langgraph: 1 day, its just upgrade the brain with langgraph

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

*Built by Anh Duc*