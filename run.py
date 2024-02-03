import addTodo.add as add_todo
import clearTodos.clear as clear
import createList.createList as createList



def run():
    list = createList.createList()

    add_todo.add_todo("get groceries", list)

    print(list)

    list = clear.clear(list)

    print(list)

if __name__ == "__main__":
    run()