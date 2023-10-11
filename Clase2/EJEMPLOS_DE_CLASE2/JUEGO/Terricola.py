from guerrero import Guerrero
from marciano import Marciano
import random
def generaIntAleatorio(a,b):
	return random.randint(a,b)

class Terricola(Guerrero):
	__totalTerricolasAlive =0
	__shots_done = [0]*(Guerrero.get_maxTarget()+1)

	def __init__(self, name): 
		Guerrero.__init__(self, name) 
		Terricola.__totalTerricolasAlive += 1 
	# Overrides the method shoot from the parent class! 
	def shoot(self): 
		''' 
		Shoot if the Terricola is alive generating a random number between 
		0 and the __max_target 
		It shoots a number of times equals to the number of shoots that a 
		Marciano can hold 
		:returns the number to shoot if the warrior is alive, -1 otherwise 
		''' 
		if(self._vivo):
			shot = generaIntAleatorio(0,Guerrero.get_maxTarget()) 
			while(Terricola.__shots_done[shot] >= Marciano.get_shotsToKillAMarciano()): 
				shot = generaIntAleatorio(0,Guerrero.get_maxTarget()) 
			Terricola.__shots_done[shot] += 1 
			print(self._name + " shoot " + str(shot) + " for " + str(Terricola.__shots_done[shot]) + " time") 
			return shot 
		else: 
			return -1 
	# Overrides the method get_shot from the parent class! 
	def get_shot(self, shot): 
		''' 
		If the target is guessed by the shoot, then the warrior dies. 
		:param shoot: int with the shoot against the soldier 
		:returns True if the shot kills the warrior (shot is the target and 
		the warrior is alive), False otherwise 
		''' 
		isTarget = Guerrero.get_shot(self,shot) 
		if(self._vivo): 
			Terricola.__totalTerricolasAlive -= 1 #cambio
		return isTarget 
	@staticmethod 
	def get_total_Terricolas_alive(): 
		''' 
		:returns the total number of Terricolas alive 
		''' 
		return Terricola.__totalTerricolasAlive 
	@staticmethod 
	def get_total_shots_done(shoot): 
		''' 
		:returns the total number of Terricolas alive 
		''' 
		if(not isinstance(shoot,int)): 
			raise TypeError("shoot should be an int") 
		elif(shoot < 0 or shoot > Guerrero.get_maxTarget()): 
			raise ValueError("shoot OUT OF RANGE") 
		return Terricola.__shots_done[shoot] 