import datetime

class Plant:
    def __init__(self, name, watering_interval):
        self.name = name.title()
        self.watering_interval = watering_interval
        self.last_watered = datetime.date.today()

    def water(self):
        self.last_watered = datetime.date.today()
        print(f"✅ {self.name} has been watered today.")

    def needs_watering(self):
        days_since = (datetime.date.today() - self.last_watered).days
        return days_since >= self.watering_interval

    def display_info(self):
        days_since = (datetime.date.today() - self.last_watered).days
        status = "Yes ✅" if self.needs_watering() else "No ❌"
        print(f"\n🌿 Plant: {self.name}")
        print(f"📆 Water every: {self.watering_interval} day(s)")
        print(f"💧 Last watered: {self.last_watered} ({days_since} days ago)")
        print(f"🚿 Needs watering: {status}")


class Garden:
    def __init__(self):
        self.plants = []

    def add_plant(self, name, watering_interval):
        if any(plant.name == name.title() for plant in self.plants):
            print(f"⚠️ {name.title()} already exists in your garden.")
            return
        self.plants.append(Plant(name, watering_interval))
        print(f"🌱 {name.title()} has been added to your garden.")

    def remove_plant(self, name):
        original_count = len(self.plants)
        self.plants = [plant for plant in self.plants if plant.name != name.title()]
        if len(self.plants) < original_count:
            print(f"🗑️ {name.title()} has been removed from your garden.")
        else:
            print(f"⚠️ {name.title()} not found.")

    def list_plants(self):
        if not self.plants:
            print("🌵 Your garden is empty.")
            return
        print("\n🪴 Your Plants:")
        for plant in sorted(self.plants, key=lambda p: p.name):
            plant.display_info()
            print("-" * 40)

    def water_plant(self, name):
        for plant in self.plants:
            if plant.name == name.title():
                plant.water()
                return
        print(f"⚠️ {name.title()} not found in your garden.")

    def suggest_watering(self):
        due_plants = [p.name for p in self.plants if p.needs_watering()]
        if due_plants:
            print("\n💡 Plants that need watering today:")
            for name in due_plants:
                print(f"👉 {name}")
        else:
            print("\n✅ All plants are well-watered today!")


def main():
    garden = Garden()

    while True:
        print("\n🌼 Gardening App Menu")
        print("1. Add a plant")
        print("2. Remove a plant")
        print("3. List all plants")
        print("4. Water a plant")
        print("5. Suggest plants to water")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter the plant name: ").strip()
            try:
                interval = int(input("Enter watering interval (in days): ").strip())
                if interval <= 0:
                    raise ValueError
                garden.add_plant(name, interval)
            except ValueError:
                print("⚠️ Please enter a valid positive integer for the interval.")

        elif choice == "2":
            name = input("Enter the name of the plant to remove: ").strip()
            garden.remove_plant(name)

        elif choice == "3":
            garden.list_plants()

        elif choice == "4":
            name = input("Enter the name of the plant to water: ").strip()
            garden.water_plant(name)

        elif choice == "5":
            garden.suggest_watering()

        elif choice == "6":
            print("👋 Exiting Gardening App. Happy planting!")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
