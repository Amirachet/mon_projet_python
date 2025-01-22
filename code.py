from datetime import datetime
import json
import csv
import random
from typing import Dict, List

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
    def __init__(self, questions_file: str):
        self.questions_file = questions_file
        self.questions = self.loadQuestions()
        self.users = self.loadUsers()


    def loadQuestions(self) -> Dict[str, List[Dict]]:
        questions = {}
        try:
            with open(self.questions_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category = row['category']
                    question = row['question']
                    options = [row['option1'], row['option2'], row['option3'], row['option4']]
                    correctOption = row['correct_answer']

                    shuffledOptions = options[:]
                    random.shuffle(shuffledOptions)
                    newCorrectOp = ['a', 'b', 'c', 'd'][shuffledOptions.index(options[int(correctOption) - 1])]

                    question = {
                        'question': question,
                        'options': shuffledOptions,
                        'correct_option': newCorrectOp
                    }

                    if category not in questions:
                        questions[category] = []
                    questions[category].append(question)
        except FileNotFoundError:
            print("erreur lors de l'ouverture du fichier")
        return questions
        
    def loadUsers(self) -> Dict:
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def saveUsers(self):
        with open('users.json', 'w') as f:
            json.dump(self.users, f, indent=4)

    def userLogin(self, username: str) -> User:
        if username in self.users:
           userInfos = self.users[username]
           user = User(username)
           user.history = userInfos['history']
           print(f"\nBienvenue a nouveau, {username}!")
        else:
           user = User(username)
           self.users[username] = {'history': []}
           print(f"\nNouveau profil créé pour {username}!")
        return user  
           
    def runQuiz(self, user: User, category: str):
        score = 0
        totalQ = len(self.questions[category])

        print(f"\nDebut du QCM - {category}")

        for i, q in enumerate(self.questions[category], 1):
            print(f"\nQuestion {i}/{totalQ}:")
            print(q['question'])

            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")

            while True:
                try:
                    answer = int(input("\nVotre réponse (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    print("Veuillez entrer un nombre entre 1 et 4.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            correct_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3}[q['correct_option']]
            is_correct = answer - 1 == correct_index
            if is_correct:
                score += 1
                print("✓ Correct!")
            else:
                print(f"✗ Incorrect. La bonne réponse était: {q['options'][correct_index]}")

        final_score = int((score / totalQ) * 100)
        print(f"\nScore final: {final_score}%")
        user.add_quiz_result(final_score, category)
        self.users[user.username]['history'] = user.history
        self.saveUsers()

        return final_score

    def export_results(self, user: User, filename: str):
        if not user.history:
            raise ValueError("No results to export.")

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Score"])  # Header row
            for result in user.history:
                writer.writerow([result["date"], result["category"], result["score"]])


def main():
    quiz_manager = QuizManager('questions.csv')

    while True:
        username = input("Entrez votre nom d'utilisateur: ")
        user = quiz_manager.userLogin(username)

        while True:
            print("\n1. Commencer un nouveau QCM")
            print("2. Voir l'historique")
            print("3. Exporter les résultats")
            print("4. Changer d'utilisateur")
            print("5. Quitter")

            choice = input("\nChoisissez une option (1-5): ")

            if choice == '1':
                print("\nCatégories disponibles:")
                categories = list(quiz_manager.questions.keys())
                for i, cat in enumerate(categories, 1):
                    print(f"{i}. {cat}")

                cat_choice = int(input("\nChoisissez une catégorie (1-{}): ".format(len(categories))))
                if 1 <= cat_choice <= len(categories):
                    quiz_manager.runQuiz(user, categories[cat_choice - 1])

            elif choice == '2':
                user.display_history()

            elif choice == '3':
                filename = f"resultats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                quiz_manager.export_results(filename)
                print(f"\nresultats exportés dans {filename}")

            elif choice == '4':
                break

            elif choice == '5':
                return


if __name__ == "__main__":
    main()
