# Homework 1 — Levani Mosiashvili

## What I Built
A Python script that calls two Gemini models with the same prompt and compares their responses, token usage, latency, and cost.

**Prompt used:** "Explain recursion and give a concrete code example in Python."

**Models called:**
- `gemini-3-flash-preview`
- `gemini-3.1-flash-lite-preview`

## How to Run
1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install google-genai python-dotenv`
4. Copy `.env.example` to `.env` and add your Gemini API key
5. Run: `python hw01.py`

## Cost Analysis

| Call | Model | Input Tokens | Output Tokens | Total Tokens | Latency (ms) | Cost (paid equiv.) |
|---   |---    |---|---|---|---|---|
| 1    | gemini-3-flash-preview | 12 | 709 | 1311 | 8667 | $0.000427 |
| 2    | gemini-3.1-flash-lite-preview | 12 | 693 | 705 | 5360 | $0.000418 |

## Reflection

Both models gave surprisingly detailed explanations for just a 12-token prompt, which showed me how much output a tiny input can generate. I expected the responses to be similar and as expected both independently chose the factorial example and structured their answers almost identically. The first model was notably slower at 8667ms versus 5360ms, even though it produced only slightly more tokens, but What confused me was the total token count discrepancy, gemini-3-flash-preview showed 1311 total tokens despite 12 input and 709 output. After looking into it I found that Gemini's thinking models generate internal reasoning tokens that are counted in the total but never shown in the response text. The cost difference between the two models was minimal at less than $0.00001, so I think model choice matters more for speed and quality than for cost.