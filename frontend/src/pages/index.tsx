import { useState } from 'react'
import AddTodo from '@components/todo/add-todo'
import ListFilters from '@components/todo/list-filters'
import TodoList from '@components/todo/todo-list'
import { Todo } from '@/types/todo'
import { useListTodos } from '@/querys/todo'

export default function Home() {
  const { data, isLoading, isError, refetch } = useListTodos()
  const [viewCompleted, setViewCompleted] = useState<boolean>(false)

  const displayCompleted = (status: boolean): void => {
    setViewCompleted(status);
  };

  return (
    <main>
      <div className="wrapper">
        <h1 className="my-12 text-2xl text-center text-white uppercase">Task List</h1>
        <div className="flex justify-center">
          <div className="w-full lg:w-1/2">
            <div className="p-4 overflow-hidden bg-white rounded-lg shadow-md">
              <ListFilters viewCompleted={viewCompleted} displayCompleted={displayCompleted} />
              {!data && isLoading && <p>Loading...</p>}
              {isError && <p>There has been Error</p>}
              {data?.pages[0].count === 0 && <p>No data</p>}
              {data?.pages[0].results.length && (
                <ul className="list-none">
                  <TodoList todos={data?.pages[0].results} viewCompleted={viewCompleted} />
                </ul>
              )}
              <div className="mt-4">
                <AddTodo refetch={refetch} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
