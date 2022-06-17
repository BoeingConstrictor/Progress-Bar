import sys
from datetime import date, datetime, timedelta

"""

To initialize the function, simply assign the class to a variable and initialize it with the length of the loop.
Next, call on the required update method, and then set the self.first_pass = False.
Then, perform the items in a loop, and at the end of the loop call on the update method again
For instance:

items_to_be_looped_through = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]

updater = UpdateProgress(len(items_to_be_looped_through))
updater.update_1()
updater.first_pass = False

for i in items_to_be_looped_through:

    __---BODY OF THE LOOP---__
    updater.update_1()



If you would like to add a specific word/character to be present in the progress bar display,
you can intialize that with the 'special_char' parameter of the method.


TO ADD MORE PROGRESS LOOPS, SIMPLY COPY 'update_1', RENAME IT, AND ADD IT TO THE CLASS.
THIS ALLOWS FOR COMPELTE CUSTOMIZATION OF YOUR FUNCTION.


"""

class UpdateProgress:

    def __init__(self, total_length, bar_length=25):

        # Intital process time features
        start = datetime.now()
        print_start = start.strftime('%H:%M:%S')
        self.psList = print_start.split(':')
        self.hours = int(self.psList[0])
        self.minutes = int(self.psList[1])

        # Status Features
        self.totallength = total_length
        self.barLength = bar_length
        self.barLengthcharacter = '#'
        # Completion features
        self.first_pass = True
        self.psL = 0
        self.ex_compl = 0
        self.beginning_time = None
        self.end_time = None
        self.process_time = None
        self.process_time_no_ms = None
        self.avg_time = None
        self.time_list = []

        # progress counter
        self.prog_counter = 0  # same as i in the original
        self.progress = self.prog_counter / self.totallength

    @staticmethod
    def time_avg(times):
        return round(sum(times) / len(times), 2)

    # This updates all the internal time features, and is called automatically with each call of the update
    # line so that it is only one line of code required in the main body of the loop instead of several
    def complete(self):
        self.prog_counter += 1
        self.progress = self.prog_counter / self.totallength
        self.end_time = datetime.now().time()
        self.process_time = datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.beginning_time)
        self.process_time_no_ms = self.process_time - timedelta(microseconds=self.process_time.microseconds)
        self.time_list.append(self.process_time_no_ms.total_seconds())
        self.avg_time = UpdateProgress.time_avg(self.time_list)
        self.ex_compl = round(self.avg_time * self.totallength / 60) + int(self.minutes)

        # This loop ensures that hours and minutes are displayed accurately, instead of having greater than 60
        # minutes in the hour format
        if self.hours > int(self.psList[0]):
            self.hours -= 1
        if self.ex_compl / 60 >= 1:
            self.ex_compl -= 60
            self.hours += 1
            if self.ex_compl / 60 >= 1:
                self.ex_compl -= 60
                self.hours += 1
                if self.ex_compl / 60 >= 1:
                    self.ex_compl -= 60
                    self.hours += 1
                    if self.ex_compl / 60 >= 1:
                        self.ex_compl -= 60
                        self.hours += 1
                        if self.ex_compl / 60 >= 1:
                            self.ex_compl -= 60
                            self.hours += 1
                            if self.ex_compl / 60 >= 1:
                                self.ex_compl -= 60
                                self.hours += 1
                                if self.ex_compl / 60 >= 1:
                                    self.ex_compl -= 60
                                    self.hours += 1
                                    if self.ex_compl / 60 >= 1:
                                        self.ex_compl -= 60
                                        self.hours += 1
                                        if self.ex_compl / 60 >= 1:
                                            self.ex_compl -= 60
                                            self.hours += 1
                                            if self.ex_compl / 60 >= 1:
                                                self.ex_compl -= 60
                                                self.hours += 1

    # This function is called each time to make sure the progress is in float format, and will return
    # an error if notd
    def float_check(self):
        # verifies that the status is a float, and returns an error if not
        if isinstance(self.progress, int):
            self.progress = float(self.progress)
        if not isinstance(self.progress, float):
            self.progress = 0
            status = "error: progress var must be float\r\n"
            sys.stdout.write(status)
            sys.stdout.flush()


    def update_1(self, special_char=''):
        UpdateProgress.float_check(self)
        if not self.first_pass:
            UpdateProgress.complete(self)
        if self.progress < 0:
            self.progress = 0
            status = "Halt...\r\n"
        if self.progress == 0 and self.avg_time is None:
            status = f"INSERT TEXT FOR ACTION ON {special_char}..."
        elif 0 < self.progress < 1:
            status = f"INSERT TEXT FOR ACTION ON {special_char}... Averaging {self.avg_time} seconds per ticker, " \
                     f"expected completion is {self.hours}:{self.ex_compl:02d}. "
        if self.progress >= 1:
            self.progress = 1
            status = "Done...\r\n"
        block = int(round(self.barLength * self.progress))
        text = "\rProgress: [{0}] {1}% {2}".format(self.barLengthcharacter * block + "-" * (self.barLength - block),
                                                   round(self.progress * 100, 2), status)
        sys.stdout.write(text)
        sys.stdout.flush()


    def update_2(self, special_char=''):
        UpdateProgress.float_check(self)
        if not self.first_pass:
            UpdateProgress.complete(self)
        if self.progress < 0:
            self.progress = 0
            status = "Halt...\r\n"
        if self.progress == 0 and self.avg_time is None:
            status = f"DIFFERENT TEXT FOR ACTION ON {special_char}..."
        elif 0 < self.progress < 1:
            status = f"DIFFERENT TEXT FOR ACTION ON {special_char} data... Averaging {self.avg_time} seconds per ticker, " \
                     f"expected completion is {self.hours}:{self.ex_compl:02d}. "
        if self.progress >= 1:
            self.progress = 1
            status = "Done...\r\n"
        block = int(round(self.barLength * self.progress))
        text = "\rProgress: [{0}] {1}% {2}".format(self.barLengthcharacter * block + "-" * (self.barLength - block),
                                                   round(self.progress * 100, 2), status)
        sys.stdout.write(text)
        sys.stdout.flush()


    def update_3(self, special_char=''):
        UpdateProgress.float_check(self)
        if not self.first_pass:
            UpdateProgress.complete(self)
        if self.progress < 0:
            self.progress = 0
            status = "Halt...\r\n"
        if self.progress == 0 and self.avg_time is None:
            status = f"THIRD TEXT FOR ACTION ON {special_char}..."
        elif 0 < self.progress < 1:
            status = f"THIRD TEXT FOR ACTION ON {special_char} data...Averaging {self.avg_time} seconds per ticker, " \
                     f"expected completion is {self.hours}:{self.ex_compl:02d}. "
        if self.progress >= 1:
            self.progress = 1
            status = "Done...\r\n"
        block = int(round(self.barLength * self.progress))
        text = "\rProgress: [{0}] {1}% {2}".format(self.barLengthcharacter * block + "-" * (self.barLength - block),
                                                   round(self.progress * 100, 2), status)
        sys.stdout.write(text)
        sys.stdout.flush()

