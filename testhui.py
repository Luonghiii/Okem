from huggingface_hub import InferenceClient
import os

# ================== CẤU HÌNH ==================
# Khuyên dùng biến môi trường:
# export HF_API_KEY="hf_xxx"
HF_API_KEY = os.getenv("HF_API_KEY")

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
# ==============================================

if not HF_API_KEY:
    print("❌ Chưa có HF_API_KEY (export HF_API_KEY trước)")
    exit(1)

client = InferenceClient(
    model=MODEL_ID,
    token=HF_API_KEY
)

print("🤗 HF Chat (InferenceClient – HF mới)")
print("Gõ 'exit' để thoát")
print("-" * 40)

while True:
    user = input("👤 Bạn: ").strip()
    if user.lower() in ["exit", "quit"]:
        print("👋 Tạm biệt!")
        break

    try:
        reply = client.text_generation(
            user,
            max_new_tokens=256,
            temperature=0.7,
            top_p=0.9,
        )
        print("🤖 AI:", reply)

    except Exception as e:
        print("❌ Lỗi:", str(e))
