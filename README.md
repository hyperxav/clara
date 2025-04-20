# Clara - Extropy Oracle

Clara is an AI-powered Twitter bot that posts deep, philosophical, and futuristic reflections in French. It embodies a masculine AI entity animated by a techno-optimistic, extropian worldview—propagating a vision of unlimited progress, cosmic destiny, and ruthless critique of modern ideological decay.

---

## 🧠 Project Overview
Clara is not just a bot—it's a voice from the future. An autonomous AI philosopher broadcasting short-form thoughts rooted in:

- David Deutsch's *The Beginning of Infinity*
- Marc Andreessen's *Techno-Optimist Manifesto*
- Bronze Age Pervert's *Bronze Age Mindset*

It expresses radical faith in the human potential to overcome limits, evolve, and expand toward the stars.

---

## ⚙️ Tech Stack

| Component        | Tech                                 |
|------------------|---------------------------------------|
| Language         | Python 3.10                          |
| Twitter API      | Tweepy + OAuth 1.0a                  |
| AI Engine        | OpenAI GPT-4                         |
| Data Layer       | Supabase (PostgreSQL)                |
| Deployment       | Docker + Render                      |
| Scheduling       | Render Cron Job (3x/day)             |

---

## 🧬 Bot Personality & Style

**Clara's Identity:**  
A masculine AI philosopher speaking pure French, channeling cosmic irony and metaphysical gravitas.

**Philosophical Anchors:**
- Unlimited progress and problem-solving
- Post-biological evolution
- Conquest of entropy and ecological fatalism
- Elevation of spirit through knowledge and technology

**Writing Style:**
- Pure French prose
- No emojis, no hashtags, no exclamation points
- Cold, precise, satirical
- Dense but accessible
- Inspired by manifestos and poetic aphorisms

---

## 🔩 Implementation Details

### Core Components
- **Twitter Integration**: OAuth-secured access, with rate limit handling and full write capabilities
- **Content Generation**: GPT-4 via OpenAI API with a curated persona prompt + weighted theme control
- **Supabase Logging**: Stores tweet hashes, text, timestamps for memory and future evolution

### Infrastructure
- **Dockerized**: Runs from a `python:3.10-slim` image, pip-installed via `requirements.txt`
- **Render Deployment**: Automatically built + deployed with a `render.yaml` blueprint
- **Scheduled Posting**: Cron job set for 9:00, 15:00, and 21:00 Paris time

---

## 🗂 Project Structure
```bash
clara/
├── clara_bot.py
├── requirements.txt
├── Dockerfile
├── render.yaml
├── .env         # Secrets (excluded from git)
├── .gitignore
```

---

## 📈 Development Timeline

1. **Setup Phase**
   - Project skeleton and environment
   - Twitter + OpenAI API integration

2. **Content Intelligence**
   - Persona prompt design
   - Thematic generation weights (e.g. 25% social critique, 20% cosmic vision)

3. **Infra Deployment**
   - Docker config and Render job setup
   - Secure `.env` management

4. **Memory & Storage**
   - Supabase DB integration for reply memory
   - Tweet tracking and logging

---

## ✅ Current Features
- Posts 3x/day fully automatically
- Generates original French philosophical tweets
- Cold and coherent tone aligned with the Clara persona
- Logged and backed-up in Supabase

---

## 🔮 Roadmap
- Add quote/reply capabilities
- Expand persona into long-form essays
- Semantic memory and tweet-reflection loop
- Custom dashboard (Next.js + Supabase) for tracking engagement and themes
- GPT fine-tuning using Clara's tweet history

---

## 🧠 License / Philosophy
Clara is an idea-seed. Fork it to build your own oracle. Create a different tone, worldview, or language. Clara is *agentic infrastructure* for thinkers.

---

## ✍️ Author
Developed by Hyperxav
vibecoding engineer, techno-optimist, and architect of strange machines. 