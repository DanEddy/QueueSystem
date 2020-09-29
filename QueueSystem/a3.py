"""
Assignment 3 part 1
CSSE1001/7030
Semester 2, 2018
"""

__author__ = "Daniel Eddy (s4480588)"

import tkinter as tk
from tkinter import messagebox
from tkinter import *
import datetime
import game


class ImportantNotice(tk.Frame):
    """ A label used to illustrate course notices
    """
    def __init__(self, parent):
        """Set up the text within the frame.

        Parameters:
            parent (Tk): Window in which this label is to be placed.
        """
        super().__init__(parent)
        # ImportantNotice is separated into two labels, 1) 'Important' 2) notice text
        # 1)
        notice_title = tk.Label(self, text="Important")
        notice_title.config(fg='dark goldenrod', bg="light yellow", font="Ariel 16 bold", anchor=tk.NW)
        notice_title.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # 2)
        self._notice_text = """Individual assessment items must be solely your own work. While students are encouraged to have high-level conversations about the problems they are
trying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically
detect similarity between assignment submissions."""
        notice_text = tk.Label(self, text=self._notice_text)
        notice_text.config(bg="light yellow", justify=tk.LEFT)
        notice_text.pack(side=tk.TOP, expand=True, anchor=tk.W)


class QuickQuestion(tk.Frame):
    """ Frame used to produce the Quick Questions partition
    """
    def __init__(self, parent):
        """ Construct a quick question partition, containing quick question examples and a quick question button

        Parameters:
            parent (Tk): Window in which quick question frame is placed.
        """

        super().__init__(parent)
        # Creating instance of queue manager
        self._queue_manager = QueueManager()
        self._request_help = None

        # The following subsections of the quick question frame are initialised and packed in order from top to
        # bottom of frame.

        # Initialising and placing quick question partition header
        self.quick_question_header()
        # Initialising and placing quick question examples
        self.quick_question_examples()
        # Initialising and placing request quick help button
        self.quick_help_button()

        # Creating instance of QueueList
        self._queue_list = QueueList(self)
        # Packing Quick Question queue
        self._queue_list.pack(side=tk.TOP, fill=tk.BOTH)

        # Initialises the recursive sequence refreshing the quick question queue every 10 seconds
        self.after(10000, self.refresh_counter)

    def quick_question_header(self):
        """ Creates the header of the quick question partition
        """

        # Title of header
        quick_question_title = tk.Label(self, text="Quick Questions")
        quick_question_title.config(fg="#3c763d", bg="#dff0d8", font="Ariel 24", width=5, height=1)
        quick_question_title.pack(side=tk.TOP, fill=tk.BOTH)

        # Time limit of question
        time_lim = tk.Label(self, text="<2 mins with a tutor", fg='#666', font='italic', width=5, height=1)
        time_lim.config(bg="#dff0d8")
        time_lim.pack(fill=tk.BOTH)

    def quick_question_examples(self):
        """ Creates label containing list of quick question examples
        """

        # examples of quick questions:
        question_examples = """
Some examples of quick questions:
    \u2022 Syntax errors
    \u2022 Interpreting error output
    \u2022 Assignment/MyPyTutor interpretation
    \u2022 MyPyTutor submission issues
    """
        # Creating and packing label of quick question examples.
        examples_label = tk.Label(self, text=question_examples)
        examples_label.config(bg='#fff', anchor=tk.W, justify=tk.LEFT)
        examples_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def quick_help_button(self):
        """ Creates button to request quick help
        """

        # label used as border of button
        button_border = tk.Label(self, bg='#4cae4c')  # Colour of border
        button_border.pack(pady=5)

        # Creating button to request quick help, and packing inside button_border
        quick_help_button = tk.Button(button_border, text="Request Quick Help", padx=5, pady=5,
                                      command=self.do_popup)
        quick_help_button.config(bg="#5cb85c", fg='#fff', relief="solid", bd=0)
        quick_help_button.pack()

    def do_popup(self):
        """ Creates instance of RequestHelp, creating a popup widow requesting requesting student's name
        """
        self._request_help = RequestHelp(self.add_name)

    def add_name(self, name):
        """ Adds Student to queue
        Parameters:
            name (str): Name of student
        """
        self._queue_manager.add_student(name)
        self.refresh_queue()

    def refresh_counter(self):
        """ Recursively calls for the quick question queue to be refreshed every 10 seconds
        """
        self.refresh_queue()
        self.after(10000, self.refresh_counter)

    def refresh_queue(self):
        """ Refreshes the queue by clearing the table and rewriting the list of students in the queue to the grid
        """
        self._queue_list.refresh_queue(self._queue_manager._students_in_queue)


