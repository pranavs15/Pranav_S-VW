function Filter({setPriority,setCompleted}){

return(

<div>

<select onChange={(e)=>setPriority(e.target.value)}>
<option value="">All Priority</option>
<option value="Low">Low</option>
<option value="Medium">Medium</option>
<option value="High">High</option>
</select>

<label>

Completed

<input
type="checkbox"
onChange={(e)=>setCompleted(e.target.checked)}
/>

</label>

</div>

)

}

export default Filter