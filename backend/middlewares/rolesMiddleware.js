const jwt = require("jsonwebtoken");
module.exports = (rolesArr) => {
  return (req, res, next) => {
    try {
      const roles = req.user.roles;
      let hasRole = false;
      roles.forEach((role) => {
        if (rolesArr.includes(role)) {
          hasRole = true;
        }
      });

      if (!hasRole) {
        res.status(403);
        throw new Error("Forbiden");
      }
      next();
    } catch (error) {
      res.status(403).json({
        code: 403,
        message: error.message,
      });
    }
  };
};

//  { friends: [ 'Dima', 'Artem', 'Vlad' ],
//   id: '64ce4b09d02b6cea34a99bcf',
//   roles: [ 'USER' ],
//   iat: 1691241752,
//   exp: 1691248952
// }