class LongQuestion(tk.Frame):
    """ Frame used to produce the Long Questions partition
    """
    def __init__(self, parent):
        """ Construct a long question partition, containing long question examples and a long question button

        Parameters:
            parent (Tk): Window in which quick question frame is placed.
        """

        super().__init__(parent)

        # Creating instance of queue manager
        self._queue_manager = QueueManager()
        self._request_help = None

        # The following subsections of the long question frame are initialised and packed in order from top to
        # bottom of frame.

        # Initialising and placing long question partition header
        self.long_question_header()
        # Initialising and placing long question examples
        self.long_question_examples()
        # Initialising and placing request long help button
        self.long_help_button()

        # Creating instance of QueueList
        self._queue_list = QueueList(self)
        # Packing Long Question queue
        self._queue_list.pack(side=tk.TOP, fill=tk.BOTH)

        # Initialises the recursive sequence refreshing the long question queue every 10 seconds
        self.after(10000, self.refresh_counter)

    def long_question_header(self):
        """ Creates the header of the long question partition
        """

        # Title of header
        long_question_title = tk.Label(self, text="Long Questions")
        long_question_title.config(fg="#31708f", bg="#d9edf7", font="Ariel 24", width=5, height=1)
        long_question_title.pack(side=tk.TOP, fill=tk.BOTH)

        # Time limit of question
        time_lim = tk.Label(self, text=">2 mins with a tutor", fg="#666", font='italic', width=5, height=1)
        time_lim.config(bg="#d9edf7")
        time_lim.pack(fill=tk.BOTH)

    def long_question_examples(self):
        """ Creates label containing list of long question examples
        """

        # examples of long questions:
        question_examples = """
        Some examples of long questions:
            \u2022 Open ended questions
            \u2022 How to start a problem
            \u2022 How to improve code
            \u2022 debugging
            \u2022 Assignment help
            """
        # Creating and packing label of quick question examples.
        examples_label = tk.Label(self, text=question_examples)
        examples_label.config(bg='#fff', anchor=tk.W, justify=tk.LEFT)
        examples_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def long_help_button(self):
        """ Creates button to request long help
        """

        # label used as border of button
        button_border = tk.Label(self, bg='#46b8da')  # Colour of border
        button_border.pack(pady=5)

        # Creating button to request long help, and packing inside button_border
        long_help_button = tk.Button(button_border, text="Request Long Help", padx=5, pady=5,
                                     command=self.do_popup)
        long_help_button.config(bg="#5bc0de", fg='#fff', relief='solid', bd=0)
        long_help_button.pack()

    def do_popup(self):
        """ Creates instance of RequestHelp, creating a popup widow requesting requesting student's name
        """
        self._request_help = RequestHelp(self.add_name)

    def add_name(self, name):
        """ Adds Student to queue

        Parameters:
            name (str): Name of student
        """
        self._queue_manager.add_student(name)
        self.refresh_queue()

    def refresh_counter(self):
        """ Recursively calls for the long question queue to be refreshed every 10 seconds
        """
        self.refresh_queue()
        self.after(10000, self.refresh_counter)

    def refresh_queue(self):
        """ Refreshes the queue by clearing the table and rewriting the list of students in the queue to the grid
        """
        self._queue_list.refresh_queue(self._queue_manager._students_in_queue)


