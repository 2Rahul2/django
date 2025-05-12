from google import genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
class GetSummary:
    def get_summary(self , review_text , product_name):
        api_key = os.getenv("GOOGLE_API_KEY")

        client = genai.Client(api_key=api_key)

        # product_name = "Samsung Galaxy S23 Ultra"  # The product user asks for
        # review_text = """
        # The Samsung Galaxy S23 Ultra has an amazing display, long battery life, and a powerful camera system.
        # However, it is quite expensive and the phone is bulky, making it less comfortable for one-handed use.
        # """

        prompt = f"""
Analyze the following product review and return a structured JSON with 'summary', 'pros', 'cons', and 'recommendations' for similar products.
For both 'pros' and 'cons', also include their percentage representation (e.g., 60% pros, 40% cons).

Review for: {product_name}

Review:
{review_text}

Strictly output only valid JSON, without extra text or explanations. Ensure it follows this format:

{{
    "summary": "Short summary of the review",
    "pros": {{
        "items": ["List of pros"],
        "percentage": <Percentage of pros, e.g., 60>
    }},
    "cons": {{
        "items": ["List of cons"],
        "percentage": <Percentage of cons, e.g., 40>
    }},
    "recommendations": [
        {{
            "product_name": "Alternative Product 1",
            "key_features": ["Feature 1", "Feature 2"],
            "why_recommended": "Short reason why this is a good alternative"
        }},
        {{
            "product_name": "Alternative Product 2",
            "key_features": ["Feature 1", "Feature 2"],
            "why_recommended": "Short reason why this is a good alternative"
        }}
    ]
}}

Only return JSON output. Do not include any additional explanations.
"""



        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )

        # Print the response as JSON
        # print(response.text)

        # (Optional) If the response is not formatted as JSON, you may need to parse it:
        # import json

        response_text = response.text.strip()  # Remove extra spaces or newlines

        # Try parsing JSON safely
        try:
            structured_output = json.loads(response_text)
            return json.dumps(structured_output, indent=4)  # Pretty-print JSON
        except json.JSONDecodeError:
            print("Response is not in valid JSON format. Fixing formatting...")

            # Attempt to extract JSON from response
            json_start = response_text.find("{")
            json_end = response_text.rfind("}") + 1
            json_content = response_text[json_start:json_end]

            try:
                structured_output = json.loads(json_content)
                return json.dumps(structured_output, indent=4)
            except json.JSONDecodeError:
                print("Failed to extract valid JSON. Please check the model's response.")
                return None
