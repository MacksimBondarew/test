const fs = require("fs/promises");
const path = require("path");
const { json } = require("stream/consumers");
// console.log(__dirname);
// console.log(path.join());
// console.log(path.resolve());
const userPath = path.join(__dirname, "..", "db", "users.json");

class FileOperations {
    constructor(path) {
        this.path = path;
    }

    read = async () => {
        return await fs.readFile(this.path, "utf-8");
    };

    display = async () => {
        const data = await this.read();
        console.log(data);
    };

    create = async (users) => {
        return await fs.writeFile(this.path, JSON.stringify(users, null, 2));
    };

    update = async (user) => {
        const data = JSON.parse(await this.read());
        data.push(user);
        return await this.create(data);
    };
    updateOne = async (user) => {
        const data = JSON.parse(await this.read());
        const updated = data.map((item) => {
            if (item.id === Number(user.id)) {
                item.name = user.name;
            } 
            return item;
        });
        return await this.create(updated);
    };
    remove = async () => {
        return await fs.unlink(this.path);
    };
    removeOne = async (user) => {
        const data = JSON.parse(await this.read());
        const removeUser = data.filter(item => {
            return item.id !== user.id;
        });
        return await this.create(removeUser);
    };
}
const file = new FileOperations(userPath);
// file.display();
// const users = [
//     { "id": 1, "name": "Dima" },
//     { "id": 2, "name": "Max" },
//     { "id": 3, "name": "Luda" }
// ]

// file.create(users);

// file.update({ id: 4, name: "Andriy" });
// file.remove();
// file.updateOne({ id: 2, name: "Max Bondarew" });
// file.removeOne({ id: 2, name: "Max Bondarew" });

const asyncHandler = async (operation, data) => {
    try {
        if (data) {
            await operation(data);
        } else {
            await operation();
        }
    } catch (error) {
        console.log(error.message);
    }
};

// asyncHandler(file.display.bind(file));
// asyncHandler(file.display);
// asyncHandler(file.update, { id: 5, name: "Masha" });
asyncHandler(file.updateOne, { id: 3, name: "Masha Chumak" });