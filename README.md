# DigitalLibrary

Digital Library app for storing books in database in order to track your reading progress

The frontend python code for this app contains the TKinter library and uses its methods to create a window, labels and text entries

The backend python code for this app contains the sqlite3 library for creating a database, contains functions for basic commands to add,delete,and update records of books in your library

## Creating own library

Upon cloning this repository on your computer, you can open any text editor with terminal and launch the app with "python3 frontend.py" command

This will create the empty SQLite3 database, where you can easily add your books which you read or didn't read in order not to forget anymore

If you want to make executable version for yourself in order to prevent from launching from terminal you can type:

```
pip install pyinstaller # install the package that creates executables

pyinstaller --onefile --windowed frontend.py # this line will create one filed executable for this app, supported on any OS
```

## Essentials

All text entries can be filled with any number of spaces and be capitalized anywhere, since here insertion goes on with lowering and stripping the strings from any trailing whitespaces

Searching can occur with only one, two, or three entries not filled, in order to allow the client search faster and find the book he accidentally forgot to read

User can also delete the whole library if he already read the books or he wants to fill it with new unread books in his collection, or delete just record by record

Also, when user points or selects some row in listbox, all elements of this row, title, genre, author and status will be filled already for him

## Version 1.0

The version 1.0 is released without any implementation of UI, addition of colors, with basic TKinter window frame, text labels, entries and listbox

As the time progresses and ideas come along, there will be additional updates on the code and the app functioning altogether

If you have any suggestions to improve the app, please don't hesitate to contact me via Telegram, my nickname is on my profile :)


