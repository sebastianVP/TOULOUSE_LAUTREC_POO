from guerrero import Guerrero
class Marciano(Guerrero):
	__totalMarcianosAlive = 0 
	__shotsToKillMarciano = 3

	def __init__(self,name):
		Guerrero.__init__(self,name)
		self.__shotsToReceive = Marciano.__shotsToKillMarciano
		Marciano.__totalMarcianosAlive +=1

	
	def get_shotsToReceive(self):
		return self.__shotsToReceive

	#Overrides the method get_shot from the parent class!
	def get_shot(self,shot):
		'''
		If the target is guessed by the shoot, the warrior dies
		:param shoot: int with the shoot against the soldier
		:returns True if the shot kills the warrior (shot is the target and the warrior is alive, False Otherwisw)
		'''
		isTarget = False
		if (self._vivo== True and self._target== shot):
			self.__shotsToReceive -=1
			isTarget = True
			if (self.__shotsToReceive==0):
				Guerrero.get_shot(self,shot)
				Marciano.__totalMarcianosAlive-=1
		return isTarget

	@staticmethod
	def get_total_marcianos_alive():
		'''
		returns the toital number of Marcianos alive
		'''
		return Marciano.__totalMarcianosAlive

	@staticmethod
	def get_shotsToKillAMarciano():
		'''
		:returns the shots needed to kill a marciano
		'''
		return Marciano.__shotsToKillMarciano


