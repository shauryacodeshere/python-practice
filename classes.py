class employee:
    name="Rohan"
    age=21
    post='AI eng'
    
    def individual(self):
        print(f'{self.name},{self.age},is a {self.post}')
    


a=employee()
print(a.name,a.age)

a.individual()


