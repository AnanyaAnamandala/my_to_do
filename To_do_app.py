from functions import get_todos, write_todos
    

while True:
    user_action = input("Type add or show or edit or complete or exit: \n")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo+'\n')

        write_todos(todos)
        
    elif user_action.startswith('show'):

        todos = get_todos()

        for index, i in enumerate(todos):
            i = i.strip("\n")
            print(f"{index+1}.{i}")


    elif user_action.startswith('edit'):
        try:
            
            number= int(user_action[5:])
            number = number-1
            todos = get_todos()

            new_todo= input("Enter the new item:")
            todos[number]=new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid \n")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos
            index = number - 1
            to_do_removed = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {to_do_removed} was removed from the list"
            print(message)
        except IndexError:
            print("No such number exists")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")
print("Bye!")       
  





