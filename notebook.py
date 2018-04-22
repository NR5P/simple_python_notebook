import datetime
import pickle


class Note:
	"""for each individual note"""

	note_id = 0
	
	def __init__(self, memo):
		self.memo = memo
		self.creation_date = datetime.date.today()
		Note.note_id += 1
		self.id = self.note_id
		
	def search(self, search_terms):
		return search_terms in self.memo 
		
		
class Notebook:
	
	def __init__(self):
		self.notes = []
		
	def new_note(self, memo):
		self.notes.append(Note(memo))

	def modify(self, note_id, memo):
		self._find_note_by_id(note_id).memo = memo
				
	def search(self, search_terms):
		return [note for note in self.notes if
				note.search(search_terms)]
				
	def _find_note_by_id(self, note_id):
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note

	def save(self):
		file = open("notes", "wb")
		pickle.dump(self.notes, file)
		file.close()

	def get_file(self):
		try:
			file = open("notes", "rb")
			self.notes = pickle.load(file)
			file.close
		except:
			self.save()

