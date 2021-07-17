import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

class TicTacToe:

    def __init__(self, app):
        self.app = app
        self.app.title('Tic Tac Toe')
        self.app.iconbitmap('icon.ico')
        self.app.geometry('650x600') 
        self.app.minsize(650, 600)
        self.app.configure(bg = 'skyblue')

        self.labels = {}
        self.buttons = {}

        self.how = False
        self.begin(False) 

        self.app.mainloop()

    def begin(self, destroy):                
        self.home = True

        def exit_game():
            if messagebox.askokcancel('Tic Tac Toe - Exit', 'Do you want to exit the game?'):
                self.app.destroy()
                if self.how: self.how_app.destroy()
        
        self.app.protocol('WM_DELETE_WINDOW', exit_game)

        if destroy:
            for label in self.labels: self.labels[label].destroy()
            for button in self.buttons: self.buttons[button].destroy()         

        self.labels['title'] = tk.Label(self.app, text = 'TIC TAC TOE', fg = 'darkblue', bg = 'skyblue', font = 'Arial 60 bold')
        self.labels['title'].place(relx = 0.5, rely = 0.25, anchor = CENTER)

        if self.how == False:
            self.buttons['how'] = Button(self.app, text = 'How to play', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 15, command = lambda:self.how_to_play())
            self.buttons['how'].place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.buttons['single'] = Button(self.app, text = 'Single player', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 15, command = lambda:self.settings(1))
        self.buttons['single'].place(relx = 0.3, rely = 0.6, anchor = CENTER)

        self.buttons['double'] = Button(self.app, text = 'Double player', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 15, command = lambda:self.settings(2))
        self.buttons['double'].place(relx = 0.7, rely = 0.6, anchor = CENTER)

        self.buttons['exit'] = Button(self.app, text = 'Exit', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 7, command = lambda:exit_game())
        self.buttons['exit'].place(relx = 0.5, rely = 0.9, anchor = CENTER)

    def how_to_play(self):
        self.buttons['how'].destroy()
        self.how = True

        self.how_app = Tk()
        self.how_app.title('Tic Tac Toe - How to play')
        self.how_app.iconbitmap('icon.ico')
        self.how_app.geometry('500x400') 
        self.how_app.resizable(width = 0, height = 0)
        self.how_app.configure(bg = 'skyblue')

        title = tk.Label(self.how_app, text = 'How to play', fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
        title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        text = tk.Text(self.how_app, width = 48, height = 12, font = 'Arial 12', padx = 15, pady = 15, wrap = WORD, spacing2 = 5)
        text.insert(1.0, "Tic Tac Toe is a very simple game to play. The game is played by 2 players on a 3 by 3 grid containing 9 squares. The 2 players take turns \
to fill up the grid with their symbol - X or O. \n\n\
The game contains to modes: Single player and Double player. In the Single player mode, the second player is the computer. Each game will consist of an even number \
of rounds. In alternate rounds Player 1 starts with X while in the other rounds, Player 2 (or computer) starts with X. \n\n\
If in a round, Player 1 starts with X and Player 2 starts with O, Player 1 begins the round by selecting a square from the grid and placing an X there. Player 2 follows \
by choosing a non-occupied square and placing an O in it. The players continue to take alternate turn to fill up the grid. \n\n\
A round comes to and end when any player manages to place their symbol in 3 consecutive squares (horizontal, vertical or diagonal) of the grid. The player wins that \
round and gets 1 point. It may so happen that all the 9 squares on the grid are filled but no player has 3 consecutive symbols on the grid. Then the round is a draw \
and each player is awarded half a point for that round. After all rounds are complete, the player with the highest points wins the game. \n\n\
Have fun playing!")

        text.configure(state = 'disabled')
        text.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        def close_how_to_play():
            self.how_app.destroy()
            self.how = False
            if self.home == True:
                self.buttons['how'] = Button(self.app, text = 'How to play', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 15, command = lambda:self.how_to_play())
                self.buttons['how'].place(relx = 0.5, rely = 0.5, anchor = CENTER)

        close = Button(self.how_app, text = 'Close', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 7, command = lambda:close_how_to_play())
        close.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        self.how_app.protocol('WM_DELETE_WINDOW', close_how_to_play)
        self.how_app.mainloop()

    def settings(self, players):
        self.players = players
        self.home = False

        for label in self.labels: self.labels[label].destroy()
        for button in self.buttons: self.buttons[button].destroy()    

        self.labels['settings'] = tk.Label(self.app, text = 'Game settings', fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
        self.labels['settings'].place(relx = 0.5, rely = 0.1, anchor = CENTER)

        self.labels['rounds'] = tk.Label(self.app, text = 'Select the number of rounds', fg = 'darkblue', bg = 'skyblue', font = 'Arial 15')
        self.labels['rounds'].place(relx = 0.4, rely = 0.3, anchor = CENTER)

        round_choices = [2, 4, 6, 8, 10, 12]
        self.total_rounds = StringVar(self.app)
        self.total_rounds.set(2)
        dropdown = OptionMenu(self.app , self.total_rounds , *round_choices)
        dropdown.config(fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 5)
        dropdown.place(relx = 0.7, rely = 0.3, anchor = CENTER)

        self.buttons['play'] = Button(self.app, text = 'Play', fg = 'white', bg = 'darkblue', font = 'Arial 20 bold', width = 10, command = lambda:[dropdown.destroy(), self.board_setup()])
        self.buttons['play'].place(relx = 0.5, rely = 0.6, anchor = CENTER)

        self.buttons['home'] = Button(self.app, text = 'Home', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 7, command = lambda:[dropdown.destroy(), self.begin(True)])
        self.buttons['home'].place(relx = 0.5, rely = 0.9, anchor = CENTER)

    def board_setup(self):
        self.total_rounds = int(self.total_rounds.get())
        for label in self.labels: self.labels[label].destroy()
        for button in self.buttons: self.buttons[button].destroy()   

        self.board = Canvas(self.app, height = 379, width = 379, bg = 'skyblue', bd = 0, highlightthickness = 0, relief = 'ridge')
        self.board.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.board.create_rectangle(117, 2, 132, 377, outline = 'darkblue', fill = 'darkblue')
        self.board.create_rectangle(247, 2, 262, 377, outline = 'darkblue', fill = 'darkblue')
        self.board.create_rectangle(2, 117, 377, 132, outline = 'darkblue', fill = 'darkblue')
        self.board.create_rectangle(2, 247, 377, 262, outline = 'darkblue', fill = 'darkblue')
        
        def quit_game():
            if messagebox.askokcancel('Tic Tac Toe - Quit game', 'Are you sure you want to quit this game? (All progress will be lost and you will be taken to the home page)'):
                self.board.destroy()
                self.begin(True)

        self.buttons['quit'] = Button(self.app, text = 'Quit', fg = 'white', bg = 'darkblue', font = 'Arial 15', width = 7, command = lambda:quit_game())
        self.buttons['quit'].place(relx = 0.5, rely = 0.9, anchor = CENTER)
        
        self.round = 1
        self.turn = 1
        self.filled = {'X': [], 'O': []}
        self.scores = {1: 0.0, 2: 0.0}
        self.round_over = False

        triplets = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.winning_triplets = {}
        for count1 in range(1, 10):
            self.winning_triplets[count1] = []
            for count2 in range(8):
                if count1 in triplets[count2]: self.winning_triplets[count1].append(triplets[count2])

        self.gameplay()

    def gameplay(self):
        if not self.round_over:
            if ((self.round + self.turn) % 2) == 0: player_to_play = 1
            else: player_to_play = 2

            if self.turn % 2 != 0: self.symbol = 'X'
            else: self.symbol = 'O'

            if self.players == 1:
                if player_to_play == 1: player_symbol = self.symbol
                else:
                    if self.symbol == 'X': player_symbol = 'O'
                    else: player_symbol = 'X'
                if self.turn > 1: self.labels['turn'].destroy()
                self.labels['turn'] = tk.Label(self.app, text = 'Round {}: You are playing with {}'.format(self.round, player_symbol), fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
                self.labels['turn'].place(relx = 0.5, rely = 0.1, anchor = CENTER)
            if self.players == 2:            
                if self.turn > 1: self.labels['turn'].destroy()
                self.labels['turn'] = tk.Label(self.app, text = 'Round {}: Player {} to play ({})'.format(self.round, player_to_play, self.symbol), fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
                self.labels['turn'].place(relx = 0.5, rely = 0.1, anchor = CENTER)

        if self.turn == 1:
            self.buttons[1] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(1))
            self.buttons[2] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(2))
            self.buttons[3] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(3))
            self.buttons[4] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(4))
            self.buttons[5] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(5))
            self.buttons[6] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(6))
            self.buttons[7] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(7))
            self.buttons[8] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(8))
            self.buttons[9] = Button(self.board, bg = 'skyblue', width = 15, height = 7, command = lambda:self.add_symbol(9))

            for count in range(1, 10):
                x_coordinate = [2, 132, 262, 2, 132, 262, 2, 132, 262]
                y_coordinate = [2, 2, 2, 132, 132, 132, 262, 262, 262]
                self.buttons[count].place(x = x_coordinate[count-1], y = y_coordinate[count-1])  

        if self.players == 1 and not self.round_over and player_to_play == 2: self.engine()        

    def add_symbol(self, position):
        self.x_position = [0.16, 0.5, 0.84, 0.16, 0.5, 0.84, 0.16, 0.5, 0.84]
        self.y_position = [0.16, 0.16, 0.16, 0.5, 0.5, 0.5, 0.84, 0.84, 0.84]
        self.buttons[position].destroy()

        self.labels[position] = tk.Label(self.board, text = self.symbol, fg = 'darkblue', bg = 'skyblue', font = 'Arial 65 bold')
        self.labels[position].place(relx = self.x_position[position-1], rely = self.y_position[position-1], anchor = CENTER)

        self.game_checker(position)
        self.turn = self.turn + 1
        self.gameplay()

    def engine(self):
        available_positions = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(self.filled['X'] + self.filled['O']))
        if self.symbol == 'X': opponent = 'O'
        else: opponent = 'X'

        to_win = []
        for count1 in available_positions:
            for count2 in self.winning_triplets[count1]:
                if all(positions in self.filled[self.symbol] for positions in (list(set(count2) - set([count1])))) and count1 not in to_win: to_win.append(count1) 

        to_not_lose = []
        for count1 in available_positions:
            for count2 in self.winning_triplets[count1]:
                if all(positions in self.filled[opponent] for positions in (list(set(count2) - set([count1])))) and count1 not in to_not_lose: to_not_lose.append(count1)

        to_double = []
        for count1 in available_positions:
            for count2 in self.winning_triplets[count1]:
                check = 0
                for count3 in list(set(count2) - set([count1])):
                    if count3 in self.filled[self.symbol] or count3 in available_positions: 
                        if count3 in self.filled[self.symbol]: check = check + 1
                if check == 1 and count1 not in to_double: to_double.append(count1)

        to_not_let_double = []
        for count1 in available_positions:
            for count2 in self.winning_triplets[count1]:
                check = 0
                for count3 in list(set(count2) - set([count1])):
                    if count3 in self.filled[opponent] or count3 in available_positions: 
                        if count3 in self.filled[opponent]: check = check + 1
                if check == 1 and count1 not in to_not_let_double: to_not_let_double.append(count1)

        if self.turn > 2:
            if to_win: self.add_symbol(random.choice(to_win))
            elif to_not_lose: self.add_symbol(random.choice(to_not_lose))
            elif to_double: self.add_symbol(random.choice(to_double))
            elif to_not_let_double: self.add_symbol(random.choice(to_not_let_double))
            else: self.add_symbol(random.choice(available_positions))
        else:
            if 5 in available_positions: self.add_symbol(5)
            else: self.add_symbol(random.choice(to_not_let_double))

    def game_checker(self, position):
        self.filled[self.symbol].append(position)

        def game_over():
            if self.turn >= 5:
                for count in range(len(self.winning_triplets[position])):
                    if all(x in self.filled['X'] for x in (self.winning_triplets[position])[count]): return 'X'
                    if all(o in self.filled['O'] for o in (self.winning_triplets[position])[count]): return 'O'
            if self.turn == 9: return 'Draw' 
            else: return 'No'     

        if self.turn == 8 and game_over() == 'No':
            position = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(self.filled['X'] + self.filled['O']))[0]
            self.buttons[position].destroy() 
            self.labels[position] = tk.Label(self.board, text = 'X', fg = 'darkblue', bg = 'skyblue', font = 'Arial 65 bold')
            self.labels[position].place(relx = self.x_position[position-1], rely = self.y_position[position-1], anchor = CENTER)
            self.filled['X'].append(position) 
            self.turn = 9    

        if game_over() != 'No':
            self.round_over = True
            self.labels['turn'].destroy()
            for count in list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(self.filled['X'] + self.filled['O'])): self.buttons[count].destroy()
            self.board.place(relx = 0.35, rely = 0.5, anchor = CENTER)

            if game_over() == 'X' or game_over() == 'O':
                if self.players == 1:                
                    if ((self.round + self.turn) % 2) == 0: 
                        message = 'You win'
                        player = 1
                    else: 
                        message = 'You lost' 
                        player = 2
                if self.players == 2:                
                    if ((self.round + self.turn) % 2) == 0: 
                        message = 'Player 1 wins'
                        player = 1
                    else: 
                        message = 'Player 2 wins'   
                        player = 2
                self.labels['round result'] = tk.Label(self.app, text = '{} Round {}!'.format(message, self.round), fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
                self.labels['round result'].place(relx = 0.35, rely = 0.1, anchor = CENTER)
                self.scores[player] = self.scores[player] + 1
            else:
                message = None
                self.labels['round result'] = tk.Label(self.app, text = 'Round {} is a draw!'.format(self.round), fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
                self.labels['round result'].place(relx = 0.35, rely = 0.1, anchor = CENTER)
                self.scores[1] = self.scores[1] + 0.5
                self.scores[2] = self.scores[2] + 0.5

            for count in range(1, 3):
                self.scores[count] = float(self.scores[count])
                if self.scores[count].is_integer(): self.scores[count] = int(self.scores[count])
            
            if self.players == 1:
                self.labels['scores'] = tk.Label(self.app, text = 'Scores:\n\nYou: {}\nComputer: {}'.format(self.scores[1], self.scores[2]), fg = 'darkblue', bg = 'skyblue', font = 'Arial 20 bold')
                self.labels['scores'].place(relx = 0.8, rely = 0.5, anchor = CENTER)
            if self.players == 2:
                self.labels['scores'] = tk.Label(self.app, text = 'Scores:\n\nPlayer 1: {}\nPlayer 2: {}'.format(self.scores[1], self.scores[2]), fg = 'darkblue', bg = 'skyblue', font = 'Arial 20 bold')
                self.labels['scores'].place(relx = 0.8, rely = 0.5, anchor = CENTER)
            
            if self.total_rounds - self.round > 0:
                self.buttons['next round'] = Button(self.app, text = 'Next round', fg = 'white', bg = 'darkblue', font = 'Arial 20 bold', width = 10, command = lambda:self.next_round())
                self.buttons['next round'].place(relx = 0.8, rely = 0.1, anchor = CENTER)
            else:
                self.buttons['result'] = Button(self.app, text = 'Result', fg = 'white', bg = 'darkblue', font = 'Arial 20 bold', width = 10, command = lambda:self.result())
                self.buttons['result'].place(relx = 0.8, rely = 0.1, anchor = CENTER)
                self.buttons['quit'].destroy()

    def next_round(self):
        self.round_over = False
        self.turn = 1
        self.round = self.round + 1

        self.buttons['next round'].destroy()
        self.labels['round result'].destroy()
        self.labels['scores'].destroy()
        for count in (self.filled['X'] + self.filled['O']): self.labels[count].destroy()
        self.filled = {'X': [], 'O': []}

        self.board.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.gameplay()

    def result(self):
        for label in self.labels: self.labels[label].destroy()
        self.buttons['result'].destroy()   
        self.board.destroy()

        if self.scores[1] != self.scores[2]: 
            winner = True
            if self.players == 1:                
                if self.scores[1] > self.scores[2] == 0: message = 'You win'
                else: message = 'You lost'
            if self.players == 2:                
                if self.scores[1] < self.scores[2] == 0: message = 'Player 1 wins'
                else: message = 'Player 2 wins'   
        else: winner = False

        if winner:
            self.labels['result'] = tk.Label(self.app, text = '{} the game!'.format(message), fg = 'darkblue', bg = 'skyblue', font = 'Arial 35 bold')
            self.labels['result'].place(relx = 0.5, rely = 0.2, anchor = CENTER)
        else:
            self.labels['result'] = tk.Label(self.app, text = 'The game is a draw!', fg = 'darkblue', bg = 'skyblue', font = 'Arial 35 bold')
            self.labels['result'].place(relx = 0.5, rely = 0.2, anchor = CENTER)

        if self.players == 1:
            self.labels['final scores'] = tk.Label(self.app, text = 'Final scores:\n\nYou: {}\nComputer: {}'.format(self.scores[1], self.scores[2]), fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
            self.labels['final scores'].place(relx = 0.5, rely = 0.5, anchor = CENTER)
        if self.players == 2:
            self.labels['final scores'] = tk.Label(self.app, text = 'Final scores:\n\nPlayer 1: {}\nPlayer 2: {}'.format(self.scores[1], self.scores[2]), fg = 'darkblue', bg = 'skyblue', font = 'Arial 25 bold')
            self.labels['final scores'].place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.buttons['home'] = Button(self.app, text = 'Home', fg = 'white', bg = 'darkblue', font = 'Arial 20 bold', width = 10, command = lambda:self.begin(True))
        self.buttons['home'].place(relx = 0.5, rely = 0.8, anchor = CENTER)

app = Tk()
game = TicTacToe(app)