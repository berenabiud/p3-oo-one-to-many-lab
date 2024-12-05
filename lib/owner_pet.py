class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds a pet to the owner, validating its type."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a list of pets sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        """
        Initialize a Pet instance.
        :param name: The name of the pet.
        :param pet_type: The type of the pet, must be one of PET_TYPES.
        :param owner: The owner of the pet, defaults to None.
        """
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type '{pet_type}'. Must be one of {Pet.PET_TYPES}.")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("The owner must be an instance of the Owner class or None.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet instance to the class-level list
        Pet.all.append(self)
