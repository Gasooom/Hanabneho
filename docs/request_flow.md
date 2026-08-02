# Request Flow

This diagram shows what happens after a citizen submits a report.

```text
Citizen

↓

POST /api/v1/reports/analyze

↓

FastAPI

↓

Analysis Service

↓

Hanabneho Graph

↓

Supervisor Agent

↓

Perception Agent

↓

Vision Agent

↓

Context Agent

↓

Reasoning Agent

↓

Routing Agent

↓

Structured Response
```


## Step 1

A citizen uploads:

- an image
- a short description


## Step 2

The API validates the request and creates the evidence object.


## Step 3

The request is passed to the LangGraph workflow.

Each agent performs one responsibility before handing the state to the next agent.


## Step 4

The final result is returned as structured JSON.

```json
{
    "summary": "...",
    "category": "...",
    "severity": "...",
    "confidence": 0.95,
    "recommended_authority": "...",
    "reasoning": "..."
}
```

The client never communicates directly with the AI model.

Everything goes through the application's workflow.