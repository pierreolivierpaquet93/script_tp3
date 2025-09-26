class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif")
        self.solde += montant

    def retirer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif")
        if montant > self.solde:
            raise ValueError("Fonds insuffisants")
        self.solde -= montant

    def transfert(self, autre_compte: "CompteBancaire", montant: float):
        if not isinstance(autre_compte, CompteBancaire):
            raise TypeError("Le destinataire doit être un CompteBancaire")
        if autre_compte == self:
            raise ValueError
        self.retirer(montant)
        autre_compte.deposer(montant)

    def est_vide(self) -> bool:
        return self.solde == 0

    def __str__(self):
        return f"Compte de {self.titulaire}, solde: {self.solde:.2f}"