# Progress-Bar
A progress bar for python loops, fully customizable and very effective.


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
