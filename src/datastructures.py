
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
             {
            "id": 1,
            "first_name": "John",
            "last_name": last_name,
            "age": 33 ,
            "lucky_numbers":[7, 13, 22],
            },
            {
            "id": 2,
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers":[10, 14, 3],
            },
            {
            "id": 3,
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5 ,
            "lucky_numbers":[1],
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

#----------------método POST----------------------
# método para añadir un miembro: 
    def add_member(self, member):
        # Si viene con id, comprobamos que no exista ya de antemano ese id
        # Para ello, recorremos el array de la familia 
        # comprobamos el id de cada miembro con el del objeto recibido
        # en caso de que coincida, le generamos id nuevo

        for person in self._members:
            if(member["id"] == person["id"]):
                member["id"] = self._generateId() 
        
        #añadimos el apellido de la familia
        member["last_name"] = self.last_name

        #añadimos el nuevo miembro a la familia
        self._members.append(member)

        return True        
     
#----------------métodos GET----------------------

# método para devolver todos los miembros de la familia
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

# método para devolver un miembro por id
    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if (member["id"] == id):
                return member
        # esta sentencia va fuera del if porque si no tendríamos un return en la primera iteración    
        return "No existe miembro"

#----------------método DELETE----------------------
# método para eliminar un miembro por id
    def delete_member(self, id):
        # fill this method and update the return
        family_before = len(self._members)
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
        family_after = len(self._members) 
        if (family_before>family_after):
                return True