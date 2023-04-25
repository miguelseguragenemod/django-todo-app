import { useInfiniteQuery, useQuery } from "@tanstack/react-query";
import { listToDoService, getTodoService } from "@/services/todo";

export function useListTodos() {
  return useInfiniteQuery({
    queryKey: ['todos'],
    queryFn: () => listToDoService(),
    getNextPageParam: ({ next }) =>{
      const nextParam = next?.slice(next?.indexOf('page=') + 5)
      return nextParam
    },
    getPreviousPageParam: ({ previous }) =>{
      const previousParam = previous?.slice(previous?.indexOf('page=') + 5)
      return previousParam
    },
  })
}

export function useTodo(uuid: string) {
  return useQuery({
    queryKey: ['GET_TODO', uuid],
    queryFn: () => getTodoService(uuid),
  })
}
