import {useState} from "react"
import TaskForm from "./TaskForm"
import TaskList from "./TaskList"
import Filter from "./Filter"

function App(){

const [priority,setPriority]=useState("")
const [completed,setCompleted]=useState(null)

return(

<div>

<h2>Task Manager</h2>

<Filter
setPriority={setPriority}
setCompleted={setCompleted}
/>

<TaskForm/>

<TaskList
priority={priority}
completed={completed}
/>

</div>

)

}

export default App