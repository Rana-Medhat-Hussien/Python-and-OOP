#from person import person
class person:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

   # getter method
    def get_health(self):
        return self.health
    def get_energy(self):
        return self.energy

    # setter method
    def set_health(self,health):
         self.health = health

    def set_energy(self,energy):
        self.energy = energy
# #####################################################################################################
#reduce the power of voldmort
Power_voldmort = {
    'avadakedavra':100,
    'crucio' : 40,
    'imperio': 20,
    'shield' : 0,
    'taboo': 80,
    'expulso': 60,
    'confringo': 55,

}
#reduce the power of harry
Power_harry = {
        'avadakedavra': 100,
        'crucio': 40,
        'imperio': 20,
        'shield': 0,
        'reducto': 60,
        'fiendfyrre': 50,
        'nebulus': 40,
}
#----------------------------------------------------------------------------------------------
def main():
    harry = person(100, 500)
    voldmort = person(100, 500)
    flag=1
    lst = []
    #first case the health not decrease
    #to concatenate in the same line
    lst = [item for item in input("Enter The two spells (harry then voldmort): ").split()]
    search1 = lst[0].lower()
    search2 = lst[1].lower()
##########################################1st for#######################################################
    # decrease from voldmort
    for k, v in Power_voldmort.items():
        if (k == search2):
            if (search2 == 'imperio'):
                voldmort_energy = voldmort.get_energy() - v
                harry_energy = harry.get_energy() - v
                voldmort.set_energy(voldmort_energy)
                harry.set_energy(harry_energy)
                print("Test both Increase")
                print(voldmort.get_energy())
                print(harry.get_energy())
                break
            else:
                voldmort_energy = voldmort.get_energy() - v
                voldmort.set_energy(voldmort_energy)
                print("energy of voldmort " + str(voldmort.get_energy()))
                break

##############################2nd For ##########################3
    # decrease from harry
    for key, value in Power_harry.items():
        if (key == search1):
                harry_energy = harry.get_energy() - value
                harry.set_energy(harry_energy)
                print("energy of harry " + str(harry.get_energy()))
                break
    #print health from harry and voldmort
    print("health of voldmort " + str(voldmort.get_health()))
    print("health of harry " + str(harry.get_health()))
    lst.clear()
########################## #in other cases#####################################################################333
    while (flag):

        lst = [item for item in input("Enter The two spells (harry then voldmort): ").split()]

        #not case sensitive
        search1 = lst[0].lower()
        search2 = lst[1].lower()

        #decrease from voldmort
        for k, v in Power_voldmort.items():
            if (k == search2):
                #case if the input imperio so he should decrease from both
                    if (search2 == 'imperio'):
                        voldmort_energy = voldmort.get_energy() - v
                        harry_energy = harry.get_energy() - v
                        voldmort.set_energy(voldmort_energy)
                        harry.set_energy(harry_energy)
                        print("energy of voldmort " + str(voldmort.get_energy()))
                        print("energy of harry " + str(harry.get_energy()))
                        break
                    else:
                         voldmort_energy = voldmort.get_energy() - v
                         voldmort.set_energy(voldmort_energy)
                         print("energy of voldmort " + str(voldmort.get_energy()))
                         break

        # decrease from harry
        for key, value in Power_harry.items():
            if (key == search1):
                # case if the input imperio so he should decrease from both
                if (search1 == 'imperio'):
                    voldmort_energy = voldmort.get_energy() - v
                    harry_energy = harry.get_energy() - v
                    voldmort.set_energy(voldmort_energy)
                    harry.set_energy(harry_energy)
                    print("energy of voldmort " + str(voldmort.get_energy()))
                    print("energy of harry " + str(harry.get_energy()))
                    break
                else:
                 harry_energy =harry.get_energy() - value
                 harry.set_energy(harry_energy)
                 print("energy of harry " + str(harry.get_energy()))
                 break

####################################################################################################################################
    #difference between two power then delete that difference from bigger
        if (search1== 'shield' or search2=='shield'):
            print("health of voldmort " + str(voldmort.get_health()))
            print("health of harry " + str(harry.get_health()))
        else:
            ####bytr7 al atnen energy
                y = abs(value - v)

                # if ((voldmort.get_energy()) > (harry.get_energy())):
                #check what power is more from dictionary then delete the difference from the bigger health
                if(value<v):
                    harry_health = harry.get_health() - y
                    harry.set_health(harry_health)
                    print("health of voldmort " + str(voldmort.get_health()))
                    print("health of harry " + str(harry.get_health()))
                elif(value>v):
                    voldmort_health = voldmort.get_health() - y
                    voldmort.set_health(voldmort_health)
                    print("health of voldmort " + str(voldmort.get_health()))
                    print("health of harry " + str(harry.get_health()))
                else:
                    print("health of voldmort " + str(voldmort.get_health()))
                    print("health of harry " + str(harry.get_health()))
                y=0
        lst.clear()
        if (harry.get_health() == 0):
            print("voldmort is winner")
            flag=0
        elif(voldmort.get_health() == 0):
            print("harry is winner")
            flag=0
############################################3
main()