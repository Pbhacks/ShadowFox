import tkinter as tk
from tkinter import messagebox
import turtle
import random

# Define words with their categories
WORD_BANK = {
    "Animals": ["elephant", "giraffe", "penguin"],
    "Climate": ["rainfall", "sunshine", "blizzard"]
}

MAX_TRIES = 6

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🐢 Hangman with Turtle Visuals")
        self.master.geometry("800x600")

        self.word, self.category = self.get_word()
        self.display_word = ['_' for _ in self.word]
        self.guessed_letters = []
        self.tries = 0

        self.create_widgets()
        self.update_display()
        self.draw_hint()

    def get_word(self):
        category = random.choice(list(WORD_BANK.keys()))
        word = random.choice(WORD_BANK[category])
        return word, category

    def create_widgets(self):
        # Frame for category and word
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(pady=10)

        self.category_label = tk.Label(self.top_frame, text=f"Category: {self.category}", font=("Arial", 16))
        self.category_label.pack()

        self.word_label = tk.Label(self.top_frame, text="", font=("Arial", 28))
        self.word_label.pack()

        # Frame for buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        self.buttons = {}
        for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            btn = tk.Button(self.button_frame, text=letter.upper(), width=4, height=2,
                            command=lambda ch=letter: self.check_letter(ch))
            btn.grid(row=i//9, column=i%9, padx=2, pady=2)
            self.buttons[letter] = btn

        # Canvas for turtle hint
        self.canvas = tk.Canvas(self.master, width=400, height=300, bg='lightblue')
        self.canvas.pack(pady=10)
        self.turtle_screen = turtle.TurtleScreen(self.canvas)
        self.turtle = turtle.RawTurtle(self.turtle_screen)
        self.turtle.hideturtle()
        self.turtle.speed(0)

    def update_display(self):
        self.word_label.config(text=" ".join(self.display_word))

    def check_letter(self, letter):
        self.buttons[letter].config(state=tk.DISABLED)
        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.display_word[i] = letter
        else:
            self.tries += 1

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        if '_' not in self.display_word:
            messagebox.showinfo("🎉 You Win!", f"Correct word: {self.word.upper()}")
            self.master.destroy()
        elif self.tries >= MAX_TRIES:
            messagebox.showerror("💀 Game Over", f"You lost! The word was: {self.word.upper()}")
            self.master.destroy()

    def draw_hint(self):
        word = self.word
        t = self.turtle
        t.clear()
        if word == "elephant":
            t.penup()
            t.goto(-30, -50)
            t.pendown()
            t.circle(40)  # Head
            t.penup()
            t.goto(-70, -20)
            t.pendown()
            t.circle(10)  # Ear
            t.penup()
            t.goto(10, -50)
            t.setheading(-90)
            t.pendown()
            t.circle(20, 180)  # Trunk

        elif word == "penguin":
            t.color("black")
            t.penup()
            t.goto(0, -80)
            t.pendown()
            t.begin_fill()
            t.circle(60)
            t.end_fill()
            t.color("white")
            t.penup()
            t.goto(-20, 0)
            t.pendown()
            t.begin_fill()
            t.circle(20)
            t.end_fill()

        elif word == "giraffe":
            t.color("orange")
            t.penup()
            t.goto(-10, -50)
            t.pendown()
            t.forward(20)
            t.left(90)
            t.forward(100)
            t.right(30)
            t.forward(20)
            t.backward(20)
            t.left(60)
            t.forward(20)

        elif word == "rainfall":
            t.color("gray")
            t.penup()
            t.goto(-100, 100)
            t.pendown()
            t.begin_fill()
            t.circle(40)
            t.end_fill()
            for x in range(-80, 100, 40):
                t.penup()
                t.goto(x, 90)
                t.setheading(-90)
                t.pendown()
                t.forward(50)

        elif word == "sunshine":
            t.color("yellow")
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            t.circle(40)
            t.end_fill()
            for angle in range(0, 360, 30):
                t.penup()
                t.goto(0, 0)
                t.setheading(angle)
                t.forward(60)
                t.pendown()
                t.forward(20)

        elif word == "blizzard":
            t.color("white")
            for _ in range(30):
                t.penup()
                t.goto(random.randint(-180, 180), random.randint(-100, 100))
                t.pendown()
                t.dot(random.randint(5, 10))

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()
