import { Todo, TodoPage } from '@/types/todo';

const API_URL: string = process.env.API_URL || 'http://localhost:8000/api/v1';

export async function listToDoService(): Promise<TodoPage> {
  const res = await fetch(`${API_URL}/todos/`, { method: 'GET' } );
  const data: TodoPage = await res.json();
  return data;
}

export async function createTodoService(data: Todo): Promise<Todo> {
  const res = await fetch(`${API_URL}/todo/`, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  });
  const createdTodo: Todo = await res.json();
  return createdTodo;
}

export async function getTodoService(uuid: string): Promise<Todo> {
  const res = await fetch(`${API_URL}/todo/${uuid}/`, { method: 'GET' });
  const data: Todo = await res.json();
  return data;
}

export async function updateTodoService(data: Todo): Promise<Todo> {
  const res = await fetch(`${API_URL}/todo/${data.uuid}/`, {
    method: 'PUT',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
    }
  });
  const updatedTodo: Todo = await res.json();
  return updatedTodo;
}

export async function deleteTodoService(uuid: string): Promise<void> {
  await fetch(`${API_URL}/todo/${uuid}/`, { method: 'DELETE' });
}
