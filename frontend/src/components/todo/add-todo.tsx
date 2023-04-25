import { useState } from "react";
import TodoModal from "./todo-modal";
import { Todo } from "@/types/todo";
import { useCreateTodo } from "@/mutations/todo";

function AddTodo({ refetch } : { refetch: () => void }) {
  const { mutate, isLoading, isError } = useCreateTodo()
  const [showModal, setShowModal] = useState<boolean>(false);
  const [activeItem, setActiveItem] = useState<Todo>({ uuid: "", title: "", description: "", is_completed: false });

  const toggleModal = () => setShowModal(!showModal);

  const onSave = (item: Todo) => {
    mutate(item, {
      onSettled: () => {
        toggleModal();
        refetch();
      }
    });
  };

  return (
    <>
      <button className="btn btn-fw btn-primary" data-testid="add-todo" onClick={toggleModal}>
        Add task
      </button>
      {showModal && (
        <TodoModal
          activeItem={activeItem}
          toggle={toggleModal}
          onSave={onSave}
          isLoading={isLoading}
          isError={isError}
        />
      )}
    </>
  );
}

export default AddTodo;
