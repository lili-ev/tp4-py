
from abc import ABC, abstractmethod


class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if len(numero) != 16 or not numero.isdigit():
            raise ValueError("Numéro de carte invalide.")

        if len(cvv) != 3 or not cvv.isdigit():
            raise ValueError("CVV invalide.")

        self.numero = numero
        self.cvv = cvv

    def payer(self):
        return f"Paiement par carte bancaire confirmé : {self._montant} €"


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement PayPal confirmé : {self._montant} €"


class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement Crypto ({self.reseau}) confirmé : {self._montant} €"


def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


if __name__ == "__main__":

    paiements = [
        CarteBancaire(200, "1234567890123456", "123"),
        CarteBancaire(350, "9876543210987654", "456"),

        PayPal(150, "alice@example.com", "TOKEN123"),
        PayPal(250, "bob@example.com", "TOKEN456"),

        Crypto(100, "WALLET001", "BTC"),
        Crypto(300, "WALLET002", "ETH")
    ]

    traiter_paiements(paiements)
