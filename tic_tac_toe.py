import tkinter as tk

class TicTacToe(tk.Tk) :
	def __init__(self, size, nbCell) :
		tk.Tk.__init__(self)
		self.initVisu(size)
		self.initGrid(nbCell)

		self.playerTurn = 0
		self.gridCellSize = int(self.canva.cget("height"))/3
		self.nbFreeCell = nbCell*nbCell
		self.finish = False

		self.bind("<Escape>", self.stop)

		if (self.nbFreeCell > 0 and not self.finish) :
			self.canva.bind("<Button-1>", self.addValueGrid)

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

	def initGrid(self, nbCell) :
		self.grid = []
		for i in range(nbCell) :
			self.grid.append([])
			for j in range(nbCell) :
				self.grid[i].append(-1)
				
	def addValueGrid(self, clic) :
		print("test")
		(x, y) = self.posGridClic(clic)

		if (self.grid[x][y] == -1) :
			if (self.playerTurn == 0) :
				self.addCross(x, y)
			else :
				self.addCircle(x, y)

			self.grid[x][y] = self.playerTurn

			self.nbFreeCell -= 1

			if not self.checkIfWin(self.playerTurn) :

				self.playerTurn = (self.playerTurn+1)%2
			else :
				self.finish = True
			

	def posGridClic(self, clic) :
		x = int(clic.x/self.gridCellSize)
		y = int(clic.y/self.gridCellSize)

		return (x, y)

	def checkIfWin(self, lastInsert) :
		if (self.grid[0][0] == lastInsert and self.grid[0][1] == lastInsert and self.grid[0][2] == lastInsert) or \
			(self.grid[1][0] == lastInsert and self.grid[1][1] == lastInsert and self.grid[1][2] == lastInsert) or \
			(self.grid[2][0] == lastInsert and self.grid[2][1] == lastInsert and self.grid[2][2] == lastInsert) or \
			(self.grid[0][0] == lastInsert and self.grid[1][0] == lastInsert and self.grid[2][0] == lastInsert) or \
			(self.grid[0][1] == lastInsert and self.grid[1][1] == lastInsert and self.grid[2][1] == lastInsert) or \
			(self.grid[0][2] == lastInsert and self.grid[1][2] == lastInsert and self.grid[2][2] == lastInsert) or \
			(self.grid[0][0] == lastInsert and self.grid[1][1] == lastInsert and self.grid[2][2] == lastInsert) or \
			(self.grid[0][2] == lastInsert and self.grid[1][1] == lastInsert and self.grid[2][0] == lastInsert) :
			return True
		return False


	def stop(self, escape) :
		self.quit()

if __name__ == "__main__" :
	app = TicTacToe(600, 3)
	app.title("Tik tak toe")
	app.mainloop()