class RequestHelp(object):
    """Pop-up window for name entry"""
    def __init__(self, callback):
        """ Construct a pop-up window allowing the student to input their name.

        Parameters/Return:
            callback (str): Binding function used to return input of pop up box to the calling function
        """
        # Creating pop-up box
        self._pop_up_box = tk.Toplevel()
        self._pop_up_box.title('Request Help')
        self._callback = callback
        self._name_label = tk.Label(self._pop_up_box, text='Enter Name: ')
        self._name_label.grid(row=0)
        self._name_entry = tk.Entry(self._pop_up_box)
        self._name_entry.grid(row=0, column=2)
        self._enter_button = tk.Button(self._pop_up_box, text='Enter', command=self.return_entry)
        self._enter_button.grid(row=1, column=2)

    def return_entry(self):
        self._callback(self._name_entry.get())
        self._pop_up_box.destroy()


class QueueManager(object):
    """ Method used for ordering the queue"""

    def __init__(self):
        """ Maintains a record of students and the associated number of questions asked.
        Constructs an ordered list of students in queue.
        """

        # Creating a dictionary that records the total number of questions asked by a given student:
        self._known_students = {}
        self._students_in_queue = []

    def add_student(self, student):
        """" Adds a student to dictionary of known students, then adds student to the list of students in the queue

        Parameters:
            student (str): Name of student to be added to queue
        """
        # Capitalising the first letter of each word in the student's name:
        student = student.title()
        # Checking if student is already in the queue, if so, the user is informed and the process is stopped.
        # Else, the students question tally is increased/initialised and the student is added to the queue.
        # Note that if the user selects the red button, the total number of questions associated is reduced by 1,
        # such that it is iff the question was not asked.

        # Returning a warning if student does not input a name.
        if student == '':
            tk.messagebox.showinfo('Warning', 'Please enter a valid student name')
            return None

        # Returning a warning if student is already in the queue, inhibiting a student from joining multiple times.
        elif [True for element in self._students_in_queue if element[0] == student] == [True]:
            tk.messagebox.showinfo('Warning',
                                   "'{}' is already in the  queue \n Student cannot join multiple times".
                                   format(student))
            return None
        # If student is already a known student, their tally of questions asked is increased.
        elif student in self._known_students:
            self._known_students[student] += 1
        # If student is no known, the student is added to the known students dictionary.
        else:
            self._known_students[student] = 0

        # Adding student to queue and recording the join time
        self._students_in_queue.append((student, self._known_students[student],
                                        datetime.datetime.now()))
        # Calling order_queue to order the students in queue
        self.order_queue()

    def delete_student(self, student):
        """
        Deletes student from list of students in queue

        parameters:
            student (str): student whose entry is to be removed from queue
        """
        self._students_in_queue.remove(student)

    def order_queue(self):
        """Orders the queue according to number of questions asked and time spent waiting in queue"""
        # ordering queue firstly with respect to the number of questions asked
        # then secondly by the elapsed time since the question was asked.
        self._students_in_queue = sorted(sorted(self._students_in_queue, key=lambda x: x[2]), key=lambda x: x[1])


