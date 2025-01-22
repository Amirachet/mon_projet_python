from datetime import datetime

import customtkinter as ctk
from tkinter import messagebox
from code import QuizManager


class QuizApp:
    def __init__(self, root, quiz_manager):
        self.root = root
        self.quiz_manager = quiz_manager
        self.user = None
        self.current_question_index = 0
        self.score = 0
        self.category = None
        self.questions = []
        self.timer_seconds = 60
        self.timer_running = False

        self.root.title("Quiz Application")
        self.root.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.loginPageUi()

    def loginPageUi(self):
        self.login_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.login_frame.pack(pady=100, padx=200, fill="both", expand=True)

        self.label_username = ctk.CTkLabel(self.login_frame, text="Username:", font=("Arial", 16))
        self.label_username.pack(pady=10)
        self.entry_username = ctk.CTkEntry(self.login_frame, placeholder_text="Enter your username", font=("Arial", 14),
                                           width=300)
        self.entry_username.pack(pady=10)

        self.button_login = ctk.CTkButton(self.login_frame, text="Login", command=self.login, font=("Arial", 16),
                                          width=200, height=40)
        self.button_login.pack(pady=20)

    def login(self):
        username = self.entry_username.get().strip()
        if not username:
            messagebox.showerror("Error", "Username cannot be empty!")
            return
        self.user = self.quiz_manager.userLogin(username)
        messagebox.showinfo("Success", f"Welcome, {username}!")
        self.login_frame.destroy()
        self.mainMenuUi()

    def mainMenuUi(self):
        self.main_menu_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_menu_frame.pack(pady=50, padx=100, fill="both", expand=True)

        label_welcome = ctk.CTkLabel(self.main_menu_frame, text=f"Welcome, {self.user.username}!",
                                     font=("Arial", 24, "bold"))
        label_welcome.pack(pady=20)
        button_start_quiz = ctk.CTkButton(self.main_menu_frame, text="Start Quiz", command=self.selectCategorUi,
                                          font=("Arial", 16), width=200, height=40)
        button_start_quiz.pack(pady=10)
        button_view_history = ctk.CTkButton(self.main_menu_frame, text="View History", command=self.historyUi,
                                            font=("Arial", 16), width=200, height=40)
        button_view_history.pack(pady=10)
        button_export_results = ctk.CTkButton(self.main_menu_frame, text="Export Results", command=self.export_results,
                                              font=("Arial", 16), width=200, height=40)
        button_export_results.pack(pady=10)
        button_quit = ctk.CTkButton(self.main_menu_frame, text="Quit", command=self.root.destroy, font=("Arial", 16),
                                    width=200, height=40)
        button_quit.pack(pady=10)

    def selectCategorUi(self):
        self.main_menu_frame.destroy()

        self.category_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.category_frame.pack(pady=50, padx=100, fill="both", expand=True)

        label_title = ctk.CTkLabel(self.category_frame, text="Select a Category", font=("Arial", 24, "bold"))
        label_title.pack(pady=20)

        categories = list(self.quiz_manager.questions.keys())

        for category in categories:
            button = ctk.CTkButton(self.category_frame, text=category,
                                   command=lambda cat=category: self.start_quiz(cat), font=("Arial", 16), width=200,
                                   height=40)
            button.pack(pady=10)

    def start_quiz(self, category):
        self.category_frame.destroy()

        self.category = category
        self.questions = self.quiz_manager.questions[category]
        self.current_question_index = 0
        self.score = 0
        self.timer_seconds = 60
        self.timer_running = True

        self.quiz_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.quiz_frame.pack(pady=50, padx=100, fill="both", expand=True)

        self.update_timer()

        self.displayQuestion()

    def displayQuestion(self):

        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        self.label_timer = ctk.CTkLabel(self.quiz_frame, text=f"Time Remaining: {self.timer_seconds} seconds",
                                        font=("Arial", 16))
        self.label_timer.pack(pady=10)

        question_data = self.questions[self.current_question_index]
        question = question_data["question"]
        options = question_data["options"]

        label_question = ctk.CTkLabel(self.quiz_frame, text=question, font=("Arial", 18), wraplength=600)
        label_question.pack(pady=20)

        for i, option in enumerate(options):
            button = ctk.CTkButton(self.quiz_frame, text=option, command=lambda opt=option: self.checkAnswer(opt),
                                   font=("Arial", 16), width=300, height=40)
            button.pack(pady=10)
    def checkAnswer(self, selected_option):
        correct_option = self.questions[self.current_question_index]["options"][
            ord(self.questions[self.current_question_index]["correct_option"]) - ord("a")
        ]

        is_correct = selected_option == correct_option
        if is_correct:
            self.score += 1

        self.displayFeedback(is_correct, correct_option)

    def update_timer(self):
        if self.timer_running:
            self.timer_seconds -= 1
            if self.timer_seconds <= 0:
                self.timer_running = False
                self.show_results()
                return

            if hasattr(self, "label_timer") and self.label_timer.winfo_exists():
                self.label_timer.configure(text=f"Time Remaining: {self.timer_seconds} seconds")

            self.root.after(1000, self.update_timer)

    def historyUi(self):
        self.main_menu_frame.destroy()

        self.history_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.history_frame.pack(pady=50, padx=100, fill="both", expand=True)

        label_title = ctk.CTkLabel(self.history_frame, text="Quiz History", font=("Arial", 24, "bold"))
        label_title.pack(pady=20)

        history = self.user.history

        if not history:
            label_no_history = ctk.CTkLabel(self.history_frame, text="No quiz history available.", font=("Arial", 16))
            label_no_history.pack(pady=10)
        else:
            for result in history:
                history_text = f"Date: {result['date']} | Category: {result['category']} | Score: {result['score']}%"
                label_history = ctk.CTkLabel(self.history_frame, text=history_text, font=("Arial", 16))
                label_history.pack(pady=5)

        button_clear_history = ctk.CTkButton(
            self.history_frame,
            text="Clear History",
            command=self.clear_history,
            font=("Arial", 16),
            width=200,
            height=40,
        )
        button_clear_history.pack(pady=10)

        button_return = ctk.CTkButton(
            self.history_frame,
            text="Return to Main Menu",
            command=self.return_to_main_menu,
            font=("Arial", 16),
            width=200,
            height=40,
        )
        button_return.pack(pady=20)

    def clear_history(self):
        self.user.history = []
        self.quiz_manager.users[self.user.username]["history"] = []
        self.quiz_manager.saveUsers()
        messagebox.showinfo("Success", "Quiz history cleared!")
        self.historyUi()

    def return_to_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.mainMenuUi()

    def export_results(self):
        filename = f"resultats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.quiz_manager.export_results(self.user,filename)
        messagebox.showinfo("Exportation", f"rrsultats exportés dans {filename}")

    def displayFeedback(self, is_correct, correct_option):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        self.label_timer = ctk.CTkLabel(self.quiz_frame, text=f"Time Remaining: {self.timer_seconds} seconds",
                                        font=("Arial", 16))
        self.label_timer.pack(pady=10)

        if is_correct:
            feedback_text = "Correct!"
            feedback_color = "green"
        else:
            feedback_text = f"Incorrect. The correct answer was: {correct_option}"
            feedback_color = "red"

        label_feedback = ctk.CTkLabel(self.quiz_frame, text=feedback_text, font=("Arial", 18),
                                      text_color=feedback_color)
        label_feedback.pack(pady=20)

        button_next = ctk.CTkButton(self.quiz_frame, text="Next Question", command=self.next_question,
                                    font=("Arial", 16), width=200, height=40)
        button_next.pack(pady=20)

    def next_question(self):
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.displayQuestion()
        else:
            self.timer_running = False
            self.show_results()

    def show_results(self):
        self.quiz_frame.destroy()

        final_score = int((self.score / len(self.questions)) * 100)

        self.user.add_quiz_result(final_score, self.category)
        self.quiz_manager.users[self.user.username]["history"] = self.user.history
        self.quiz_manager.saveUsers()

        results_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        results_frame.pack(pady=50, padx=100, fill="both", expand=True)

        label_results = ctk.CTkLabel(results_frame, text=f"Quiz Finished!\nYour Score: {final_score}%",
                                     font=("Arial", 24, "bold"))
        label_results.pack(pady=20)

        button_return = ctk.CTkButton(results_frame, text="Return to Main Menu", command=self.return_to_main_menu,
                                      font=("Arial", 16), width=200, height=40)
        button_return.pack(pady=10)


if __name__ == "__main__":
    quiz_manager = QuizManager("questions.csv")
    root = ctk.CTk()
    app = QuizApp(root, quiz_manager)
    root.mainloop()