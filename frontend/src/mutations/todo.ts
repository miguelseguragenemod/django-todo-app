import { useMutation } from "@tanstack/react-query";
import { createTodoService, updateTodoService, deleteTodoService } from "@/services/todo";
import { Todo } from "@/types/todo";

export function useCreateTodo() {
  return useMutation({
    mutationFn: (data: Todo) => createTodoService(data),
  })
}

export function useUpdateTodo() {
  return useMutation({
    mutationFn: (data: Todo) => updateTodoService(data),
  })
}

export function useDeleteTodo() {
  return useMutation({
    mutationFn: (uuid: string) => deleteTodoService(uuid),
  })
}
