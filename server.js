const express = require("express");
const app = express();
const { exec } = require("child_process");
const path = require("path");
const port = 8009;

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));

//import correct password from file 'password.js'
const passwords = require("./password.js");

app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("Home/index");
});

app.get("/track", (req, res) => {
  res.render("Map/password");
});

app.get("/trashgpt", (req, res) => {
  res.render("Toolchain/TrashGPT/index");
});

app.get("/Revolute", (req, res) => {
  res.render("Revolute/index");
});

app.get("/calendar", (req, res) => {
  res.render("Calendar/calendar");
});

// app.get('/iphone15', (req, res) => {

//     var orderdata = require('./Modules/ordertrack/orderstatusoutput.json');

//     res.render('order/index', { orderdata })

// });

app.get("/3d", (req, res) => {
  res.render("3D/index");
});

app.use("/members/:username/:file", (req, res, next) => {
  // Extract the username parameter from the URL
  const { username, file } = req.params;

  // Build the path to the HTML file based on the username
  const filePath = path.join(
    `/mnt/cloud/mainstorage/owncloud/data/${username}/files/Website/${file}.html`,
  );

  console.log(filePath);
  // Serve the HTML file
  res.sendFile(filePath, (err) => {
    // If the file doesn't exist, pass control to the next middleware
    if (err) {
      next();
    }
  });
});

app.get("/clicker", (req, res) => {
  res.render("Clicker/index");
});

app.get("/videodownload", (req, res) => {
  res.render("Toolchain/VideoDownload/index");
});

app.get("/about", (req, res) => {
  var changelog = require("./Modules/changelog/git_log.json");

  res.render("About/about", { changelog });
});

app.get("/onestepfurther", (req, res) => {
  res.render("onestep/osf");
});

// app.post('/track' , (req,res) => {

// if (req.body.passWord == passwords){
//     res.render('Map/index')
//     }else{
//         console.log("error")
//         res.render('Map/password')
//     }

// })

app.use((req, res, next) => {
    res.render('Error/index')
})

//function updatePerDay(){
//
//    exec("python3 modules/changelog/gitlog.py", (error, stdout, stderr) => {
//        if (error) {
//            console.log(`error: ${error.message}`);
//            return;
//        }
//        if (stderr) {
//            console.log(`stderr: ${stderr}`);
//            return;
//        }
//       console.log(`${stdout}`);
//
//    });
//
//}

// function updatePerMinute() {
//     exec("python3 Mapgen/MapGenerator.py", (error, stdout, stderr) => {
//         if (error) {
//             console.log(`error: ${error.message}`);
//             return;
//         }
//         if (stderr) {
//             console.log(`stderr: ${stderr}`);
//             return;
//         }
// //        console.log(`stdout: ${stdout}`);
//         console.log(`${stdout}`);
//     });

//     exec("python3 Mapgen/airpodonly.py", (error, stdout, stderr) => {
//         if (error) {
//             console.log(`error: ${error.message}`);
//             return;
//         }
//         if (stderr) {
//             console.log(`stderr: ${stderr}`);
//             return;
//         }
// //        console.log(`stdout: ${stdout}`);
//         console.log(`${stdout}`);
//     });

//    exec("python3 Modules/ordertrack/appleordershippingstatus.py", (error, stdout, stderr) => {
//        if (error) {
//            console.log(`error: ${error.message}`);
//            return;
//        }
//        if (stderr) {
//            console.log(`stderr: ${stderr}`);
//            return;
//        }
////        console.log(`stdout: ${stdout}`);
//        console.log(`${stdout}`);
//    });
//

// }

// updatePerMinute();

//  updatePerDay();

// const interval = setInterval(updatePerMinute, 60000);
//  const intervalDay = setInterval(updatePerDay, 86400000);

// router.post('/', (req,res)=> {
//     // const isValid = false

//     // console.log(req.body.firstName)
//     // res.send('createuser')
// })

// const userRouter = require('./routes/users')

// app.use('/users',userRouter)

function logger(req, res, next) {
  console.log(req.originalUrl);
  next();
}

//app.listen(3000)
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
