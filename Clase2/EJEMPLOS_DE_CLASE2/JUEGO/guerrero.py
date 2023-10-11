from servivo import SerVivo
import random

def generaIntAleatorio(a,b):
	return random.randint(a,b)

class Guerrero(SerVivo):

	__max_target = 10

	def __init__(self,name):
		SerVivo.__init__(self)

		self._target = self.__generateTargetToDie()
		self._name   = name

	def get_name(self):
		return self._name
		# no se crea un set porgue los guerreros no pueden cambiar de nomber
		'''
		def set_name(self,name):
			reutrn self._name = name
		'''
	def get_target(self):
		return self._target

	def shoot(self):
		'''
		Shoot if the warrior is alive generating a randome number between 0 an the __max_target
		: returns the number to shoot if the warrior is alive, -1 otherwise
		'''
		if (self._vivo):
			shot  = generaIntAleatorio(0,Guerrero.__max_target)
			print(self._name + " dispara " + str(shot))
			return shot
		else:
			return -1

	def get_shot(self,shot):
		'''
		If the target is guessed by the shoot, then the warrior dies.
		: param shoot: int with the shoot against the soldier
		;return True if the shot kills the warrior(shot is the target and the warrior is alive), False otherwise
		'''
		isTarget= False
		if (self._vivo == True and self._target==shot):
			self._vivo = False # The SerVivoDIES!
			isTarget   = True
			print(self._name + " se muere por el disparo " + str(shot) )
		return isTarget

	def __generateTargetToDie(self):
		'''
		Private Method to generate the target to get shot
		'''
		return generaIntAleatorio(0,Guerrero.__max_target)
	'''TODO IF NEEDED OVERRIDE METHODS EQUALITY, COMPARISON, HASH,ETC.
	'''

	def __str__(self):
		'''Override method toString to identify the objects and know their states 
		'''
		return self._name
	
	@staticmethod
	def get_maxTarget(): 
 		return Guerrero.__max_target