# 1. MobilePhone Class
class MobilePhone:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def make_call(self, number: str) -> None:
        # Yahan print kariye: "Calling {number} from {self.brand} {self.model}..."
        print(f"calling{number} from {self.brand} {self.model}")
        pass


# 2. Person Class (Association Yahan Hoga)
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def call_friend(self, phone: MobilePhone, number: str) -> None:
        # Yahan 'phone' object ka 'make_call(number)' method call kariye!
        
        pass


# 3. Main Execution
if __name__ == "__main__":
    my_phone = MobilePhone("Apple", "iPhone 15")
    rahul = Person("Rahul")

    # Rahul apne my_phone se "9876543210" par call kar raha hai:
    rahul.call_friend(my_phone, "9876543210")
