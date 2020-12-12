# Libraries

from tkinter import *
from tkinter import messagebox
import random
import webbrowser

url = 'https://www.github.com/m3r4j'

players_turn = random.choice(['X', 'O'])


# Create the window
root = Tk()
root.title('Tic-Tac-Toe')
root.resizable(0,0)


# Create the board
board = {
'1':' ', '2':' ', '3':' ',
'4':' ', '5':' ', '6':' ',
'7':' ', '8':' ', '9':' ',
}

def reset():
	global board
	global players_turn

	players_turn = random.choice(['X', 'O'])

	board = {
	'1':' ', '2':' ', '3':' ',
	'4':' ', '5':' ', '6':' ',
	'7':' ', '8':' ', '9':' ',
	}

	root.after(0, display_board)
	messagebox.showinfo(players_turn, f'{players_turn} is starting!')


def open_github():
	webbrowser.open(url)


def options():
	button_reset = Button(root, text='Reset', command=reset, padx=85, fg='blue')
	button_reset.grid(row=0, column=1)



	button_exit = Button(root, text='Exit', command=root.destroy, padx=85, fg='blue')
	button_exit.grid(row=0, column=2)


	button_github = Button(root, text='Github', command=open_github, padx=85, fg='blue')
	button_github.grid(row=0, column=3)


def place_move(position,column):
	# Checks
	global players_turn


	row = 3

	if int(position) in list(range(1,4)):
		row = 1

	elif int(position) in list(range(4,7)):
		row = 2

	if board[position] == ' ':
		board[position] = players_turn
		Label(root, text=players_turn, font=(None, 60)).grid(row=row, column=column)

	else:
		messagebox.showinfo('Taken','This spot has already been taken')


	if players_turn == 'X':
		players_turn = 'O'

	elif players_turn == 'O':
		players_turn = 'X'

	
	if check_winner('O'):
		messagebox.showinfo('Winner','O is the winner!')
		return 

	if check_winner('X'):
		messagebox.showinfo('Winner','X is the winner!')
		return 

	if check_if_tie():
		messagebox.showinfo('Draw',' It was a tie!')
		return





def check_winner(player):
	if board['1'] == player and board['2'] == player and board['3'] == player:
		return True

	elif board['4'] == player and board['5'] == player and board['6'] == player:
		return True

	elif board['7'] == player and board['8'] == player and board['9'] == player:
		return True

	elif board['1'] == player and board['4'] == player and board['7'] == player:
		return True

	elif board['2'] == player and board['5'] == player and board['8'] == player:
		return True

	elif board['3'] == player and board['6'] == player and board['9'] == player:
		return True

	elif board['1'] == player and board['5'] == player and board['9'] == player:
		return True

	elif board['3'] == player and board['5'] == player and board['7'] == player:
		return True



# Check if the board is filled out
def check_if_filled():
	count = 0
	for i in board.values():
		if i != ' ':
			count += 1


	if count == 9:
		return True



def check_if_tie():
	if check_if_filled():
		return True



def display_board():

	# Display the board onto the screen

	# Row 1
	button_1 = Button(root, text=board['1'], padx=100, pady=100, command=lambda: place_move('1',1))
	button_1.grid(row=1, column=1)
	
	button_2 = Button(root, text=board['2'], padx=100, pady=100, command=lambda: place_move('2',2))
	button_2.grid(row=1, column=2)

	button_3 = Button(root, text=board['3'], padx=100, pady=100, command=lambda: place_move('3',3))
	button_3.grid(row=1, column=3)
	
	# Row 2
	button_4 = Button(root, text=board['4'], padx=100, pady=100, command=lambda: place_move('4',1))
	button_4.grid(row=2, column=1)

	button_5 = Button(root, text=board['5'], padx=100, pady=100, command=lambda: place_move('5',2))
	button_5.grid(row=2, column=2)

	button_6 = Button(root, text=board['6'], padx=100, pady=100, command=lambda: place_move('6',3))
	button_6.grid(row=2, column=3)
	
	# Row 3
	button_7 = Button(root, text=board['7'], padx=100, pady=100, command=lambda: place_move('7',1))
	button_7.grid(row=3, column=1)

	button_8 = Button(root, text=board['8'], padx=100, pady=100, command=lambda: place_move('8',2))
	button_8.grid(row=3, column=2)
	
	button_9 = Button(root, text=board['9'], padx=100, pady=100, command=lambda: place_move('9',3))
	button_9.grid(row=3, column=3)



def main():
	display_board()
	options()

	# Tell the screen who is starting
	messagebox.showinfo(players_turn, f'{players_turn} is starting!')

main()


# Run the mainloop
root.mainloop()