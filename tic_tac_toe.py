import tkinter as tk
import time
import random

class TicTacToe(tk.Tk) :
	def __init__(self, size, nbCell) :
		tk.Tk.__init__(self)
		self.initVisu(size)

		self.gridCellSize = int(self.canva.cget("height"))/nbCell
		self.nbFreeCell = nbCell*nbCell
		self.nbCell = nbCell

		self.initGrid()

		self.player1Value = 0
		self.player2Value = 1
		self.playerTurn = self.player1Value
		self.isIaSecondPlayer = True

		self.bind("<Escape>", self.stop)
		self.canva.bind("<Button-1>", self.play)

	def initVisu(self, size) :
		self.canva = tk.Canvas(self, bg = "red", height = size, width = size)
		
		self.canva.create_line(0, size/3, size, size/3)
		self.canva.create_line(0, 2*size/3, size, 2*size/3)
		self.canva.create_line(size/3, 0, size/3, size)
		self.canva.create_line(2*size/3, 0, 2*size/3, size)

		self.canva.pack()

	def addCross(self, x, y) :
		x *= self.gridCellSize
		y *= self.gridCellSize

		self.canva.create_line(x+self.gridCellSize/6, y+self.gridCellSize/6, x+5*self.gridCellSize/6, y+5*self.gridCellSize/6)
		self.canva.create_line(x+5*self.gridCellSize/6, y+self.gridCellSize/6, x+self.gridCellSize/6, y+5*self.gridCellSize/6)

	def addCircle(self, x, y) :
		x *= self.gridCellSize
		y *= self.gridCellSize

		self.canva.create_oval(x+self.gridCellSize/6, y+self.gridCellSize/6, x+5*self.gridCellSize/6, y+5*self.gridCellSize/6)
		self.canva.create_oval(x+5*self.gridCellSize/6, y+self.gridCellSize/6, x+self.gridCellSize/6, y+5*self.gridCellSize/6)

	def initGrid(self,) :
		self.grid = []
		for i in range(self.nbCell) :
			self.grid.append([])
			for j in range(self.nbCell) :
				self.grid[i].append(-1)
				
	def addValueGrid(self, clic) :
		(x, y) = self.posGridClic(clic)

		if (self.grid[x][y] == -1) :
			if (self.playerTurn == 0) :
				self.addCross(x, y)
			else :
				self.addCircle(x, y)

			self.grid[x][y] = self.playerTurn

			self.nbFreeCell -= 1

			return True
		return False
			

	def posGridClic(self, clic) :
		x = int(clic.x/self.gridCellSize)
		y = int(clic.y/self.gridCellSize)

		return (x, y)

	def checkIfWin(self) :
		return (self.grid[0][0] == self.playerTurn and self.grid[0][1] == self.playerTurn and self.grid[0][2] == self.playerTurn) or \
			(self.grid[1][0] == self.playerTurn and self.grid[1][1] == self.playerTurn and self.grid[1][2] == self.playerTurn) or \
			(self.grid[2][0] == self.playerTurn and self.grid[2][1] == self.playerTurn and self.grid[2][2] == self.playerTurn) or \
			(self.grid[0][0] == self.playerTurn and self.grid[1][0] == self.playerTurn and self.grid[2][0] == self.playerTurn) or \
			(self.grid[0][1] == self.playerTurn and self.grid[1][1] == self.playerTurn and self.grid[2][1] == self.playerTurn) or \
			(self.grid[0][2] == self.playerTurn and self.grid[1][2] == self.playerTurn and self.grid[2][2] == self.playerTurn) or \
			(self.grid[0][0] == self.playerTurn and self.grid[1][1] == self.playerTurn and self.grid[2][2] == self.playerTurn) or \
			(self.grid[0][2] == self.playerTurn and self.grid[1][1] == self.playerTurn and self.grid[2][0] == self.playerTurn)


	def isFinish(self) :
		return self.checkIfWin() or self.nbFreeCell <= 0

	def play(self, event) :
		if (self.addValueGrid(event)) :

			if not self.isFinish() :
				self.playerTurn = (self.playerTurn+1)%2

				if (self.isIaSecondPlayer and self.playerTurn == self.player2Value) :
					(event.x, event.y) = self.iaPosition()
					(event.x, event.y) = (event.x*self.gridCellSize + self.gridCellSize/2, event.y*self.gridCellSize + self.gridCellSize/2)

					self.play(event)
			else :
				self.canva.unbind("<Button-1>")
				if (self.checkIfWin()) :
					print("Joueur : ", self.playerTurn, " a gagné !")
				else :
					print("Egalité !")
	
	def iaPosition(self) :
		return self.iaRandomPosition()
	
	def iaRandomPosition(self) :
		while (self.nbFreeCell > 0) :
			(x, y) = (random.randint(0, self.nbCell-1), random.randint(0, self.nbCell-1))

			if (self.grid[x][y] == -1) :
				break
		
		return (x, y)

	def stop(self, escape) :
		self.quit()

if __name__ == "__main__" :
	app = TicTacToe(600, 3)
	app.title("Tik tak toe")
	app.mainloop()