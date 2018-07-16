const express=require('express')
const router=express.Router
const route=router()
const sequelize=require('sequelize')
const datatype=sequelize.DataTypes
const db=new sequelize({
    dialect: 'sqlite',
    storage: __dirname+ '/teachers.db',
    
})
db.authenticate().then(()=>{
    console.log("connected")
}).catch((err)=>{
    console.log("error");
})
const teacher_db=db.define('teacher_db',{
    name:datatype.STRING,
    subject:datatype.STRING,
})
let teachers=[
    {name:"ABC",subject:"abc"},
    {name:"XYZ",subject:"xyz"}
]
route.get('/',(req,res)=>res.send(teachers))
route.post('/',(req,res)=>{
    db.sync().then(
        ()=>{
            teacher_db.create(
                {
                    name:req.body.name,
                    subject:req.body.subject
                }
            )
            teachers.push({
                name:req.body.name,
                sub:req.body.subject
            })
            res.send(teachers);
        }
    ).catch((err)=>{console.log("error")})
})
route.get('/:id',(req,res)=>res.send(teachers[req.params.id]))

module.exports=route