class WaitTime(object):
    """ Object for recording and evaluate time"""
    def __init__(self):
        """ Evaluates the current time, and elapsed time since student joined the queue
        """
        self._display = None
        self._wait = None

    def current_time(self):
        """ Returns the current time
        """
        return datetime.datetime.now()

    def elapsed_time(self, join_time):
        """ Returns the time elapsed since student joined queue

        Parameters:
            join_time (datetime.datetime): Time at which the student joined the queue
        """
        return divmod((self.current_time() - join_time).total_seconds(), 60)

    def individual_time_categories(self, join_time):
        """ Returns the string form of the categorised students wait time

        Parameters:
            join_time(datetime.datetime): Time at which the student joined the queue
        """
        # Determining elapsed time
        elapsed_time = self.elapsed_time(join_time)
        # Categorising the students wait falls into
        if elapsed_time[0] < 1:
            self._display = 'a few seconds ago'
        elif 1 <= elapsed_time[0] < 2:
            self._display = 'a minute ago'
        elif 2 <= elapsed_time[0] < 60:
            self._display = '{} minutes ago'.format(int(elapsed_time[0]))
        elif 60 <= elapsed_time[0] < 120:
            self._display = '1 hour ago'
        else:
            self._display = '{} hours ago'.format(int(elapsed_time[0]//60))

        return self._display

    def queue_time_categories(self, average_wait):
        """ Returns the string form of the categorized averaged wait time of the queue

        Parameters:
            average_wait (int): Average wait time of queue in minutes
        """
        # Categorising the average wait time.
        if average_wait < 1:
            self._wait = "a few seconds"
        elif average_wait == 1:
            self._wait = '1 minute'
        elif 1 < average_wait < 60:
            self._wait = '{} minutes'.format(int(average_wait))
        elif 60 <= average_wait < 120:
            self._wait = '1 hour'
        else:
            self._wait = '{} hours'.format(int(average_wait//60))

        return self._wait


class QueueList(tk.Frame):
    """ A tkinter grid containing the queue list"""

    def __init__(self, master, *args, **kwargs):
        """
        Constructs the queue qui

        Parameters:
            master (tk.Tk|tk.Frame): Frame containing this widget
        """
        super().__init__(master, *args, bg="lightgrey", **kwargs)
        self._master = master
        self._row = 0
        self._queue = []
        # Creating an instance of queue time
        self._wait_time = WaitTime()
        # Initialising the grid which will contain the queue
        for column in range(1, 4):
            tk.Grid.columnconfigure(self, column, weight=1)

        # Writing in queue
        self.refresh_queue(self._queue)

    def refresh_queue(self, lst):
        """ Rewrites entire queue list

        Parameter:
            lst (list): List of students currently in the queue
        """
        self._row = 0
        self._queue = lst
        # Clearing table
        self.clear_table()

        # Writing in average wait time
        self.average_wait_time()

        # Writing in the column headers
        self.grid_titles_config(('#', 'Name', 'Questions Asked', 'Time', '', ''))

        # Writing in students waiting in the queue
        for student in self._queue:
            self.add_row(student)

    def clear_table(self):
        """ Deletes entire queue grid
        """
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) >= 0:
                label.grid_forget()

    def average_wait_time(self):
        """ Determines the average wait time for the number of students in the queue. Writes the average wait time
        and number of students in the queue to a label
        """

        sum_time = 0
        # Summing wait times for all students currently in the queue
        for student in self._queue:
            sum_time += self._wait_time.elapsed_time(student[2])[0]
        # Base case - No students currently in the queue
        if not self._queue:
            num_students = 0
            average_wait = 0
        else:
            num_students = len(self._queue)
            average_wait = sum_time // num_students

        # Calling WaitTime to identify the average wait time of the queue
        wait_time = self._wait_time.queue_time_categories(average_wait)

        # Determining text of average wait time
        if num_students == 0:
            average_wait_text = 'No students in queue.'
        elif num_students == 1:
            average_wait_text = 'An average wait time of ' + wait_time + ' for 1 student.'
        else:
            average_wait_text = 'An average wait time of ' + wait_time + ' for ' + str(num_students) + ' students.'

        # Creating label which displays the average_wait_text
        average_wait_border = tk.Label(self, bg='#fff', text=average_wait_text, anchor=tk.W, justify=tk.LEFT)
        average_wait_border.columnconfigure(0, weight=1)
        average_wait_border.grid(row=self._row, columnspan=6, sticky=tk.N+tk.E+tk.S+tk.W, ipady=5, pady=1)
        self._row += 1

    def grid_titles_config(self, *titles):
        """
        Appends the list of column titles to the grid:

        Parameters:
            titles (tuple): Tuple containing column titles
        """
        for entry in titles:
            for column, value in enumerate(entry):
                label = tk.Label(self, text=value, font='Ariel 9 bold', bg='#fff', anchor=tk.W, justify=tk.LEFT)
                label.columnconfigure(column, weight=1)
                label.grid(row=self._row, column=column, sticky=tk.N+tk.E+tk.S+tk.W, ipady=1, pady=1)
            self._row += 1

    def add_row(self, *lst):
        """
        Append a new row of values to the grid

        Parameters:
            lst (lst): list containing student name and relevant data i.e. number of questions asked and wait time
        """
        for entry in lst:
            # Creating label containing the integer value of the students position in the queue
            label = tk.Label(self, text=str(self._row - 1), bg='#fff', anchor=tk.W, justify=tk.LEFT)
            label.columnconfigure(0, weight=1)
            label.grid(row=self._row, column=0, sticky=tk.N+tk.E+tk.S+tk.W, ipady=1)
            for column, value in enumerate(entry):
                # Creating labels to hold remaining student information
                if column + 1 == 3:
                    # Calling WaitTime to identify the elapsed time since student joined the queue
                    text = self._wait_time.individual_time_categories(value)
                    label = tk.Label(self, text=text, bg='#fff', anchor=tk.W, justify=tk.LEFT)
                    label.columnconfigure(0, weight=1)
                    label.grid(row=self._row, column=column+1, sticky=tk.N + tk.E + tk.S + tk.W, ipady=1)
                else:
                    label = tk.Label(self, text=value, bg='#fff', anchor=tk.W, justify=tk.LEFT)
                    label.columnconfigure(0, weight=1)
                    label.grid(row=self._row, column=column + 1, sticky=tk.N + tk.E + tk.S + tk.W, ipady=1)

        # Creating the accept and cancel buttons for each row
        cancel_button = tk.Button(self, command=lambda row=self._row: self.cancel(row), bg='red')
        cancel_button.grid(row=self._row, column=4, sticky=tk.E, pady=1)
        cancel_button.config(height=1, width=1)

        accept_button = tk.Button(self, command=lambda row=self._row: self.accept(row), bg='green')
        accept_button.grid(row=self._row, column=5, stick=tk.W, pady=1)
        accept_button.config(height=1, width=1)
        self._row += 1

    def cancel(self, row):
        """
        Deletes specified row from grid, and removes 1 from number of questions asked by student

        Parameters:
            row (int): Row of grid to be deleted
        """
        # Removing a question from sum of questions asked
        student = self._master._queue_manager._students_in_queue[0][0]
        self._master._queue_manager._known_students[student] -= 1
        # Deleting student from queue
        del self._master._queue_manager._students_in_queue[row - 2]
        # Refreshing queue
        self._master.refresh_queue()

    def accept(self, row):
        """
        Deletes specified row from grid

        Parameters:
            row (int): Row of grid to be deleted
        """
        # Deleting student from queue
        del self._master._queue_manager._students_in_queue[row - 2]
        # Refreshing queue
        self._master.refresh_queue()


class Window(object):
    """ Queue window design"""
    def __init__(self, master):
        """ Initialize the Queue window layout with a header containing the Important notice, and remaining area
            containing the quick and long question partitions
        """
        # Title of Window
        master.title("CSSE1001 Queue")
        master.config(bg="white")
        # Creating and packing Important Notice.
        important_notice = ImportantNotice(master)
        important_notice.pack(side=tk.TOP, anchor=tk.W)
        # Creating frames which contains the quick and long question partitions
        bottom_frame = tk.Frame(master, bg="white")
        bottom_frame.pack(expand=1, fill=tk.BOTH)
        # Creating and packing Quick Question.
        quick_question = QuickQuestion(bottom_frame)
        quick_question.config(bg='white')
        quick_question.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Creating and packing Long Question.
        long_question = LongQuestion(bottom_frame)
        long_question.config(bg='white')
        long_question.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Additional Feature - Snake game.
        def callback():
            """ Function used to call the snake game"""
            game.SnakeGame()
        # Creating drop-down menu to start snake game
        menubar = Menu(root)
        root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu.add_command(label='Snake', command=callback)
        menubar.add_cascade(label='Menu', menu=filemenu)


root = tk.Tk()
app = Window(root)
root.mainloop()
