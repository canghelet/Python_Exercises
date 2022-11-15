
# 1. Implementarea unei aplicatii de gestionare a unui abonament de streaming
# Avand implementarea clasei StreamingService, implementati:
# - o clasa BankAccount (owner: str, iban: str, balance: int default 0) cu functii specifice unui cont (deposit, withdraw, show_balance)
# - o clasa StreamingServicePaymentProxy (provider: str, subscription_price: int, subscription_expiration_date: datetime, account: BankAccount)
# care sa implementeze un design pattern potrivit si sa faca handling asupra abonamentului, permitand vizualizarea unui show
# numai in cazul in care abonamentul este inca activ sau, in caz contrar, daca in contul bancar mai sunt suficiente fonduri
# pentru a finanta inca o luna (caz in care se retrage suma din cont si se prelungeste abonamentul cu 30 de zile)
# - o clasa AuthorizedAccount (authorized_person: BankAccount, observable: BankAccount) care sa implementeze un design pattern potrivit pentru a desemna o persoana imputernicita
# asupra contului bancar, aceasta fiind notificata asupra oricarei operatiuni de retragere sau depunere de bani din cont cu
# un mesaj sugestiv, de ex: ">Notification from account nr <....> (owner <....>): <mesajul tranzactiei>"
# Pasi sugerati pentru testarea programului:
# 1) instantierea unui BankAccount (preferabil cu 0 lei)
# 2) instantierea unui BankAccount de imputernicit
# 3) instantierea unui AuthorizedAccount al imputernicit catre contul initial
# 4) instantierea unui StreamingServicePaymentProxy legat la primul cont (preferabil cu abonamentul expirat)
# 5) apel catre watching_a_show(show_name) (daca abonamentul e expirat si contul nu are bani, ar trebui sa va afiseze un mesaj sugestiv)
# 6) depunere bani in cont (pe langa depunerea in sine, persoana imputernicita ar trebui sa primeasca un mesaj de notificare despre operatiune)
# 7) apel catre watching_a_show (pe langa mesajul despre show-ul urmarit, acum ar trebui sa primim un mesaj de succes cu privire la tranzactia din cont si unul cu privire la actualizarea abonamentului, cat si unul cu notificarea imputernicitului)

from datetime import datetime, timedelta

class StreamingService:
    def __init__(self, provider):
        self.provider = provider

    def watching_a_show(self, show):
        print(f"You are now watching {show} on {self.provider}.")


class BankAccount:
    def __init__(self, owner, iban, balance=0):
        self.owner = owner
        self.iban = iban
        self.balance = balance
        self._observers = []

    def __str__(self):
        return f"{self.owner}, you have in your account {self.iban} the amount of {self.balance} RON, at {datetime.now().isoformat()}."

    def show_balance(self):
        print(self.__str__())

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

            notification = f"{amount} RON has been withdrawn from your account."
            print(notification)
            self.notify_observers(notification)

            return True

        else:
            notification = f"You do not have sufficient funds."
            print(notification)
            self.notify_observers(notification)

            return False

    def deposit(self, amount):
        self.balance += amount

        notification = f"Your account has been credited with {amount}."
        print(notification)
        self.notify_observers(notification)

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, notification):
        for obs in self._observers:
            obs.notify(self, notification)


class StreamingServicePaymentProxy:
    def __init__(self, provider, subscription_price, expiration_date, account):
        self.streaming_service = StreamingService(provider)
        self.subscription_price = subscription_price
        self.subscription_expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.account = account

    def watching_a_show(self, show):
        if self.subscription_expiration_date > datetime.now():
            self.streaming_service.watching_a_show(show)
        else:
            if self.account.withdraw(self.subscription_price):
                self.subscription_expiration_date += timedelta(days=30)
                print(f"Your subscription has been extended until {self.subscription_expiration_date}.")
                self.streaming_service.watching_a_show(show)
            else:
                print(f"Subscription is expired! There is not enough money in your account.")


class AuthorizedAccount:
    def __init__(self, person, observable):
        self.person = person
        observable.register_observer(self)

    def notify(self, observable, notification):
        print(f">Notification from account nr {observable.iban} (owner {observable.owner}): {notification}")


Sanchez = BankAccount("Sanchez", "RO70INGB1234")
Sanchez.show_balance()

Nelson = BankAccount("Nelson", "RO80INGB4568", 6000)
authorized_account = AuthorizedAccount(Nelson, Sanchez)

streaming_service = StreamingServicePaymentProxy("Netflix", 60, "2022-11-14", Sanchez)
streaming_service.watching_a_show("Sherlock")

Sanchez.deposit(3000)
Sanchez.show_balance()

streaming_service.watching_a_show("Sherlock")