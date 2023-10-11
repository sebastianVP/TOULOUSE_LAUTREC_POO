# REQUERIMIENTOS
'''
1. GUERRA FICTICIA 2 NAVES
2. UNA DE MARCIANOS 
3. UNA DE TERRICOLAS
4. -AMBOS BANDO O NAVES VAN DISPARANDO, 
   -SI ACIERTA A ALGUN COMPONENTE DE LA OTRA NAVE LO MATA
	GENERANDO NUMEROS ALEATORIOS EN CADA DISPARO
5. DIAGRAMA DE OBJETOS QUE DIALOGAN ENTRE SI
'''

from guerrero import Guerrero
from nave import Nave
class Guerra(): 
	def __init__(self, numTerricolas=3, numMarcianos=3):
		self.__terricolasNave = Nave("Guerreros.TERRICOLA", "Millenium Falcon", numTerricolas) 
		self.__marcianosNave = Nave("Guerreros.MARCIANO", "Wing X", numMarcianos) 
 
	def start_war(self):
		numTerricolasInNave = self.__terricolasNave.number_of_members()
		numMarcianosInNave = self.__marcianosNave.number_of_members() 
		if(numTerricolasInNave >= numMarcianosInNave): 
			max_shots = numTerricolasInNave 
		else: 
			max_shots = numMarcianosInNave 
		while(self.are_members_in_both_crews()): 
			for warrior in range (0,max_shots): 
				if(warrior < numTerricolasInNave and self.__terricolasNave.isWarriorAlive(warrior)): 
					shot = self.__terricolasNave.shoot(warrior) 
					self.__marcianosNave.get_shot(shot) 
				if(warrior < numMarcianosInNave and self.__marcianosNave.isWarriorAlive(warrior)): 
					shot = self.__marcianosNave.shoot(warrior) 
					self.__terricolasNave.get_shot(shot) 
		if (self.__terricolasNave.membersAlive() > 0): 
			print("Todos los Marcianos murieron")
			return 0 
		elif (self.__marcianosNave.membersAlive() > 0):
			print("Todos los Terricolas muerieron") 
			return 1 
		else: 
			raise Exception 

	def are_members_in_both_crews(self):
		if( (self.__terricolasNave.membersAlive()) > 0 and (self.__marcianosNave.membersAlive()) > 0): 
			return True
		else: 
			return False

def main():
	g1_galaxia=Guerra(4,1)
	g1_galaxia.start_war()

if __name__=="__main__":
 	main()	