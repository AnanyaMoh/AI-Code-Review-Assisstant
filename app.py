from flask import Flask, request, jsonify
from review_engine.analyzer import analyze_code
from review_engine.nlp_model import get_nlp_feedback
from db.mongo_interface import save_review

app = Flask(_name_)

@app.route('/review', methods=['POST'])
def review():
    code = request.json.get('code')
    issues = analyze_code(code)
    feedback = get_nlp_feedback(code)
    save_review(code, issues, feedback)
    return jsonify({"issues": issues, "feedback": feedback})

if _name_ == '_main_':
    app.run(debug=True)
