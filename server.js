const express = require('express')
// var favicon = require('serve-favicon');
const app = express()
const { exec } = require("child_process");

app.use(express.static("public"))
// app.use('/static', express.static('public'))
app.use(express.urlencoded({ extended: true}))
// app.use(express.favicon("/public/icons/favicon.ico"));
// app.use(favicon(__dirname + '/icons/favicon.ico'));
// app.use('/images/favicon', express.static('icons/favicon7.png'));
import { passgen } from 'password.js';

var passwords = passgen();

app.set('view engine', 'ejs')


app.get('/',(req, res) => {

    // console.log('here')
     //res.send('hi')
    // res.sendStatus(404)
    // res.status(404).send("page not found")
    res.render('Home/index')
}) 

app.get('/track',(req, res) => {
    res.render('Map/password')
}) 

app.get('/calendar',(req, res) => {
    res.render('Calendar/calendar')
}) 




app.get('/3d',(req, res) => {
    res.render('3D/index')
}) 

app.get('/about',(req, res) => {
    res.render('About/about')
}) 
app.get('/onestepfurther',(req, res) => {
    res.render('onestep/osf')
}) 

app.post('/track' , (req,res) => {
    

if (req.body.passWord == passwords){
        // res.push({passWord: req.body.passWord })
        // res.redirect(`/map/index`)
        //res.render('home/index')
        // res.sendFile(__dirname + '/views/map/map.html');
        res.render('Map/index')
        // res.sendFile(__dirname + '/views/map/map.html' , { root: '.' });

    }else{
        console.log("error")
        //res.render('map/password',{passWord: req.body.passWord })
        res.render('Map/password')
    }

})

function updatemap() {
    exec("python3 Mapgen/MapGenerator.py", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });


    exec("python3 Mapgen/airpodonly.py", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
  }
  updatemap();

  const interval = setInterval(updatemap, 60000);




// router.post('/', (req,res)=> {
//     // const isValid = false
    
//     // console.log(req.body.firstName)
//     // res.send('createuser')
// })


// const userRouter = require('./routes/users')

// app.use('/users',userRouter)


function logger (req,res,next) {
    console.log(req.originalUrl)
    next()

}

app.listen(3000)


