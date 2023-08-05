const { Schema, model } = require("mongoose");

const UsersSchema = new Schema({
  name: {
    type: String,
    default: "Sandra",
  },
  email: { type: String, required: [true, "DB: email is required"] },
  password: { type: String, required: [true, "DB: password is required"] },
  token: { type: String, default: null },
  roles: [
    {
      type: String,
      ref: "roles",
    },
  ],
});

module.exports = model("users", UsersSchema);
