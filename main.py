from flask import Flask, request, jsonify
from groq import Groq
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = Groq(
    api_key="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",
)

@app.route('/fact-check', methods=['POST'])
def fact_check():
    data = request.json
    user_input = data.get('text', '')

    prompt = f"""Analyze the following text for potential misinformation:

"{user_input}"

Provide a fact-check analysis in the following format:
1. Summary: A brief summary of the claim.
2. Verdict: Truthful, Misleading, False, or Unverified.
3. Explanation: A detailed explanation of the fact-check.
4. Sources: List reliable sources that support your analysis. Include full URLs for any relevant articles.
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
       
    )

    response = chat_completion.choices[0].message.content

    # Split the response into sections
    sections = response.split('\n\n')
    structured_response = {
        'summary': sections[0].replace('1. Summary: ', '').strip() if len(sections) > 0 else '',
        'verdict': sections[1].replace('2. Verdict: ', '').strip() if len(sections) > 1 else '',
        'explanation': sections[2].replace('3. Explanation: ', '').strip() if len(sections) > 2 else '',
        'sources': sections[3].replace('4. Sources: ', '').strip() if len(sections) > 3 else '',
    }

    # Extract links from sources
    import re
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', structured_response['sources'])
    structured_response['links'] = urls

    return jsonify(structured_response)

if __name__ == '__main__':
    app.run(debug=True)