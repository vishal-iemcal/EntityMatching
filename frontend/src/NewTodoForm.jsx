import { useState } from "react"

export function NewTodoForm({ onSubmit }) {
  const [itemName, setItemName] = useState("")
  const [itemAddress, setItemAddress] = useState("")

  function handleSubmit(e) {
    e.preventDefault()
    if (itemName === "" || itemAddress ==="") return

    onSubmit(itemName , itemAddress)

    setItemName("")
  }

  return (
    <form onSubmit={handleSubmit} className="new-item-form">
      <div className="form-row">
        <label htmlFor="item">Name</label>
        <input
          value={itemName}
          onChange={e => setItemName(e.target.value)}
          type="text"
          id="item"
        />
      </div>
      <div className="form-row">
        <label htmlFor="item">Address</label>
        <input
          value={itemAddress}
          onChange={e => setItemAddress(e.target.value)}
          type="text"
          id="item"
        />
      </div>
      <button className="btn">Search</button>
    </form>
  )
}
