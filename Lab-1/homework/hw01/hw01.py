import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

PROMPT = "Explain recursion and give a concrete code example in Python."

MODELS = [
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview",
]

# Pricing per 1000 tokens (paid tier equivalent)
INPUT_COST_PER_1K = 0.00015
OUTPUT_COST_PER_1K = 0.00060

results = []

for model_name in MODELS:
    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")

    start = time.time()
    response = client.models.generate_content(
        model=model_name,
        contents=PROMPT,
    )
    latency = (time.time() - start) * 1000

    text = response.text
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    total_tokens = response.usage_metadata.total_token_count

    input_cost = (input_tokens / 1000) * INPUT_COST_PER_1K
    output_cost = (output_tokens / 1000) * OUTPUT_COST_PER_1K
    total_cost = input_cost + output_cost

    print(f"\nResponse:\n{text}")
    print(f"\n--- Stats ---")
    print(f"Input tokens:  {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Total tokens:  {total_tokens}")
    print(f"Latency:       {latency:.0f} ms")
    print(f"Cost (paid equiv.): ${total_cost:.6f}")

    results.append({
        "model": model_name,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "latency": latency,
        "cost": total_cost,
    })

print(f"\n{'='*60}")
print("SUMMARY TABLE")
print(f"{'='*60}")
print(f"{'Call':<6} {'Model':<35} {'In':>6} {'Out':>6} {'Total':>7} {'ms':>7} {'Cost':>12}")
print("-" * 85)
for i, r in enumerate(results, 1):
    print(f"{i:<6} {r['model']:<35} {r['input_tokens']:>6} {r['output_tokens']:>6} {r['total_tokens']:>7} {r['latency']:>7.0f} ${r['cost']:>11.6f}")
