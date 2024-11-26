from tkinter import *
import random2
from PIL import ImageTk, Image
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """Speak the given audio string."""
    engine.setProperty("rate", 175)
    engine.say(audio)
    engine.runAndWait()


# Initialize the main window
root = Tk()
root.title("Stone Paper Scissors")
root.geometry("600x400")

# Load and resize images
img1 = Image.open('C:/Users/91765/Downloads/Telegram Desktop/stonePaper/stonePaper/stone.png')
img1_resized = img1.resize((100, 100))
stone_img = ImageTk.PhotoImage(img1_resized)

img2 = Image.open('C:/Users/91765/Downloads/Telegram Desktop/stonePaper/stonePaper/paper.png')
img2_resized = img2.resize((100, 100))
paper_img = ImageTk.PhotoImage(img2_resized)

img3 = Image.open('C:/Users/91765/Downloads/Telegram Desktop/stonePaper/stonePaper/scissors.png')
img3_resized = img3.resize((100, 100))
scissors_img = ImageTk.PhotoImage(img3_resized)

# Initialize variables
comp = random2.randint(1, 3)
result_label = Label(root, text="", font=("Arial", 16))
result_label.grid(row=1, column=0, columnspan=3, pady=20)

play_again_button = None  # Reference for the "Play Again" button


def reset_game():
    """Reset the game state."""
    global comp, result_label, play_again_button
    comp = random2.randint(1, 3)
    result_label.config(text="")
    if play_again_button:
        play_again_button.grid_forget()  # Remove the "Play Again" button


def choice(c):
    """Handle the player's choice and determine the result."""
    global comp, result_label, play_again_button
    outcomes = {
        (1, 1): "IT'S A TIE!!",
        (1, 2): "Computer won!!",
        (1, 3): "You won!!",
        (2, 2): "IT'S A TIE!!",
        (2, 1): "You won!!",
        (2, 3): "Computer won!!",
        (3, 3): "IT'S A TIE!!",
        (3, 1): "Computer won!!",
        (3, 2): "You won!!"
    }
    result_text = outcomes.get((c, comp), "Unexpected result!")
    result_label.config(text=result_text)
    speak(result_text)

    # Add a "Play Again" button
    play_again_button = Button(root, text="Play Again?", bg="orange", command=reset_game)
    play_again_button.grid(row=2, column=1, pady=20)


# Buttons for user choices
stone_button = Button(root, image=stone_img, text="Stone", command=lambda: choice(1))
stone_button.grid(row=0, column=0)

paper_button = Button(root, image=paper_img, text="Paper", command=lambda: choice(2))
paper_button.grid(row=0, column=1)

scissors_button = Button(root, image=scissors_img, text="Scissors", command=lambda: choice(3))
scissors_button.grid(row=0, column=2)

# Quit button
exit_button = Button(root, text="Quit", bg="blue", fg="white", command=root.quit)
exit_button.grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()


