from datetime import datetime

class User:
    def __init__(self, username: str):
        self.username = username
        self.history = []
    
    def add_quiz_result(self, score: int, category: str):
        result = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'score': score,
            'category': category
        }
        self.history.append(result)