import numpy as np
import random
no_Queens = 12
boards = None
each_board_survival = []
selected_boards = []
max_fitness = 12
alpha = .01

class BoardSetup:
	def __init__(self):
		self.fitness = None
		self.position = None
	def set_fitness(self, fitness):
		self.fitness = fitness
	def set_position(self, value):
		self.position = value
	def print_board(self):
		return {'fitness': fitness, 
				'position' : position}



def survival_probability(boards):
		#since boards are numpy array, find sum of fitness for  each board
			global each_board_survival
			
			total_fitness = np.sum([i.fitness for i in boards])
			
		#survival probability =(individual fitness / total fitness)
			for i in boards:
				survival_probability = (i.fitness/total_fitness)
				each_board_survival.append(survival_probability)

			#print ('board survival', each_board_survival)
		### use the Roulette wheel to select 
			#roulette_wheel(boards)



def generate_fitness(board):
	# max fitness for 4 queens is 12
	global max_fitness
	clash = 0
	#if the sequence has two similar values means two 
	#queens are in the same row
	clash_row = abs(len(board) - len(np.unique(board)))
	clash += clash_row
	
	for i in range (len(board)):
		for j in range (len(board)):
			if (i != j):
				x_axis = abs(i - j)
				y_axis = abs(board[i] - board[j])
				if (x_axis == y_axis):
					clash +=1
	
	#fitness is max_fitness - total clashes
	fitness = max_fitness - clash
	return fitness

def generate_initial_position():
	global no_Queens
	#use numpy arrray to generate 4 queens
	initial_position = np.arange(no_Queens)
	#randomize the queens on the board
	np.random.shuffle(initial_position)
	print ('initial_position', initial_position)
	return initial_position

def generate_boards(total_boards ):
	global boards
	#boards have fitness and position attribute
	boards = [BoardSetup() for i in range(total_boards)]
	for i in range(total_boards):
		#create board sequence and randomize it
		boards[i].set_position(generate_initial_position())
		#get firness for each board
		boards[i].set_fitness(generate_fitness(boards[i].position))
	return boards

def roulette_wheel(boards):
	sum = 0.0
	global selected_boards
	for j in range (len(boards)):
		arrow = random.random()
		#print ('arrow', arrow)
		for i in range(len(each_board_survival)): # 0 to 8
			global selected_boards
			#print ('count', i)
			if ((arrow >= sum) and (arrow < (sum + each_board_survival[i]))):
				selected_boards.append(i)
				break
			else:
				sum += each_board_survival[i]
		sum = 0.0
	print ('len of seleccted boards',len(selected_boards))
	print ('selected boards', selected_boards)
	temp_boards =  [BoardSetup() for i in range(len(boards))]

	for i in range (len(boards)):
		temp_boards[i].position = boards[i].position
	'''for i in range (len(temp_boards)):
					print ('temp boards', temp_boards[i].position)
			'''
	for i in range(len(selected_boards)):
		boards[i].position = temp_boards[selected_boards[i]].position
	for i in range (len(boards)):
		print ('next_generation', i, boards[i].position)

def mating( ):
	mating_list = [0]* 10
	for i in range (len(mating_list)):
		mating_list[i] = i
	random.shuffle(mating_list)
	print('mating_list', mating_list)
	#making pairs
	return mating_list
	#crossover(mating_list


def crossover(mating_list):
	global boards
	crossover_point = random.randint(0, (no_Queens -1) )
	print ('crossover_point', crossover_point)
	
	for i in range(0, len(mating_list), 2): # 0 to 9
		for j in range(crossover_point, no_Queens): # crossover point to 3
			temp = boards[mating_list[i]].position[j]
			#print ('temp', temp)
			boards[mating_list[i]].position[j] = boards[mating_list[i + 1]].position[j]
			#print (boards[mating_list[i]].position[j])
			boards[mating_list[i + 1]].position[j] = temp
			temp = 0
	for i in range (len(boards)):
		print ('mated boards:' ,i, boards[i].position)


def start_genetic_algorithm(boards):
	#boards = generate_boards(size)
	survival_probability(boards)
	roulette_wheel(boards)
	mating_list = mating()
	crossover(mating_list)


	

if __name__ == '__main__':
	size = 10 #size of boards
	boards = generate_boards(size)
	new_boards = start_genetic_algorithm(boards)




	'''def finish():
		global boards
		board_fitness = [board.fi
		tness for board in boards]
		if ((iterations == 10) or board_fitness == max_fitness):
			return True
			print (board_fitness)
		else:
			False

	if __name__ == '__main__':
		size = 10 #size of boards
		boards = generate_boards(size)
		iterations = 10
		while not finish():
			new_boards = start_genetic_algorithm(boards)
			iterations += 1
		print ('program ended')		'''

