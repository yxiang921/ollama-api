from flask import Flask, request, jsonify
from langchain_community.llms import Ollama
import logging

app = Flask(__name__)

cache_llm = Ollama(model="phi3:mini")

@app.route('/ai', methods=['POST'])
def aiPost():
    json_content = request.json
    query = json_content.get("query")
    app.logger.info(f"Received query: {query}")

    try:
        response = cache_llm.invoke(query)
        app.logger.info(f"Response: {response}")

        response_answer = {
            "answer": response
        }
        return jsonify(response_answer)
    except Exception as e:
        app.logger.error(f"Error: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)