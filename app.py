from flask import Flask, request, jsonify
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Set up the Flask app
app = Flask(__name__)
load_dotenv()

# Set up the Hugging Face Inference API client
api_key = os.getenv("YOUR_HUGGINGFACE_API_KEY")
client = InferenceClient(model="google/flan-t5-large", token=api_key)

@app.route("/generate", methods=["POST"])
def generate_email():
    try:
        # Parse request JSON for the subject
        data = request.json
        subject = data.get("subject", "")

        if not subject:
            return jsonify({"error": "Subject is required"}), 400

        # Create the prompt
        prompt = (
            f"Subject: {subject}\n\n"
            "Write a professional email based on the subject above. The email should:\n"
            "- Include a polite greeting.\n"
            "- Clearly state the purpose of the meeting.\n"
            "- Avoid repetition and keep the response concise (100-150 words).\n"
            "- Conclude with a polite closing.\n\n"
            "The email should be clear, formal, and professional."
        )

        # Generate the email using the Hugging Face Inference API
        response = client.text_generation(
            prompt,
            max_new_tokens=200,
            temperature=0.7,  
            top_k=50,         
            top_p=0.9,        
            repetition_penalty=2.0
        )

        # Return the generated email
        return jsonify({"email": response.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

