const { Schema, model } = require('mongoose');

const drink = new Schema({
    name: {
        type: String,
        required: [true, 'DB: name is required'],
    },
    value: {
        type: Number,
        required: [true, 'DB: value is required'],
    },
    adult: {
        type: Boolean,
        default: true,
    }
})

module.exports = model('drinks', drink)