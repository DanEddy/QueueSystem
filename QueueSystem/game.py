"""
Assignment 3 part 2
CSSE1001/7030
Semester 2, 2018
"""

__author__ = "Daniel Eddy (s4480588)"

# Remake of the game snake

import tkinter as tk
from tkinter import messagebox
import random


class Game(tk.Canvas):
    """" A game of snake"""
    def __init__(self):
        """ Construct a game of snake
        """
        super().__init__(width=300, height=300)
        # Initialising variables
        self._play = False
        self._orientation = None
        self._fruit_position = None
        self._head_pos = None
        # Snake Gui attributes
        self._snake_head = 'Ӧ'
        self._snake_tail_parts = 'o'
        # Initial tail length of snake
        self._num_tail_parts = 2
        self._fruit = '©'
        self._score = 0
        # Initialising snake movement
        self._x_movement = 0
        self._y_movement = 0
        # Binding arrow keys to snake direction:
        self.master.bind('<Up>', self.up_direction)
        self.master.bind('<Down>', self.down_direction)
        self.master.bind('<Left>', self.left_direction)
        self.master.bind('<Right>', self.right_direction)

        # Starting the game
        self.start_game()

    def start_game(self):
        """ Initialises elements of game
        """
        self._play = True

        # Identifying random start position
        self._head_pos = self.random_position()
        # Identifying random start orientation
        self._orientation = self.start_orientation()
        # Placing snake and fruit on canvas
        self.place_elements()

        # Using recursion to refresh the snake game every 175 milliseconds
        self.after(175, self.play_game)

    def play_game(self):
        """ Recursion used to refresh the game (snake movement) every 175 milliseconds
        """
        # Determining if the snake has collided with the wall or itself
        self.check_won()
        self.check_impact()
        if self._play:
            # Checking if the snake has 'eaten' an fruit
            self.got_fruit()
            # Moving the snake
            self.move_snake()
            self.after(175, self.play_game)

    def check_won(self):
        """ Determines if snake has filled the screen
        """
        # Identifying snakes Head and Tail elements
        head = self.find_withtag('Head')
        tail_parts = self.find_withtag('Tail')
        # Determining if snake has filled the 30x30 screen
        if len(head + tail_parts) == 900:
            self.game_won()

    def check_impact(self):
        """ Determines if snake has collided with itself or the wall
        """
        # Check for collision with wall
        head_pos = self.coords('Head')
        if head_pos[0] < 10:
            self.end_game()
        elif head_pos[0] > 290:
            self.end_game()
        elif head_pos[1] < 10:
            self.end_game()
        elif head_pos[1] > 290:
            self.end_game()

        # Checking if snakes head has collided with tail.
        tail = self.find_withtag('Tail')
        for index in range(len(tail)):
            if head_pos == self.coords(tail[index]):
                self.end_game()

    def got_fruit(self):
        """ Checks if the snake is close enough to eat the fruit
        """
        if self.coords('Head') == self.coords('Fruit'):
            # Eat food (add tail to snake)
            x_coord, y_coord = self.coords('Fruit')
            self.create_text(x_coord, y_coord, text=self._snake_tail_parts, tag='Tail')
            # Give user points
            self._score += 100
            # Deleting caught fruit from canvas
            self.delete('Fruit')
            # Create new piece of fruit
            self.place_fruit()

    def move_snake(self):
        """ Moves snake forward
        """
        # Identifying snakes Head and Tail elements
        head = self.find_withtag('Head')
        tail_parts = self.find_withtag('Tail')

        # Compiling snake part positions
        snake = tail_parts + head
        # Moving Tail Parts from last to first
        for index in range(len(snake)-1):
            # Identifying position of snake tail parts, and the future position of the tail_part.
            current_coord = self.coords(snake[index])
            future_coord = self.coords(snake[index+1])

            # Identifying the x and y coordinate change for each tail movement
            delta_x = future_coord[0] - current_coord[0]
            delta_y = future_coord[1] - current_coord[1]
            # Moving snake element by change in x and y
            self.move(snake[index], delta_x, delta_y)

        # Moving the snakes head
        self.move(head, self._x_movement, self._y_movement)

    def end_game(self):
        """ Ends the game
        """
        self._play = False
        tk.messagebox.showinfo('Game Over', 'Your Score: ' + str(self._score))
        # Deleting snake game
        self.pack_forget()

    def game_won(self):
        """ Wins the game
        """
        self._play = False
        tk.messagebox.showinfo('Winner', 'Your score: ' + str(self._score))
        # Deleting snake game
        self.pack_forget()

    def start_orientation(self):
        """ Returns a random direction
        """
        return random.choice('NSEW')

    def random_position(self):
        """ Returns a tuple of random coordinates within the canvas
        """
        x = random.randrange(10, 290, 10)
        y = random.randrange(10, 290, 10)
        pos = (x, y)
        return pos

    def place_elements(self):
        """ Creates the snakes initial two tail lengths with respect to the direction of travel. Also places a fruit.
        """
        # Placing an initial fruit
        self.place_fruit()
        # Creating snake head
        self.create_text(self._head_pos, text=self._snake_head, tag='Head')
        # Creating tail in opposite direction to direction of travel
        if self._orientation == 'N':
            self.create_text(self._head_pos[0], self._head_pos[1]-20, text=self._snake_tail_parts, tag='Tail')
            self.create_text(self._head_pos[0], self._head_pos[1]-10, text=self._snake_tail_parts, tag='Tail')
            self._x_movement = 0
            self._y_movement = 10

        elif self._orientation == 'E':
            self.create_text(self._head_pos[0]-20, self._head_pos[1], text=self._snake_tail_parts, tag='Tail')
            self.create_text(self._head_pos[0]-10, self._head_pos[1], text=self._snake_tail_parts, tag='Tail')
            self._x_movement = 10
            self._y_movement = 0

        elif self._orientation == 'S':
            self.create_text(self._head_pos[0], self._head_pos[1]+20, text=self._snake_tail_parts, tag='Tail')
            self.create_text(self._head_pos[0], self._head_pos[1]+10, text=self._snake_tail_parts, tag='Tail')
            self._x_movement = 0
            self._y_movement = -10

        elif self._orientation == 'W':
            self.create_text(self._head_pos[0]+20, self._head_pos[1], text=self._snake_tail_parts, tag='Tail')
            self.create_text(self._head_pos[0]+10, self._head_pos[1], text=self._snake_tail_parts, tag='Tail')
            self._x_movement = -10
            self._y_movement = 0

    def place_fruit(self):
        """ Places a fruit at a random position on canvas
        """
        (x, y) = self.random_position()
        # Placing fruit on canvas
        self.create_text(x, y, text=self._fruit, tag='Fruit')

    def up_direction(self, event):
        """ Change movement direction to North
        """
        if self._y_movement <= 0:
            self._x_movement = 0
            self._y_movement = -10

    def down_direction(self, event):
        """ Change movement direction to South
        """
        if self._y_movement >= 0:
            self._x_movement = 0
            self._y_movement = 10

    def right_direction(self, event):
        """ Change movement direction to East
        """
        if self._x_movement >= 0:
            self._x_movement = 10
            self._y_movement = 0

    def left_direction(self, event):
        """ Changes movement direction to west
        """
        if self._x_movement <= 0:
            self._x_movement = -10
            self._y_movement = 0


class GameWindow(tk.Frame):
    """Snake Window design
    """
    def __init__(self):
        super().__init__()
        """ Initialise the Snake window layout, containing the game canvas
        """
        # Creating instance of game
        Game().pack()


class SnakeGame(object):
    """ Class used to only run game on command"""
    def __init__(self):
        """ Begin construction of snake game"""
        app = GameWindow()

