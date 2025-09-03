class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # validate name
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")

        # validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Pet type must be one of {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None  # default until assigned
        Pet.all.append(self)

        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an Owner instance")
            self.owner = owner


class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string")
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign an owner to a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted alphabetically by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
