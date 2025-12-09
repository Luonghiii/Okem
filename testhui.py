from huggingface_hub import InferenceClient
import os

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"

if not HF_API_KEY:
    print("❌ Chưa có HF_API_KEY")
    exit(1)

client = InferenceClient(
    token=HF_API_KEY
)

print("🤗 HF Chat (HF mới – conversational)")
print("Gõ 'exit' để thoát")
print("-" * 40)

messages = []

while True:
    user = input("👤 Bạn: ").strip()
    if user.lower() in ["exit", "quit"]:
        print("👋 Tạm biệt!")
        break

    messages.append({"role": "user", "content": user})

    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=messages,
            max_tokens=256,
            temperature=0.7,
        )

        reply = response.choices[0].message["content"]
        print("🤖 AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("❌ Lỗi:", str(e))
