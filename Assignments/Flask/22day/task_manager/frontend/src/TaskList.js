import axios from "axios"
import {useEffect,useState} from "react"

function TaskList({priority,completed}){

const [tasks,setTasks]=useState([])

const loadTasks = async()=>{

let url="http://localhost:5000/tasks?"

if(priority) url+=`priority=${priority}&`
if(completed!==null) url+=`completed=${completed}`

const res = await axios.get(url)

setTasks(res.data)

}

useEffect(()=>{
loadTasks()
},[priority,completed])

return(

<table border="1">

<thead>
<tr>
<th>Title</th>
<th>Priority</th>
<th>Status</th>
</tr>
</thead>

<tbody>

{tasks.map(task=>(

<tr key={task.id}>
<td>{task.title}</td>
<td>{task.priority}</td>
<td>{task.completed ? "Done":"Pending"}</td>
</tr>

))}

</tbody>

</table>

)

}

export default TaskList