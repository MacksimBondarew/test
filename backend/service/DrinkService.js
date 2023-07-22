const DrinkModel = require("../models/drinksModel");

class DrinksService {
    all = async () => {
        const drinks = await DrinkModel.find({});
        if (!drinks) {
            return null;
        };
        return drinks;
    }
};

module.exports = new DrinksService();