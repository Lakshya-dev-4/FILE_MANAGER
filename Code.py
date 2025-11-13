import os
from time import sleep
from shutil import rmtree
from datetime import datetime as dt

class FileManager:
    def __init__(self, base_dir='.'):
        self.base_dir = base_dir

    def greet(self):
        print('\n', "FILE MANAGER".center(50, '◇'), '\n')

    def add_item(self):
        timestamp = dt.now().strftime("[%H:%M:%S]") 	
        try:
            item_type = input('Directory or File (d/f): ').lower()
            item_name = input('Enter name: ')
            path = os.path.join(self.base_dir, item_name)

            if item_type == 'd':
                if not os.path.exists(path):
                    os.mkdir(path)
                    print(f"'{item_name}' directory created successfully at {timestamp}.")
                else:
                    print(f"'{item_name}' already exists.")
            elif item_type == 'f':
                if not os.path.exists(path):
                    with open(path, 'x'):
                        pass
                    print(f"'{item_name}' file created successfully at {timestamp}.")
                else:
                    print(f"'{item_name}' already exists.")
            else:
                print('INVALID INPUT. Choose either (f)ile or (d)irectory.')
        except Exception as error:
            print('An error occurred.\n', error)

    def delete_item(self):
        try:
            item_name = input('Enter name: ')
            path = os.path.join(self.base_dir, item_name)
            if not os.path.exists(path):
                print(f"'{item_name}' not found.")
            elif os.path.isfile(path):
                os.remove(path)
                print(f"'{item_name}' removed successfully.")
            elif os.path.isdir(path):
                rmtree(path)
                print(f"'{item_name}' directory removed successfully.")
        except Exception as error:
            print('An error occurred.\n', error)

    def view_items(self):
        items = os.listdir(self.base_dir)
        if not items:
            print('No files or directories available.')
        else:
            for index, item in enumerate(items, start=1):
                item_type = "Dir" if os.path.isdir(item) else "File"
                print(f"{index}. {item} ({item_type})")

    def edit_file(self):
        timestamp = dt.now().strftime("[%H:%M:%S]") 
        try:
            file_name = input('Enter the file name: ')
            path = os.path.join(self.base_dir, file_name)
            if not os.path.exists(path):
                print(f"'{file_name}' not found.")
            elif os.path.isdir(path):
                print('Cannot edit a directory.')
            else:
                content = input('Enter the content: ')
                with open(path, 'a') as file:
                    file.write(content + '\n')
                print(f"Content added to '{file_name}' at {timestamp}.")
        except Exception as error:
            print('An error occurred.\n', error)

    def read_file(self):
        try:
            file_name = input('Enter the file name: ')
            path = os.path.join(self.base_dir, file_name)
            if not os.path.exists(path):
                print(f"'{file_name}' not found.")
            else:
                with open(path, 'r') as file:
                    content = file.read()
                    print(f'Content:\n{content}' if content else 'File is empty.')
        except Exception as error:
            print('An error occurred.\n', error)

    def search_item(self):
        try:
            item_name = input('Enter name: ')
            path = os.path.join(self.base_dir, item_name)
            if not os.path.exists(path):
                print(f"'{item_name}' not found.")
                return

            item_type = "File" if os.path.isfile(path) else "Directory"
            size_kb = round(os.path.getsize(path) / 1024, 2)
            created = dt.fromtimestamp(os.path.getctime(path)).strftime("%H:%M:%S %d-%m-%Y")
            modified = dt.fromtimestamp(os.path.getmtime(path)).strftime("%H:%M:%S %d-%m-%Y")

            print("\nInformation about the item:")
            print(f"Name: {item_name}")
            print(f"Type: {item_type}")
            print(f"Size: {size_kb} KB")
            print(f"Created at: {created}")
            print(f"Last modified at: {modified}")

            if os.path.isdir(path):
                show_contents = input(f"\nDo you want to see the files in '{item_name}'? [y/n]: ").lower()
                if show_contents == 'y':
                    contents = os.listdir(path)
                    if not contents:
                        print("No files available in this directory.")
                    else:
                        print("\nContents:")
                        print("\n".join(f"{i}. {entry}" for i, entry in enumerate(contents, start=1)))
            else:
                show_content = input("\nDo you want to see the content of the file? [y/n]: ").lower()
                if show_content == 'y':
                    with open(path, 'r') as file:
                        content = file.read()
                        print("\nContent:\n" + content if content else "File is empty.")
        except Exception as error:
            print('An error occurred.\n', error)

    def rename_item(self):
        old_name = input('Enter current name: ')
        new_name = input('Enter the new name: ')
        old_path = os.path.join(self.base_dir, old_name)
        new_path = os.path.join(self.base_dir, new_name)
        if not os.path.exists(old_path):
            print(f"'{old_name}' not found.")
        else:
            os.rename(old_path, new_path)
            print(f"'{old_name}' renamed to '{new_name}'.")

    def exit_program(self):
        print('Closing....')
        sleep(1)
        print('Goodbye')

    def run(self):
        self.greet()
        run_count = 0
        while True:
            print('\nOptions:')
            print('1: Create File / Directory')
            print('2: Delete File / Directory')
            print('3: Read file')
            print('4: Edit file')
            print('5: Rename File / Directory')
            print('6: View all items')
            print('7: Search item')
            print('8: Exit\n')

            try:
                choice = int(input('Choose: '))
                if choice == 1:
                    self.add_item()
                elif choice == 2:
                    self.delete_item()
                elif choice == 3:
                    self.read_file()
                elif choice == 4:
                    self.edit_file()
                elif choice == 5:
                    self.rename_item()
                elif choice == 6:
                    self.view_items()
                elif choice == 7:
                    self.search_item()
                elif choice == 8:
                    self.exit_program()
                    break
                else:
                    print('Invalid choice. Try from 1–8.')
            except Exception as error:
                print('An error occurred.\n', error)

            run_count += 1
            if run_count % 3 == 0:
                sleep(3)
                os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    fm = FileManager()
    fm.run()
