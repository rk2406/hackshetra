const express=require('express')
const srv=express()

const teachers=require('./routes/teachers')
const students=require('./routes/students')

srv.use(express.json())
srv.use(express.urlencoded({extended:true}))

srv.use('/students',students)
srv.use('/teachers',teachers)

srv.listen(2233);