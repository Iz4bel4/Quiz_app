from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizz App')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text='Score: 0 ', bg=THEME_COLOR, fg='white', font=('Arial', 12, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text='sth', fill='black', font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score:{self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='The end of the game')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)