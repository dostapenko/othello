'''
Created on Feb 19, 2014

@author: gregbocko
'''

from TreeNode import TreeNode
from Board import Board
import random

class OthelloPlayer(object):
    '''
    classdocs
    '''
    

    def __init__(self, color):
        global player_color 
        player_color = color
        
       
    def opponent(self, player):
        "Self explanatory"
        
        if player == 'B': 
            opp = 'W'
        else: 
            opp = 'B'
        return opp

    def heuristic_Function(self, Board):
    	a = random.randint(0,100)
    	headNode = TreeNode(Board, 'B', a)
    	print 'got here at least'
    	a = self.Alpha_Beta(headNode, 0, -1000, 1000, 'B')
    	print 'AB'
    	print a

    #might need to change to B/W or +1/-1
    def minmax_Opposite(self, minmaxvar):
    	if(minmaxvar == 'max'):
    		return 'min'
    	else:
    		return 'max'

    def Cutoff_test(self, state, depth):
    	if(depth >= 4):
    		return True
    	return False

    def Alpha_Beta(self, node, depth, alpha, beta, player):
    	moves = node.access_Board().legal_moves(player)
    	self.create_Children(node, moves, player)

    	if self.Cutoff_test(node, depth):
    		print node.get_moves(player)
    		print player
    		a = [0,[0,0,0,0]]
    		a[0] = node.get_moves(player)
      		return a #node.get_moves(player)
    	best = [None]
    	#handles early pruning
    	#will have to be changed

    	counter = 0
    	children = node.return_All_Children()
    	best = [0, 0, 0 ,0]
    	if(player == 'B'):

    		for i in range(len(children)):
    			
    			#children[i].access_Board().print_board()
    			#moves = child.legal_moves()
    			#child.create_Children(child, moves, player)
    			value = self.Alpha_Beta(children[i], depth+1, alpha, beta, self.opponent(player))
    			print 'coming out and itno depth %i', depth
    			print alpha, value[0], beta
    			#print value
    			#print 'this is alpha1 %i', value
    			#print value
    			#if not (value == None):
	    		if(value[0] > alpha):
	    			#print 'maximizing'
	    			print 'new alpha VALUE', alpha, value[0]
	    			alpha = value[0]
	    			best = value[1]
	    			best[depth] = i
	    		elif(value[0] == alpha):
	    			a = random.randint(0,1)
	    			if(a == 1):
	    				#print depth
	    				alpha = value[0]
	    				best = value[1]
	    				best[depth] = i
	    		if (beta <= alpha):
    				print 'this should never happen2'
    				break
    				#return [None]
    			

    		return alpha, best, children[best[depth]].get_move()
    	else:
    		for i in range(len(children)):

    			#node.access_Board().print_board()
    			#moves = child.legal_moves()
    			#child.create_Children(child, moves, player)
    			value = self.Alpha_Beta(children[i], depth+1, alpha, beta, self.opponent(player))
	    		print 'coming out and itno depth %i', depth
	    		print value
	    		if(value[0] < beta):
	    			print 'new beta VALUE', beta, value[0]
	    			beta = value[0]
	    			print value
	    			best = value[1]
	    			best[depth] = i

	    		elif(value[0] == beta):
	    			a = random.randint(0,1)
	    			if(a == 1):
	    				#print depth
	    				beta = value[0]
	    				best = value[1]
	    				best[depth] = i
	    				#if(depth == 2):
	    				#print 
	    		
    			if (beta <= alpha):
    				print 'this should never happen2'
    				break
    				#return [None]
    			
    		return beta, best, children[best[depth]].get_move()

    '''
    These arent being used anymore but I dont want to get rid of them yet
    def start_Build_Tree(self, Board):
    	a = random.randint(0,100)
    	headNode = TreeNode(Board, 'max', a)
    	moves = Board.legal_moves(player_color)
    	self.create_Children(headNode, moves, player_color)
    	#Board.print_board
    	children = headNode.return_All_Children()
    	#for child in children:
    		#child.access_Board().print_board()

    	self.Alpha_Beta(headNode, 0, -1000, 1000, 'W')


    
    
    def build_Tree(self, node, player_color, level):
    	if(level < 4):
    		Board = node.access_Board
    		moves = Board.legal_moves(player_color)
    		self.create_Children(node, moves, player_color)
    	else:
    		if(node.get_minmax == 'max'):
    			children = node.return_All_Children()
    			for item in children     
    		else:
    

    def create_child(self, board, parentNode, move, player):
    	newBoard = board
    	newBoard = newBoard.make_move(player, move[0], move[1])
    	minmaxvar = self.minmax_Opposite(parentNode.get_minmax())
    	a = random.randint(0,100)
    	newNode = TreeNode(newBoard, minmaxvar, a)
    	parentNode.create_Child(newNode)
    '''
    #creates the children of a node. Takes in moves and modifies a board for each child and creates
    #a new node for each child
    def create_Children(self, parentNode, moves, player):
    	parent = parentNode.access_Board()
    	for item in moves:
    		oldBoard = Board(True,parentNode.get_Board())
    		oldBoard = oldBoard.make_move(player, item[0], item[1])
    		minmaxvar = self.minmax_Opposite(parentNode.get_minmax())
    		a = random.randint(0,100)
    		newNode = TreeNode(oldBoard, minmaxvar, a)
    		newNode.set_move(item)
    		parentNode.create_Child(newNode)


    		
