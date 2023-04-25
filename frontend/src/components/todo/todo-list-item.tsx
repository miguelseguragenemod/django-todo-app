import { useState } from 'react';
import { Todo } from '@/types/todo';
import TodoModal from './todo-modal';
import { useDeleteTodo, useUpdateTodo } from '@/mutations/todo';
import { useListTodos } from '@/querys/todo';

interface TodoListItemProps {
  item: Todo;
  viewCompleted: boolean;
}

function TodoListItem({ item, viewCompleted }: TodoListItemProps) {
  const { refetch } = useListTodos()
  const { mutate: updateTodo, isLoading, isError } = useUpdateTodo()
  const { mutate: deleteTodo } = useDeleteTodo()
  const [showModal, setShowModal] = useState(false);
  const toggleModal = () => setShowModal(!showModal);

  const handleUpdate = (editedItem: Todo) => {
    updateTodo(editedItem, {
      onSettled: () => {
        refetch()
        toggleModal();
      }
    });
  }

  const handleDelete = () => {
    deleteTodo(item.uuid, {
      onSettled: () => {
        refetch()
      }
    })
  }

  return (
    <>
      <li
        key={item.uuid}
        className="flex items-center justify-between px-4 py-2 border-b border-gray-300"
      >
        <span
          className={`todo-title mr-2 text-gray-500 ${
            viewCompleted ? 'line-through' : ''
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            className="mr-2 btn btn-primary"
            onClick={toggleModal}
          >
            Edit
          </button>
          <button className="px-3 py-1 btn btn-alert" onClick={handleDelete}>
            Delete
          </button>
        </span>
      </li>
      {showModal && (
        <TodoModal
          activeItem={item}
          toggle={toggleModal}
          onSave={handleUpdate}
          isLoading={isLoading}
          isError={isError}
        />
      )}
    </>
  );
}

export default TodoListItem;
