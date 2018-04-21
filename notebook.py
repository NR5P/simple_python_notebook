import datetime

id = 0

class Note:
	"""for each individual note"""
	
	def __init__(self, memo):
		self.memo = memo
		self.creation_date = datetime.date.today()
		global id
		id += 1
		self.id = id
		
	def search(self, search_terms):
		return search_terms in self.memo 
		
		
class Notebook:
	
	def __init__(self):
		self.notes = []
		
	def new_note(self, memo):
		self.notes.append(Note(memo))

	def modify(self, id):
		self._find_note_by_id(note_id).memo = memo
				
	def search(self, search_terms):
		return [note for note in self.notes if
				note.search(search_terms)]
				
	def _find_note_by_id(self, note_id):
		for note in self.notes:
			if note.id == id:
				return note
			return None
