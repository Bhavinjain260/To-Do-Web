import streamlit as st
import functions

todos = functions.get_todo()


def add_tod():
    todos.append(st.session_state["New_todo"] + "\n")
    functions.write_todo(todos)


st.title("My Todo App")
st.write("This App will help you boost your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new Todo..",
              on_change=add_tod, key="New_todo")
