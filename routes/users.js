
const express = require ("express")
const router = express.Router()


router.use(logger)

router.get('/', (req,res) =>{
    res.send('userlist')

})

router.get('/new', (req,res) =>{
    // res.send('usernewform')
    res.render("users/new",{firstName:'test'})
    
    
})

router.post('/', (req,res)=> {
    // const isValid = false
    if (req.body.firstName == "10"){
        users.push({firstName: req.body.firstName })
        res.redirect(`/users/${users.length - 1}`)
    }else{
        console.log("error")
        res.render("users/new", { firstName: req.body.firstName})
    }
    // console.log(req.body.firstName)
    // res.send('createuser')
})

router
.route("/:id")
.get((req,res)=>{

    console.log(req.user)
    res.send(`get user with id ${req.params.id}`)
}).put( (req,res)=>{
    res.send(`update user with id ${req.params.id}`)
}).delete((req,res)=>{
    res.send(`delete user with id ${req.params.id}`)
})

const users =[{name:"kyle"},{name:"aaa"}]

router.param("id",(req,res,next,id)=>{
    //console.log(id)
    req.user = users[id]
    next()

})

function logger (req,res,next) {
    console.log(req.originalUrl)
    next()

}

module.exports = router

