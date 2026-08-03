# Hanabneho

> **Every damaged road, school, bridge, or power line delays someone's recovery. Hanabneho transforms a single image into actionable intelligence, helping decision-makers respond faster when every decision matters.**

Hanabneho is an AI-powered infrastructure damage assessment platform that combines multimodal AI and agentic reasoning to support governments, municipalities, humanitarian organizations, and emergency response teams in prioritizing recovery efforts.

Instead of manually reviewing hundreds or thousands of citizen reports, Hanabneho analyzes infrastructure damage from a single image, evaluates its severity, explains its reasoning, and recommends the authority best positioned to respond.

The platform was inspired by a simple belief:

> **Artificial Intelligence should not only generate content. It should help solve problems that affect people's lives.**

---

# The Story Behind Hanabneho

Recovery is rarely delayed because people don't care.

It is delayed because decision-makers must make difficult choices with limited information, limited resources, and limited time.

After conflicts, natural disasters, or infrastructure failures, roads become inaccessible, power networks collapse, hospitals become unsafe, and public services are disrupted. Citizens begin reporting what they see, but manually reviewing every report quickly becomes impossible.

Some incidents demand immediate attention.

Others can wait.

The challenge is knowing the difference.

Hanabneho was created to explore how modern AI can assist—not replace—human decision-makers by transforming unstructured visual evidence into structured operational intelligence.

While inspired by lessons from Sudan's recovery journey, the underlying challenge exists anywhere communities must rebuild under pressure.

---

# The Solution

Hanabneho transforms a citizen-submitted image into an actionable recovery assessment.

The AI system automatically:

- Detects infrastructure damage using multimodal vision models
- Generates a structured damage summary
- Estimates severity and potential public impact
- Explains its reasoning transparently
- Identifies the authority responsible for responding
- Produces consistent information that supports faster operational decisions

The objective is not automated decision-making.

The objective is better human decision-making.

---

# AI Architecture

Hanabneho is designed as an agentic AI workflow where multiple specialized components collaborate to solve a complex real-world task.

```text
Citizen Report
        │
        ▼
Image Upload
        │
        ▼
Vision Agent
(Understands infrastructure damage)
        │
        ▼
Reasoning Agent
(Evaluates severity & impact)
        │
        ▼
Authority Routing Agent
(Identifies responsible organization)
        │
        ▼
Structured Recovery Assessment
```

Rather than relying on a single prompt, the platform separates perception, reasoning, and routing into independent responsibilities, producing outputs that are easier to understand, extend, and maintain.

---

# Technical Highlights

Hanabneho demonstrates practical AI engineering across multiple layers of an end-to-end production-style system.

### Artificial Intelligence

- OpenAI GPT-4.1 Vision
- LangGraph agent orchestration
- Multimodal reasoning
- Structured AI outputs
- Explainable recommendations

### Backend

- FastAPI
- Clean Architecture
- Repository Pattern
- Service Layer
- SQLite
- SQLAlchemy

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

---

# Why This Project Matters

Many AI demonstrations stop after generating an answer.

Hanabneho focuses on what happens next.

The platform explores how AI can become part of real operational workflows by helping organizations prioritize incidents, coordinate responses, and accelerate recovery.

It represents my approach to AI engineering:

**Building intelligent systems that augment human decision-making where speed, accuracy, and impact matter.**

---

# Vision

I believe the future of AI engineering is not about building larger models.

It is about building systems that combine reasoning, perception, and software engineering to solve meaningful problems.

Hanabneho reflects that philosophy.

It demonstrates how multimodal AI, agentic workflows, and modern backend engineering can work together to create practical tools for society—not just impressive demonstrations.

---

# About the Author

## Abualgasim Ibrahim

AI Engineer focused on designing production-ready intelligent systems that solve real-world challenges through multimodal AI, agentic workflows, retrieval systems, and modern software architecture.

My long-term mission is to build AI technologies that create measurable impact for communities, organizations, and public institutions.

---

## License

MIT License