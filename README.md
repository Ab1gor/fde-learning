# LiveKit FDE Practice — Exercise 1

## Customer report

> The agent joins successfully and responds to the user. However, after the user has been talking for a while, the agent becomes increasingly delayed. Eventually the user says something and the agent responds to something they said several seconds earlier.

## Your task

You are the FDE. Debug the repository.

The interview evaluates:

1. How you orient yourself in an unfamiliar codebase.
2. How you trace the critical path.
3. How you form and test hypotheses.
4. How you use instrumentation/logging.
5. How you make a minimal fix.
6. How you verify the fix with tests.
7. How you explain tradeoffs.

### Important

Do not assume the obvious suspicious line is necessarily the root cause. Reproduce the customer symptom before changing the architecture.

## Suggested commands

Run the tests:

    pytest -q

Run the application:

    python main.py

You may add temporary logging and write additional tests.

## Interview rule

Do not look for a pre-written solution. Treat this as a debugging exercise.
