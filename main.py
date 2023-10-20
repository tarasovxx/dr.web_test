"""
This module contains the main logic for interacting with the database.
"""
from database import Database

def main():
    """
    Main function for interacting with the database.
    """
    db = Database()
    while True:
        try:
            command = input("> ").split()
            cmd = command[0]
            if cmd == "SET":
                db.set(command[1], command[2])
            elif cmd == "GET":
                result = db.get(command[1])
                print(result)
            elif cmd == "UNSET":
                db.unset(command[1])
            elif cmd == "COUNTS":
                count = db.count(command[1])
                print(count)
            elif cmd == "FIND":
                found = db.find(command[1])
                print(found)
            elif cmd == "BEGIN":
                db.begin()
            elif cmd == "ROLLBACK":
                db.rollback()
            elif cmd == "COMMIT":
                db.commit()
            elif cmd == "END":
                break
        except EOFError:  # Обработка EOFError
            print("EOF detected. Exiting.")
            break
        except (IndexError, KeyError):
            print("Invalid command")
        finally:
            print()


if __name__ == "__main__":
    main()
