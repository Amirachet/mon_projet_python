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
        def display_history(self):
        if not self.history:
            print("\nAucun historique disponible.")
            return
        
        print(f"\nHistorique des QCM pour {self.username}:")
        for result in self.history:
            print(f"Date: {result['date']} | Catégorie: {result['category']} | Score: {result['score']}%")

class QuizManager:
    def __init__(self):
        self.questions = {
            'Python': [
                {
                    'question': 'Quelle est la fonction pour afficher du texte en Python?',
                    'options': ['display()', 'print()', 'show()', 'write()'],
                    'correct_answer': 1
                },
                {
                    'question': 'Comment déclare-t-on une liste vide en Python?',
                    'options': ['list()', '[]', 'new List()', '{}'],
                    'correct_answer': 1
                },
                {
                    'question': 'Quelle méthode permet d\'ajouter un élément à une liste?',
                    'options': ['add()', 'append()', 'push()', 'insert()'],
                    'correct_answer': 1
                },
                {
                    'question': 'Quel est le type de données d\'une chaîne de caractères en Python?',
                    'options': ['text', 'string', 'str', 'chars'],
                    'correct_answer': 2
                },
                {
                    'question': 'Comment écrit-on une condition "si" en Python?',
                    'options': ['if:', 'when:', 'switch:', 'case:'],
                    'correct_answer': 0
                }
            ]