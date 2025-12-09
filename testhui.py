import requests
import os
import json

# ====== CẤU HÌNH ======
HF_API_KEY = os.getenv("HF_API_KEY") or "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"

MODELS = {
    "1": "mistralai/Mistral-7B-Instruct-v0.3",
    "2": "microsoft/Phi-3-mini-4k-instruct",
    "3": "Qwen/Qwen2.5-7B-Instruct"
}

current_model_key = "1"

def chat(prompt):
    model_id = MODELS[current_model_key]
    url = f"https://router.huggingface.co/hf-inference/models/{model_id}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt
    }

    res = requests.post(url, headers=headers, json=payload, timeout=60)
    return res.json()

def show_models():
    print("\n📦 Danh sách model:")
    for k, v in MODELS.items():
        active = "✅" if k == current_model_key else "  "
        print(f"{active} {k}. {v}")
    print("Gõ: /model <số> để đổi model")
    print("Gõ: /exit để thoát\n")

print("🤗 Hugging Face Chat (FREE)")
print("Gõ /model để đổi model | /exit để thoát")
show_models()

while True:
    user_input = input("👤 Bạn: ").strip()

    if user_input.lower() in ["/exit", "exit", "quit"]:
        print("👋 Tạm biệt!")
        break

    if user_input.startswith("/model"):
        _, *args = user_input.split()
        if args and args[0] in MODELS:
            current_model_key = args[0]
            print(f"✅ Đã đổi sang model: {MODELS[current_model_key]}")
        else:
            print("❌ Model không hợp lệ")
        show_models()
        continue

    try:
        result = chat(user_input)

        if isinstance(result, list) and "generated_text" in result[0]:
            print("🤖 AI:", result[0]["generated_text"])
        else:
            print("⚠️ Phản hồi lạ:")
            print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        print("❌ Lỗi:", str(e))
