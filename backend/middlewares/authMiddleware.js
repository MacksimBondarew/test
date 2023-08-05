const jwt = require("jsonwebtoken");
module.exports = (req, res, next) => {
  //   отримуємо токен
  // розшифровуємо токен
  //  передаємо інформацію з токеном далі
  try {
    const [tokenType, token] = req.headers.authorization.split(" ");
    if (tokenType === "Bearer" && token) {
      const decodet = jwt.verify(token, "pizza");
      req.user = decodet;
      next();
    }
  } catch (error) {
    res.status(401).json({
      code: 401,
      message: error.message,
    });
  }
};
