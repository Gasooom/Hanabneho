# System Architecture

Hanabneho is organized into independent layers so that each part of the system has a single responsibility.

The API handles requests, the service layer coordinates the application's use cases, and the AI Brain is responsible for understanding and analyzing citizen reports. This separation makes the project easier to maintain today and easier to extend as new AI capabilities are added.


## High-Level Architecture

```text
                 Citizen
                    │
                    ▼
          ┌──────────────────┐
          │   FastAPI API    │
          └──────────────────┘
                    │
                    ▼
          ┌──────────────────┐
          │ Analysis Service │
          └──────────────────┘
                    │
                    ▼
      ┌──────────────────────────┐
      │ Hanabneho AI Brain       │
      │      (LangGraph)         │
      │                          │
      │ Supervisor               │
      │        │                 │
      │ Perception               │
      │        │                 │
      │ Vision                   │
      │        │                 │
      │ Context                  │
      │        │                 │
      │ Reasoning                │
      │        │                 │
      │ Routing                  │
      └──────────────────────────┘
                    │
                    ▼
      Structured Incident Analysis
```


## API Layer

The API receives citizen reports, validates the request, and returns a structured response.

Its responsibility is communication with the outside world, not AI reasoning.

## Service Layer

The service layer coordinates the application's use cases.

For AI analysis, it prepares the request and hands it to the AI Brain without containing model-specific logic.


## AI Brain

The AI Brain is implemented using **LangGraph**.

Instead of relying on one large AI prompt, the workflow is divided into specialized agents. Each agent performs one responsibility before passing the shared state to the next step.

This design keeps the workflow easier to understand, easier to test, and easier to extend over time.


## Domain Layer

The domain contains the core business entities of the application, including reports, evidence, incidents, and authorities.

These models are independent from both FastAPI and AI providers.


## Infrastructure Layer

External services such as OpenAI, Gemini, and repositories are isolated from the business logic.

This makes it possible to replace AI providers or persistence implementations without changing the rest of the application.


## Design Principles

While building Hanabneho, I tried to follow a few simple principles:

- Every component should have one responsibility.
- AI should be part of the application's architecture, not just an API call.
- Business logic should stay independent from AI providers.
- New capabilities should be added by extending the workflow instead of rewriting it.

The current architecture is intentionally simple, but it provides a solid foundation for future features such as audio reports, OCR, historical retrieval, and more advanced multi-agent workflows.