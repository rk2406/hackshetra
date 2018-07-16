const express=require('express')
const router=express.Router
const route=router()

const sequelize=require('sequelize')
const datatype=sequelize.DataTypes
const db=new sequelize({
    dialect: 'sqlite',
    storage: __dirname+ '/students.db',
    
})
db.authenticate().then(()=>{
    console.log("connected")
}).catch((err)=>{
    console.log("error");
})
const student_db=db.define('student_db',{
    name:datatype.STRING,
    year:datatype.INTEGER,
})

let students=[
    {name:"MNO",year:1},
    {name:"PQR",year:2}
]
route.get('/',(req,res)=>res.send(students))
route.post('/',(req,res)=>{
    db.sync().then(
        ()=>{
            student_db.create(
                {
                    name:req.body.name,
                    year:req.body.year
                }
            )
            students.push({
                name:req.body.name,
                year:req.body.year
            })
            res.send(students);
        }
    ).catch((err)=>{console.log("error")})
})
route.get('/:id',(req,res)=>res.send(students[req.params.id]))

module.exports=route