class bankAccount:

	def __init__(self,IDcode,Name):
			self.setID(IDcode)
			self.setName(Name)
			self.setBalance(0)
			self.setNext(None)
			self.setPrevious(None)
		
	def getID(self):
			return self._id

	def getName(self):
			return self._name

	def getBalance(self):
			return self._balance

	def getNext(self):
			return self._next

	def getPrevious(self):	
			return self._prev

	def setID(self,ID):
		self._id = ID

	def setName(self,name):
		self._name = name
	
	def setBalance(self,balance):
		self._balance = balance

	def	setNext(self,next):
		self._next = next

	def setPrevious(self,prev):
		self._prev = prev

class doubleLinkedList:

	def __init__(self):
		self._head = None
		self._tail = None

#Add the new account 

	def add(self,IDcode,Name):
		newest = bankAccount(IDcode,Name)
		newest.setNext(self._head)
		if self._head == None:
			self._tail = newest
		if self._head != None:
			newest.getNext().setPrevious(newest) 
		self._head = newest	

	#Delete the account

	def delete(self,code):
		iterator = self._head
		if iterator.getID() == code and iterator == self._head:
			self._head = iterator.getNext()
			iterator = iterator.getNext().setPrevious(None)
			iterator = self._head
		elif self._head.getID() == code and self._tail.getID() == code and self._head == self._tail:
			self._head = None
			self._tail = None	
		while iterator != None:
			if iterator.getID() == code and iterator != self._tail:
				iterator = iterator.getPrevious().setNext(iterator.getNext())
				break		
			elif iterator.getID() == code and iterator == self._tail:
				self._tail = iterator.getPrevious()
				iterator = iterator.getPrevious().setNext(None)
				break

			iterator = iterator.getNext()	
			
	def bubbleSort(self):
		stop = self._tail
		nextStop = None
		while stop != self._head:
			iterator = self._head
			while iterator != stop:
				if iterator.getNext() == stop:
					nextStop = iterator
				if iterator.getID() > iterator.getNext().getID():
					tmpID = iterator.getID()
					tmpName = iterator.getName()
					tmpBalance = iterator.getBalance()
					iterator.setID(iterator.getNext().getID()) 
					iterator.setName(iterator.getNext().getName()) 
					iterator.setBalance(iterator.getNext().getBalance()) 
					iterator.getNext().setID(tmpID)
					iterator.getNext().setName(tmpName)
					iterator.getNext().setBalance(tmpBalance)

				iterator = iterator.getNext()

			stop = nextStop				

	def display(self):
		iterator = self._head
		while iterator != None:
			print(str(iterator.getID()) + ":" + iterator.getName() + " " + str(iterator.getBalance()))
			iterator = iterator.getNext()
	
#Put the money on balance from the certain account

	def deposit(self,IDcode,Ammount):
		iterator = self._head
		while iterator != None:
			if iterator.getID() == IDcode:
				iterator = iterator.setBalance(int(iterator.getBalance()) + int(Ammount))
				break
			iterator = iterator.getNext()	

#Take the money from balance from the certain account and give an error if there is lack of money

	def withDraw(self,IDcode,Ammount):			
		iterator = self._head
		while iterator != None:
			if iterator.getID() == IDcode and int(iterator.getBalance()) - int(Ammount) >= 0:
				iterator = iterator.setBalance(int(iterator.getBalance()) - int(Ammount))	
				break
			elif iterator.getID() == IDcode and int(iterator.getBalance()) - int(Ammount) < 0:
				print("Not possible to make a transaction at the account id: " + str(iterator.getID()))
				break
			iterator = iterator.getNext()	
