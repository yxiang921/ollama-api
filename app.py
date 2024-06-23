from flask import Flask, request
from langchain_community.llms import Ollama

app = Flask(__name__)

cache_llm = Ollama(model="phi3:mini")

@app.route('/ai', methods=['POST'])
def aiPost():
    json_content = request.json
    query = json_content.get("query")
    print(f"query: {query}")

    response = cache_llm.invoke(query)
    print(f"response: {response}")

    response_answer = {
        "answer": response
    }

    return response


if __name__ == '__main__':
    app.run(debug=True)