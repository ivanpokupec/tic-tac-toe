""" This is a program demonstrating the minimax algorithm for a tic-tac-toe game """
import operator

state = [0] * 9 # a field of value 'x' is x, and 'o' for o
print state

# This function generates states based on the next move
def getAvailableStates(state, turn):
	states = []

	for i in range(9):
		if state[i] == 0:
			copied_state = list(state)
			copied_state[i] = turn
			states.append(copied_state)

	return states

# Checking winning conditions (a little bad, but it suits the needs)
def checkWin(state):
	for i in range(3):
		if state[i*3] == state[i*3 + 1] == state [i*3 + 2] and state[i*3] != 0:
			return state[i*3]
	
		if state[i] == state[i+3] == state [i+6] and state[i] != 0:
			return state[i]

	if state[0] == state[4] == state[8] and state[0] != 0:
		return state[0]
	
	if state[2] == state[4] == state[6] and state[2] != 0:
		return state[2]
		
	if 0 not in state:
		return 0

	return -1

# 1 if x wins, -1 if o wins, 0 for draw
def utility(winner):
	if winner == 'x':
		return 1
	elif winner == 'o':
		return -1
	else:
		return 0

# this is where all the action happens
def minimax(state, turn):
	print max_value(state, turn, 0)

def max_value(state, turn, depth):
	if checkWin(state) != -1:
		return utility(checkWin(state)), state

	next_turn = 'x'
	if turn == 'x':
		next_turn = 'o'
	
	min_values = []
	for available_state in getAvailableStates(state, turn):
		min_values.append(min_value(available_state, next_turn, depth+1))
	
	max_min_value = max(min_values, key=operator.itemgetter(0))
	if depth == 0:
		return max_min_value
	else:
		return max_min_value[0], state

def min_value(state, turn, depth):
	if checkWin(state) != -1:
		return utility(checkWin(state)), state	

	next_turn = 'x'
	if turn == 'x':
		next_turn = 'o'

	max_values = []
	for available_state in getAvailableStates(state, turn):
		max_values.append(max_value(available_state, next_turn, depth+1))

	min_max_value = min(max_values, key=operator.itemgetter(0))
	if depth == 0:
		return min_max_value
	else:
		return min_max_value[0], state
	return min_max_value, state

# some test values
minimax(['x', 'x', 0,
	 'o', 'o', 0,
	 0, 0, 'x'], 'x')
minimax([0, 0, 0, 0, 0, 0, 0, 0, 0], 'x')
minimax(['x', 'o', 'x',
	0, 0, 0,
	0, 'o', 0], 'x')
