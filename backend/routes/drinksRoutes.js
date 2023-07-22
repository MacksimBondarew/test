// Cannot GET /api/v1/drinks
const drinksContoller = require('../controllers/DrinksContoler')

const drinksRouter = require('express').Router();

//додати напій

drinksRouter.post('/drinks', (req, res, next) => {
    console.log('joi');
    next();
} , drinksContoller.add)

// отримати всі 

drinksRouter.get('/drinks', drinksContoller.getAll)

// отримати один

drinksRouter.get('/drinks/:id', drinksContoller.getOne)

// оновити напій

drinksRouter.put('/drinks/:id', drinksContoller.update)

// видалити напій

drinksRouter.delete('/drinks/:id', drinksContoller.remove)

module.exports = drinksRouter;
