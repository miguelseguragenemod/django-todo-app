export interface Todo {
  uuid: string;
  title: string;
  description: string;
  is_completed: boolean;
}

export interface TodoPage {
  count: number;
  next: string | null;
  previous: string | null;
  results: Todo[];
}
