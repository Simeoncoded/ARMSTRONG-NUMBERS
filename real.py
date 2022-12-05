import tkinter as tk
import re

main_window = tk.Tk()

canvas = tk.Canvas(main_window, width=400, height=300,  relief='raised')
canvas.pack()

title = tk.Label(main_window, text='Check for Armstrong number')
title.config(font=('helvetica', 14))
canvas.create_window(200, 25, window=title)

user_instructions = tk.Label(main_window, text='Type your Number from 100-999:')
user_instructions.config(font=('helvetica', 10))
canvas.create_window(200, 100, window=user_instructions)


user_input = tk.Entry(main_window)

canvas.create_window(200, 140, window=user_input)


def submit():
    try:

        number = int(user_input.get())
        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = number
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10

        # display the result
        if number == sum:
            info.set(f'{number} is an Armstrong number')
        else:
            info.set(f'{number} is not an Armstrong number')

        # display a message if user's input is not a number
    except(ValueError):
        info.set(f'Input a valid number')


button = tk.Button(text='Submit', command=submit, bg='brown',
                   fg='white', font=('helvetica', 9, 'bold'))

info = tk.StringVar()
info.set('')
info_label = tk.Label(main_window, textvariable=info)
canvas.create_window(200,210,window=info_label)

canvas.create_window(200, 180, window=button)

main_window.mainloop()
