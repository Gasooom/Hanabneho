# Hanabneho

Helping communities report damaged infrastructure using AI.

## Why I Built This

Hanabneho started with a simple idea.

When roads collapse, bridges fail, or public infrastructure is damaged, citizens are often the first people to see it. Unfortunately, reporting those incidents is usually slow, unstructured, and difficult to prioritize.

I wanted to explore how AI could help make that process faster and more useful.

Rather than building another chatbot, I designed Hanabneho as an AI-powered reporting system where uploaded evidence is analyzed through a structured workflow before producing a response.

The goal isn't to replace engineers or public authorities.

The goal is to help them receive clearer, more organized information so they can respond more effectively.


## What Hanabneho Does

A citizen submits:

- A photo
- A short description

The system then:

- Understands the uploaded image
- Combines it with the citizen's description
- Identifies the type of incident
- Estimates its severity
- Suggests the authority responsible for handling it
- Returns a structured analysis through an API


## Why LangGraph?

I chose LangGraph because I wanted the AI workflow to be explicit.

Instead of asking one large prompt to do everything, the work is divided between small agents that each have one responsibility.

That makes the system easier to understand today and easier to extend in the future.

As the project grows, adding capabilities like speech, OCR, or historical retrieval should mean adding new agents rather than rewriting the entire pipeline.


## Current Status

The current version supports:

- Image understanding
- Infrastructure damage assessment
- Structured AI analysis
- Multi-agent orchestration using LangGraph
- FastAPI REST API
- Automated tests

Future versions will introduce audio reports, OCR, historical retrieval, and better routing decisions.