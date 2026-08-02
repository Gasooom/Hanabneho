# The AI Brain

One design decision I cared about from the beginning was avoiding one giant AI prompt.

Instead, I wanted the system to behave more like a team.

Each agent has one job.

That keeps the workflow easier to understand, easier to test, and easier to improve over time.


## Supervisor Agent

The Supervisor starts the workflow.

Its responsibility is to coordinate the execution of the graph and prepare the shared state.


## Perception Agent

The Perception Agent is responsible for collecting information from the available evidence.

Today it works with images.

In future versions it will also support:

- Audio
- OCR
- GPS
- Other sources of information


## Vision Agent

The Vision Agent looks at uploaded images.

Its job is simply to describe what it sees.

It doesn't classify incidents or decide what should happen next.


## Context Agent

The Context Agent combines all available observations into one shared context.

Instead of passing raw data to the next step, it creates a cleaner picture of the incident.


## Reasoning Agent

The Reasoning Agent is where the actual analysis happens.

It produces:

- Summary
- Category
- Severity
- Confidence
- Recommended authority
- Explanation


## Routing Agent

The Routing Agent is intentionally simple in the current version.

For now it forwards the recommended authority.

In future versions it will apply deterministic business rules so routing decisions come from the application instead of the language model.