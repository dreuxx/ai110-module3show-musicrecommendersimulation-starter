# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the coding assistant to complete a small content-based recommender,
test it, and help document its behavior in plain English.

**Prompts used:**

"Implement CSV loading with numeric conversion, score genre, mood, energy, and
acoustic preference, rank the top K songs, and return explanations. Then run
the tests and CLI."

**What did the agent generate or change?**

The implementation updated `src/recommender.py`, `src/main.py`, and
`data/songs.csv`. It also completed `README.md` and `model_card.md`. I ran
`python -m pytest -q` and `python -m src.main`.

**What did you verify or fix manually?**

I checked the score math, the numeric CSV types, the ranking order, the three
profiles, and the test output. I fixed the package import so the CLI works with
`python -m src.main`.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
