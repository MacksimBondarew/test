require("colors");
const path = require("path");
const asyncHandler = require("express-async-handler");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const configPath = path.join(__dirname, "..", "config", ".env");
require("dotenv").config({ path: configPath });
const connectDb = require("../config/connectDb");
const errorHandler = require("./middlewares/errorHandler");
const usersModel = require("./models/usersModel");
const authMiddleware = require("./middlewares/authMiddleware");
const rolesModel = require("./models/rolesModel");

const express = require("express");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/api/v1", require("./routes/drinksRoutes"));

//  Реєстрація - це збереження користувача у базі даних
// Аутентифікація - це перевірка данних які передав користував і порівнявання з тими які які є у базі
// Авторизація - це перевірка прав доступу
// Розлогінення - вихід із додатку

app.post(
  "/register",
  asyncHandler(async (req, res) => {
    //   отримаємо та валідуємо дані отриманні від користувача
    // шукуємо чи є користувач у базі
    // якщо знайши викидаємо помилку
    // хешуємо пароль
    //  зберігаємо користвача
    const { email, password } = req.body;

    if (!email || !password) {
      res.status(400);
      throw new Error("Provide all fields");
    }

    const condidat = await usersModel.findOne({ email });

    if (condidat) {
      res.status(400);
      throw new Error("User already exist");
    }

    const hashPassword = bcrypt.hashSync(password, 5);

    const roles = await rolesModel.findOne({ value: "USER" });

    const user = await usersModel.create({
      ...req.body,
      password: hashPassword,
      roles: [roles.value],
    });

    res.status(201).json({
      code: 201,
      data: {
        email: user.email,
      },
    });
  })
);

app.post(
  "/login",
  asyncHandler(async (req, res) => {
    //   отримуємо та валідуємо дані отримані від користувача
    // шукаємо користувача у базі та розхешовуємо пароль
    //  як не знайшли або не розшрифували - invalid email or password
    //  якщо все ок , генеруємо токен
    //  зберігаємо токен до користувача

    const { email, password } = req.body;

    if (!email || !password) {
      res.status(400);
      throw new Error("Provide all fields");
    }

    const user = await usersModel.findOne({ email });

    if (!user) {
      res.status(400);
      throw new Error("invalid email or password");
    }

    const isValidPassword = bcrypt.compareSync(password, user.password);

    if (!isValidPassword) {
      res.status(400);
      throw new Error("invalid email or password");
    }

    const token = generateToken({
      friends: ["Dima", "Artem", "Vlad"],
      id: user._id,
      roles: user.roles,
    });

    user.token = token;

    await user.save();

    res.status(200).json({
      code: 200,
      data: {
        email: user.email,
        token: user.token,
      },
    });
  })
);

function generateToken(data) {
  const payload = { ...data };
  return jwt.sign(payload, "pizza", { expiresIn: "2h" });
}

app.get(
  "/logout",
  authMiddleware,
  asyncHandler(async (req, res) => {
    const { id } = req.user;

    const user = await usersModel.findById(id);
    user.token = null;
    await user.save();

    res.status(200).json({
      code: 200,
      data: {
        email: user.email,
        message: "logout success",
      },
    });
  })
);

app.use(errorHandler);

connectDb();

app.listen(process.env.PORT, () => {
  console.log("Server is running on port ".green.bold.italic + process.env.PORT);
});

// eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmllbmRzIjpbIkRpbWEiLCJBcnRlbSIsIlZsYWQiXSwiaWF0IjoxNjkxMjM3MjM4LCJleHAiOjE2OTEyNDQ0Mzh9.-KlVJIhxgnrgAXQhE96OquoKgZ--jf5vVIS61BnLQk4
