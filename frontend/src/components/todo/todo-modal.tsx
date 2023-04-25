import { useState } from "react";
import { Portal } from "react-portal";

import { Todo } from "@/types/todo";
import TailSpin from "../common/loading";

type CustomModalProps = {
  activeItem: Todo;
  toggle: () => void;
  onSave: (item: Todo) => void;
  isLoading: boolean;
  isError: boolean;
};

export default function CustomModal({
  activeItem,
  toggle,
  onSave,
  isLoading,
  isError,
}: CustomModalProps) {
  const [item, setItem] = useState(activeItem);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;

    setItem((prevItem) => ({
      ...prevItem,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSave = () => {
    onSave(item);
  };

  return (
    <Portal node={document && document.getElementById('modal-portal')}>
      <div className="fixed inset-0 z-50 overflow-y-auto bg-blue-950 bg-opacity-80">
        <div className="wrapper">
          <div className="flex items-center justify-center min-h-screen">
            <div className="w-full p-4 overflow-hidden bg-white rounded-lg shadow-lg lg:w-1/2" data-testid="todo-modal">
              <div className="mb-4 text-xl font-medium text-gray-900">
                Todo Item
              </div>
              <form>
                <div className="mb-4">
                  <label
                    htmlFor="todo-title"
                    className="block mb-2 font-medium text-gray-700"
                  >
                    Title
                  </label>
                  <input
                    type="text"
                    id="todo-title"
                    name="title"
                    value={item.title}
                    onChange={handleChange}
                    placeholder="Enter Todo Title"
                    className="w-full p-2 border border-gray-400 rounded"
                  />
                </div>
                <div className="mb-4">
                  <label
                    htmlFor="todo-description"
                    className="block mb-2 font-medium text-gray-700"
                  >
                    Description
                  </label>
                  <input
                    type="text"
                    id="todo-description"
                    name="description"
                    value={item.description}
                    onChange={handleChange}
                    placeholder="Enter Todo Description"
                    className="w-full p-2 border border-gray-400 rounded"
                  />
                </div>
                <div className="mb-4">
                  <label className="flex items-center font-medium text-gray-700">
                    <input
                      type="checkbox"
                      name="is_completed"
                      checked={item.is_completed}
                      onChange={handleChange}
                      className="mr-2 form-checkbox"
                    />
                    <span>Completed</span>
                  </label>
                </div>
              </form>
              <div className="flex justify-end mt-4 max-h-8">
                <span className={!isLoading ? 'hidden' : 'mx-4'}>
                  <TailSpin height={32} width={32} stroke="var(--blue-genemod)" />
                </span>
                <span className={!isError ? 'hidden' : 'text-red-500 mx-4'}>
                  Error
                </span>
                <button
                  type="button"
                  onClick={handleSave}
                  className="px-4 py-2 btn btn-primary"
                >
                  Save
                </button>
                <button
                  type="button"
                  onClick={toggle}
                  className="px-4 py-2 ml-2 btn btn-alert"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Portal>
  );
}
