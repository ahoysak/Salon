from framework.models import Model


class Salonuser(Model):
    file = "../database/salons.json"

    def __init__(self,name_salon,adress_salon,id):
        self.name_salon = name_salon
        self.adress_salon = adress_salon
        self.id = id


