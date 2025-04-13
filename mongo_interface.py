from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.code_review

def save_review(code, issues, feedback):
    db.reviews.insert_one({
        "code": code,
        "issues": issues,
        "feedback": feedback
    })
