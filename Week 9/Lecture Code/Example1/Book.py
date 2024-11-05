class Airport:
    def __init__(self, name):
        self.name = name
        self.checked_in_passports = []

    def check_in_passport(self, passport):
        if passport not in self.checked_in_passports:
            self.checked_in_passports.append(passport)
            print(f"{passport.holder_name} checked in at {self.name}.")
        else:
            print(f"{passport.holder_name} is already checked in at {self.name}.")

    def check_out_passport(self, passport):
        if passport in self.checked_in_passports:
            self.checked_in_passports.remove(passport)
            print(f"{passport.holder_name} checked out from {self.name}.")
        else:
            print(f"{passport.holder_name} is not currently checked in at {self.name}.")

    def list_checked_in_passports(self):
        print(f"Current passports checked in at {self.name}:")
        if self.checked_in_passports:
            for passport in self.checked_in_passports:
                passport.display_info()
        else:
            print("No passports are currently checked in.")
