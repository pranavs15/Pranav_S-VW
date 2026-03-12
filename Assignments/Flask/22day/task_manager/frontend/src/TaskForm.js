import axios from "axios"
import {useState} from "react"

function TaskForm(){

const [title,setTitle]=useState("")
const [priority,setPriority]=useState("Low")

const submitTask = async ()=>{

await axios.post("http://localhost:5000/tasks",{
title:title,
priority:priority
})

}

return(

<div>

<input
placeholder="Task title"
onChange={(e)=>setTitle(e.target.value)}
/>

<select onChange={(e)=>setPriority(e.target.value)}>
<option>Low</option>
<option>Medium</option>
<option>High</option>
</select>

<button onClick={submitTask}>
Add Task
</button>

</div>

)

}

export default TaskForm