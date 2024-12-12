export function TodoItem({ completed, id, itemName, itemAddress, toggleTodo, deleteTodo }) {
  return (
    <li>
      <label>
        <input
          type="checkbox"
          checked={completed}
          onChange={e => toggleTodo(id, e.target.checked)}
        />
        {itemName} {itemAddress}
      </label>
      <button onClick={() => deleteTodo(id)} className="btn btn-danger">
        Delete
      </button>
    </li>
  )
}
