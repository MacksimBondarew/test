const { connect } = require("mongoose");

const connectDb = async () => {
    try {
        const db = await connect(process.env.DB_HOST);
        console.log(
            `DATABASE is connected. Name: ${db.connection.name}. Host: ${db.connection.host}. Port: ${db.connection.port}`.green.bold.italic
        );
    } catch (error) {
        console.log(error.message.red.bold);
        process.exit(1);
    }
};

module.exports = connectDb;

// const Cat = mongoose.model('Cat', { name: String });

// const kitty = new Cat({ name: 'Zildjian' });
// kitty.save().then(() => console.log('meow'));
