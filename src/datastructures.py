class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
        
        # Add initial members with pre-defined IDs
        self.add_member({
            'first_name': 'John',
            'age': 33,
            'lucky_numbers': [7, 13, 22],
            'id': 1
        })
        self.add_member({
            'first_name': 'Jane',
            'age': 35,
            'lucky_numbers': [10, 14, 3],
            'id': 2
        })
        self.add_member({
            'first_name': 'Jimmy',
            'age': 5,
            'lucky_numbers': [1],
            'id': 3
        })

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if 'id' not in member:
            member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        member_to_delete = None
        for member in self._members:
            if member['id'] == id:
                member_to_delete = member
                break
        
        if member_to_delete:
            self._members.remove(member_to_delete)
            return {'done': True}
        return {'done': False}

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return {'error': 'Member not found'}

    def get_all_members(self):
        return self._members