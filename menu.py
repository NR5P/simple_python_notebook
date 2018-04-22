import os
from notebook import Notebook, Note
import pickle

class Menu(Notebook):
	
	def __init__(self):
		super().__init__()
		self.choices = {
				"1" : self.show_notes,
				"2" : self.search_notes,
				"3" : self.add_note,
				"4" : self.modify_note,
				"5" : self.delete_note,
				"6" : self.quit
				}

	def display_menu(self):
		print("""
Menu

1. Show all notes
2. Search notes
3. Add note
4. Modify note
5. delete note
6. Quit
""")

	def run(self):
		self.get_file()
		try:
			Note.note_id = self.notes[-1].id
		except:
			pass
		while True:
			self.display_menu()
			choice = input("enter option number: ")
			try:
				action = self.choices.get(choice)  
				action()
			except:
				print("INVALID CHOICE")


	def show_notes(self, notes=None):
		if not notes:
			notes = self.notes
		for note in notes:
			print("{} : {}\n{}\n\n".format(note.id, note.creation_date.strftime("%b/%d/%Y"), note.memo))
		if not notes:
			print("NO NOTES")

	def search_notes(self):
		search_items = input("search for: ")
		notes = self.search(search_items)
		self.show_notes(notes)

	def add_note(self):
		memo = input("enter note: ")
		self.new_note(memo)
		self.save()
		print("your note has been added")

	def modify_note(self):
		note_id = input("enter a note id: ")
		memo = input("enter new note: ")
		if memo:
			self.modify(note_id, memo)
			self.save()

	def delete_note(self):
		note_id = input("enter a note id: ")
		self.notes.remove(self._find_note_by_id(note_id))
		self.save()


	def quit(self):
		print("bye")
		os._exit(0)

if __name__ == "__main__":
	Menu().run()
