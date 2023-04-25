type ListFiltersProps = {
  viewCompleted: boolean;
  displayCompleted: (status: boolean) => void;
}

function ListFilters({ viewCompleted, displayCompleted }: ListFiltersProps) {
  return (
    <div className="flex mb-4 overflow-hidden rounded-lg">
      <span
        className={`flex-1 text-center cursor-pointer font-bold py-2 px-4 ${viewCompleted ? "toggle-disabled" : "toggle-active"}`}
        onClick={() => displayCompleted(!viewCompleted)}
      >
        Incomplete
      </span>
      <span
        className={`flex-1 text-center cursor-pointer font-bold py-2 px-4 ${!viewCompleted ? "toggle-disabled" : "toggle-active"}`}
        onClick={() => displayCompleted(!viewCompleted)}
      >
        Complete
      </span>
    </div>
  )
}

export default ListFilters;
