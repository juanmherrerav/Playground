class Student():
    def __init__(self, name, qualification):
        self.name = name
        self.qualification = qualification
    def __str__(self):
        return "El alumno {} ha sacado un {} ".format(self.name, self. qualification)
    def has_passed(self):
        if self.qualification < 5:
            return False
        else:
            return True


jose = Student('Jose',10)
print(jose)
is_passed = jose.has_passed()
if is_passed:
    print('Esta aprobado')
else:
    print('Esta suspendido')
