# class Employee: # always write capital letters when makeing the class
#     def showEmployeeData(self):
#         print('johan' ,'43' , '$5566')
# obj = Employee()
# obj.showEmployeeData()


company = 'learn2code'
class Employee2: 
    def __init__(self,name,age , salary,gender, desig , dept, resposibility,cpu,gpu,ram):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail(Employee2)
        # self.job = self.job(desig,dept,resposibility)
        # self.Computer = self.Computer(cpu,gpu,ram)
        # self.job = self.job()
    
    def generateEmail(self ,cls):
        return f'{self.name}@{cls.company}.com'
    def showInfo(self):
        print(self.name, self.age,self.salary, self.gender,self.email)

    @classmethod
    def changeCompanyName( cls , newName):
        cls.company = newName

    @staticmethod
    def info():
        print('this is three of creating a emplayee and it requires a paramenters.')

Employee2.changeCompanyName('learnToCode')


    # class job:
    #     def __init__(self,designation , department, resposibility):
    #         self.designation = designation
    #         self.resposibility = resposibility
    #         self.department = department
    #     def showInfo(self):
    #         print(self.designation , self.department,self.resposibility)

    # class Computer:
    #     def __init__(self, cpu,gpu,ram):
    #         self.cpu = cpu
    #         self.ram = ram
    #         self.gpu = gpu
    #     def showInfo(self):
    #         print(self.cpu,self.gpu,self.ram)
    
obj = Employee2('john', "34", '$33455', 'm' , 'manager', 'it','server', 'i5' , 'gtx3',"3gb")

Employee2.info()

obj.showInfo()

# obj.job.showInfo()
# obj.computer.showInfo()