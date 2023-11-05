import random
import PySimpleGUI as sg
from database import load_settings, save_settings

def magic_number_game():
    while True:
        attempts = 0

        layout = [
            [sg.Text("Вгадай число!", font=("Helvetica", 16))],
            [sg.Text("Введіть число від 1 до 5: ")],
            [sg.InputText(key="user_guess")],
            [sg.Text("", size=(20, 2), key="output_text")],
            [sg.Button("Вгадати"), sg.Button("Вийти")]
        ]

        window = sg.Window("Гра Вгадай число", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Вийти":
                window.close()
                return

            if event == "Вгадати":
                user_guess = values["user_guess"]

                try:
                    user_guess = int(user_guess)
                    attempts += 1

                    magic_number = random.randint(1, 5)

                    if user_guess < magic_number:
                        window["output_text"].update("Число більше.")
                    elif user_guess > magic_number:
                        window["output_text"].update("Число менше.")
                    else:
                        window["output_text"].update(f"Ви вгадали число {magic_number} за {attempts} спроб.")
                        window["Вгадати"].update(disabled=True)

                        replay = sg.popup_yes_no("Бажаєте грати ще раз?", "Гра Вгадай число")

                        if replay == "Yes":
                            break
                        else:
                            window.close()
                            return
                except ValueError:
                    window["output_text"].update("Напишіть число в межах від 1 до 5.")

def main():
    magic_number_game()

if __name__ == "__main__":
    main()