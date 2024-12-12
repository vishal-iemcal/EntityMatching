import { useEffect, useState } from "react"
import { NewTodoForm } from "./NewTodoForm"
//import "./styles.css"
import { TodoList } from "./TodoList"
import Axios from "axios"
import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';
import Grid from '@mui/material/Grid2';

export default function App() {
  
  const columns = [
    { field: 'id', headerName: 'ID', width: 40 },
    { field: 'document', headerName: 'Document', width: 600 },
    { field: 'doc_id', headerName: 'doc id', width: 300 },
    { field: 'distance', headerName: 'distance', width: 250 },
  ];
  
  const paginationModel = { page: 0, pageSize: 5 };

  

  const [name , setName] = useState("")
  const [address , setAddress] = useState("")
  const [matchResponse , setMatchResponse] = useState([])



  
  const fetchMatchingData = () => {
    fetch(`http://127.0.0.1:5000/getMatchList/?name=${name}&address=${address}`, {
      mode:  'cors' 
    }).then(
      res =>res.json()
    ).then(
      data => {
        setMatchResponse(data)
        console.log(data)
      }
    )
  }



  return (
    <>
      <Box
          component="form"
          sx={{ '& .MuiTextField-root': { m: 1, width: '50ch' } }}
          noValidate
          autoComplete="off"
      >
        
        <Grid container spacing={2}>
        <Grid size={12}>
      
        <Alert severity="info">Enter the Entity Name and Address below to find closest similarity mactches from the database.</Alert>
        
        </Grid>
        <Grid size={4}>
        <TextField id="entityname" labelId="nameLabel" label = "Entity Name" variant="outlined" onChange={(event) => {setName(event.target.value)}} />
        </Grid>
        <Grid size={4}>
        <TextField id="entityAddress" label="Entity Address" labelId = "addressLabel" variant="outlined" onChange={(event) => {setAddress(event.target.value)}} />
        </Grid>
        <Grid size={4}>
        <Button variant="contained" onClick={fetchMatchingData}>Get Results</Button>
        </Grid>
        
      </Grid>

    </Box>
      
      <div className="col">
        <h1>Below are existing similar entities </h1>

      <Paper sx={{ height: 400, width: '100%' }}>
      <DataGrid 
        
        rows={matchResponse}
        columns={columns}
        initialState={{ pagination: { paginationModel } }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
        sx={{ border: 0 }}
      />
    </Paper>

     </div>
     
    </>
  )
}