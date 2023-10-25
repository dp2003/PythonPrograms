class Vaccine:
    def __init__(self, id, company, effectiveness, price, country):
        self.id = id
        self.company = company
        self.effectiveness = effectiveness
        self.price = price
        self.country = country
        vaccines = []
    def addVaccine(vaccine):
        vaccines.append(vaccine)
        
    def displayVaccines():
        print("List of vaccines")
        for i in range(0, len(vaccines)):
            print("Id = " + str(vaccines[i].id) + "\tCompany = " + vaccines[i].company + "\tEffectiveness = " + str(vaccines[i].effectiveness) + "\tPrice = " + str(vaccines[i].price) + "\tCountry = " + vaccines[i].country)

    def maxEffectiveVaccine():
        bestVaccine = vaccines[0]
        bestEffectiveness = vaccines[0].effectiveness
        for i in range(0, len(vaccines)):
            if vaccines[i].effectiveness > bestEffectiveness:
                bestVaccine = vaccines[i]
            return bestVaccine

vacc=Vacccine( id, company, effectiveness, price, country)

    def main():
        vaccine1 = Vaccine(1, 'Covishield', 89, 300, 'India')
        addVaccine(vaccine1)
        vaccine2 = Vaccine(2, 'Covaxin', 85, 800, 'India')
        addVaccine(vaccine2)
        vaccine3 = Vaccine(3, 'Sputnik', 95, 1500, 'Russia')
        addVaccine(vaccine3)
        displayVaccines()
        bestVaccineFound = maxEffectiveVaccine()
        print("\n")
        print("Most effective vaccine")
