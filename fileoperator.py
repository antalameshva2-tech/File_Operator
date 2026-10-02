# Project: Personal Journal Manager (File Operator)
#
# File modes used:
#   "x" -> create a new file
#   "a" -> add entry at the end (old entries stay safe)
#   "r" -> read the file (view and search)
#   "w" -> erase everything written in the file (used in Delete All)

import os
import time
from datetime import datetime


class JournalManager:

    def __init__(self):
        # entries are stored in a text file named journal.txt
        self.filename = "journal.txt"

    # 1. Add a New Entry
    def add_entry(self):
        print("\nEnter your journal entry:")
        text = input()

        # empty entry is not allowed
        if text.strip() == "":
            print("\nOutput:")
            print("Error: Entry cannot be empty. Please write something and try again.")
            return

        # every entry has a timestamp + user input
        timestamp = time.time()                       # timestamp (seconds since 1970)
        time_now = datetime.fromtimestamp(timestamp)  # timestamp -> date and time
        time_text = str(time_now)[:19]                # "YYYY-MM-DD HH:MM:SS"

        try:
            # create the file if it is not there
            if not os.path.exists(self.filename):
                file = open(self.filename, "x")
                file.close()

            # add the entry at the end of the file
            file = open(self.filename, "a")
            file.write("[" + time_text + "]\n")
            file.write(text + "\n\n")
            file.close()

            print("\nEntry added successfully!")
        except PermissionError:
            print("\nOutput:")
            print("Error: Permission denied. Please check the file permissions.")

    # 2. View All Entries (only today's entries are shown)
    def view_entries(self):
        try:
            file = open(self.filename, "r")
            data = file.read()
            file.close()

            # today's date from the timestamp: "YYYY-MM-DD"
            today = str(datetime.fromtimestamp(time.time()))[:10]

            entries = []
            for e in data.strip().split("\n\n"):
                if e.startswith("[" + today):
                    entries.append(e)

            if len(entries) > 0:
                entries.reverse()               # latest entry on top

                print("\nOutput (If the file exists):")
                print("Your Journal Entries:")
                print("-" * 33)
                print("\n\n".join(entries))

            print("\nOutput (If the file does not exist):")
            print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print("\nOutput (If the file does not exist):")
            print("No journal entries found. Start by adding a new entry!")
            print("\nOutput:")
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("\nOutput:")
            print("Error: Permission denied. Please check the file permissions.")

    # 3. Search for an Entry
    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()

        # empty keyword is not allowed
        if keyword == "":
            print("\nOutput:")
            print("Error: Keyword cannot be empty. Please enter a word or a date (YYYY-MM-DD).")
            return

        try:
            file = open(self.filename, "r")
            data = file.read()
            file.close()

            entries = data.strip().split("\n\n")
            entries.reverse()

            found = []
            for e in entries:
                if keyword.lower() in e.lower():
                    found.append(e)

            if len(found) > 0:
                print("\nOutput (If a match is found):")
                print("Matching Entries:")
                print("-" * 33)
                print("\n\n".join(found))

            print("\nOutput (If no match is found):")
            print("No entries were found for the keyword: " + keyword + ".")

        except FileNotFoundError:
            print("\nOutput:")
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("\nOutput:")
            print("Error: Permission denied. Please check the file permissions.")

    # 4. Delete All Entries (entries are erased, file stays)
    def delete_entries(self):
        # nothing to delete if file is missing or empty
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")
            return

        answer = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()

        if answer == "yes":
            try:
                file = open(self.filename, "w")      # "w" erases everything inside
                file.close()

                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")
                print("\nOutput (If the file does not exist):")
                print("No journal entries to delete.")
            except PermissionError:
                print("\nOutput:")
                print("Error: Permission denied. Please check the file permissions.")
        elif answer == "no":
            print("\nDelete cancelled.")
        else:
            print("\nOutput:")
            print("Invalid input. Please type yes or no.")

    # Menu
    def show_menu(self):
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

    # Main loop
    def run(self):
        # program works only with text files (.txt)
        if not self.filename.endswith(".txt"):
            print("Error: This program works only with text files (.txt).")
            return

        while True:
            self.show_menu()
            print("\nUser Input:")
            choice = input().strip()

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entries()
            elif choice == "3":
                self.search_entry()
            elif choice == "4":
                self.delete_entries()
            elif choice == "5":
                print("\nOutput:")
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("\nOutput:")
                print("Invalid option. Please select a valid option from the menu.")


# Create object and start the program
journal = JournalManager()
journal.run()