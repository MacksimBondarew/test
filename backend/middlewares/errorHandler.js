module.exports = (error, req, res, next) => {
    const statusCode = res.statusCode || 500;
    res.status(statusCode);
    res.json({
        message: error.message,
        stack: error.stack
    })
}