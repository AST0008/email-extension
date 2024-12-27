from flask import Flask, request, jsonify
from huggingface_hub import InferenceClient

# Set up the Flask app
app = Flask(__name__)

# Set up the Hugging Face Inference API client
YOUR_HUGGINGFACE_API_KEY = "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"
client = InferenceClient(model="google/flan-t5-large", token=YOUR_HUGGINGFACE_API_KEY)

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
            "Write a professional email based on the subject above. The email should include:\n"
            "- A polite greeting.\n"
            "- A clear purpose explaining the meeting request.\n"
            "- Relevant details about the meeting (date, time, location, and agenda).\n"
            "- A polite closing and a call to action.\n\n"
            "Keep the email concise, formal, and professional."
        )

        # Generate the email using the Hugging Face Inference API
        response = client.text_generation(
            prompt,
            max_new_tokens=250,
            temperature=0.5,  # Reduces randomness
            top_k=50,         # Limits sampling to the top 50 words
            top_p=0.9,        # Ensures diversity with nucleus sampling
            repetition_penalty=2.0  # Penalizes repeated phrases
        )

        # Return the generated email
        return jsonify({"email": response.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


# from huggingface_hub import InferenceClient

# YOUR_HUGGINGFACE_API_KEY = "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"

# # Set up the Hugging Face Inference API client
# client = InferenceClient(model="google/flan-t5-large", token=YOUR_HUGGINGFACE_API_KEY)

# # Input email subject
# subject = "Meeting Request for Quarterly Strategy"
# # Create a prompt
# prompt = (
#     f"Subject: {subject}\n\n"
#     "Write a professional email based on the subject above. The email should include:\n"
#     "- A polite greeting.\n"
#     "- A clear purpose explaining the meeting request.\n"
#     "- Relevant details about the meeting (date, time, location, and agenda).\n"
#     "- A polite closing and a call to action.\n\n"
#     "Keep the email concise, formal, and professional."
# )

# # Send the request
# response = client.text_generation(
#     prompt,
#     max_new_tokens=250,
#     temperature=0.5,  # Reduces randomness
#     top_k=50,         # Limits sampling to the top 50 words
#     top_p=0.9,        # Ensures diversity with nucleus sampling
#     repetition_penalty=2.0  # Penalizes repeated phrases
# )

# # Print the generated email
# print(response)

