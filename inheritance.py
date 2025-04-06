class employee():

    def __init__(self,name,occ):
        self.name=name
        self.occ=occ

    def data(self):
        print(f'{self.name} is a/an {self.occ}')

class extra_details(employee):
    def showdata(self):
        print(f'Python expert')

a=employee('Rohan','DS')
a.data()
b=extra_details('Hari',"SD")
b.data()
b.showdata()

