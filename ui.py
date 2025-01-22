import customtkinter as ctk
from tkinter import messagebox
from code import QuizManager


class QuizApp:
    def __init__(self, root, quiz_manager):
        self.root = root
        self.quiz_manager = quiz_manager
        self.user = None

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
        self.entry_username = ctk.CTkEntry(self.login_frame, placeholder_text="Enter your username", font=("Arial", 14), width=300)
        self.entry_username.pack(pady=10)

        self.button_login = ctk.CTkButton(self.login_frame, text="Login", command=self.login, font=("Arial", 16), width=200, height=40)
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

        label_welcome = ctk.CTkLabel(self.main_menu_frame, text=f"Welcome, {self.user.username}!", font=("Arial", 24, "bold"))
        label_welcome.pack(pady=20)
        button_start_quiz = ctk.CTkButton(self.main_menu_frame, text="Start Quiz", command=self.selectCategorUi, font=("Arial", 16), width=200, height=40)
        button_start_quiz.pack(pady=10)
        button_view_history = ctk.CTkButton(self.main_menu_frame, text="View History", command=self.historyUi, font=("Arial", 16), width=200, height=40)
        button_view_history.pack(pady=10)
        button_export_results = ctk.CTkButton(self.main_menu_frame, text="Export Results", command=self.export_results, font=("Arial", 16), width=200, height=40)
        button_export_results.pack(pady=10)
        button_quit = ctk.CTkButton(self.main_menu_frame, text="Quit", command=self.root.destroy, font=("Arial", 16), width=200, height=40)
        button_quit.pack(pady=10)




if __name__ == "__main__":
    quiz_manager = QuizManager("questions.csv")
    root = ctk.CTk()
    app = QuizApp(root, quiz_manager)
    root.mainloop()
