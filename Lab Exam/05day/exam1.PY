"""
Name: Your Name
Description: Command line shopping list application with file persistence.
"""

import os


class ShoppingList:
    def __init__(self):
        """Initialize shopping list and load items from file."""
        self.filename = "shopping_list.txt"
        self.items = []
        self.load_items()

    def start_menu(self):
        """Print program instructions."""
        print("What do you want to add to your shopping list?")
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'HELP' for additional info.")
        print("Enter 'SHOW' to see your shopping list.")
        print("Enter 'REMOVE' to remove an item from your shopping list.")
        print("-----------------------------------------")

    def normalize_item(self, item):
        """Normalize item capitalization."""
        return item.strip().capitalize()

    def add_to_list(self, item):
        """Add item if not already present."""
        item = self.normalize_item(item)

        if not item:
            print("Cannot add an empty item.")
            return

        if item in self.items:
            print(f"{item} is already in your shopping list.")
        else:
            self.items.append(item)
            print(f"{item} was added to your shopping list.")
            print(f"You have {len(self.items)} items on your list.")

    def remove_item(self, item):
        """Remove item if present."""
        item = self.normalize_item(item)

        if item in self.items:
            self.items.remove(item)
            print(f"{item} was removed from your shopping list.")
            print(f"You have {len(self.items)} items on your list.")
        else:
            print(f"{item} was not found in your shopping list.")

    def show_shopping_list(self):
        """Display the current shopping list."""
        print("My Shopping List:")
        if not self.items:
            print("(Your shopping list is empty.)")
        else:
            for item in self.items:
                print(f"- {item}")

    def save_items(self):
        """Save items to file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                for item in self.items:
                    file.write(item + "\n")
        except OSError as e:
            print(f"Error saving shopping list: {e}")

    def load_items(self):
        """Load items from file."""
        if not os.path.exists(self.filename):
            return  # Start empty if file does not exist

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.items = [line.strip() for line in file if line.strip()]
        except OSError as e:
            print(f"Error loading shopping list: {e}")
            self.items = []


def main():
    shopping_list = ShoppingList()
    shopping_list.start_menu()

    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                continue

            command = user_input.upper()

            if command == "DONE":
                shopping_list.save_items()
                print("See you soon!")
                print("Your shopping list has been saved.")
                shopping_list.show_shopping_list()
                break

            elif command == "HELP":
                shopping_list.start_menu()

            elif command == "SHOW":
                shopping_list.show_shopping_list()

            elif command == "REMOVE":
                shopping_list.show_shopping_list()
                item_to_remove = input("What do you want to remove?: ")
                shopping_list.remove_item(item_to_remove)

            else:
                shopping_list.add_to_list(user_input)

        except EOFError:
            # Handle Ctrl+D (Unix) or Ctrl+Z (Windows)
            print("\nEOF received. Saving your shopping list...")
            shopping_list.save_items()
            print("Your shopping list has been saved. Goodbye!")
            break


if __name__ == "__main__":
    main()
