const DrinkModel = require("../models/drinksModel");
const asyncHandler = require("express-async-handler");
const DrinkService = require("../service/DrinkService");

class DrinksContoller {
    add = asyncHandler(async (req, res) => {
        const { name, value } = req.body;
        if (!name || !value) {
            res.status(400);
            throw new Error("Provide all required fields")
        }
        const drink = await DrinkModel.create({ ...req.body });
        res.status(201).json({
            code: 201,
            data: {
                drink,
            }
        })
    });

    // getAll = asyncHandler(async (req, res) => {
    //     const drinks = await DrinkModel.find({});
        
    //     res.status(200).json({
    //         code: 200,
    //         data: {
    //             drinks,
    //             qty: drinks.length, 
    //         },
    //     })
    // });

    
    getAll = asyncHandler(async (req, res) => {
        const drinks = await DrinkService.all();
        if (!drinks) {
            res.status(400);
            throw new Error("Unable to fetch")
        }
        res.status(200).json({
            code: 200,
            data: {
                drinks,
                qty: drinks.length, 
            },
        })
    });

    getOne = asyncHandler(async (req, res) => {
        const { id } = req.body;
        await DrinkModel.findById(id);
    });

    update = (req, res) => {
        const drinks = await 
    };

    remove = (req, res) => {
        res.send("remove");
    };
}

module.exports = new DrinksContoller();
