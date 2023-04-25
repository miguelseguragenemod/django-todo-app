import { Todo } from '@/types/todo';
import TodoListItem from './todo-list-item';

interface TodoListProps {
  todos: Todo[];
  viewCompleted: boolean;
}

function TodoList({ todos, viewCompleted }: TodoListProps) {
  const newItems = todos.filter((item) => item.is_completed === viewCompleted);

  return (
    <>
      {newItems.map((item) => (
        <TodoListItem key={item.uuid} item={item} viewCompleted={viewCompleted} />
      ))}
    </>
  )
}

export default TodoList
