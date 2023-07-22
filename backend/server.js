require("colors");
const path = require("path");
const configPath = path.join(__dirname, "..", "config", ".env");
require("dotenv").config({ path: configPath });
const connectDb = require("../config/connectDb");
const errorHandler = require('./middlewares/errorHandler');

const express = require("express");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/api/v1", require("./routes/drinksRoutes"));

app.use(errorHandler);

connectDb();

app.listen(process.env.PORT, () => {
    console.log(
        "Server is running on port ".green.bold.italic + process.env.PORT
    );
});
