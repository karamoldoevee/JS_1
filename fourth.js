const Duck = {

    name: 'Дональд',

    color: 'белый',

    old: 1,
    toStr: function () {
        console.log(`${this.name}, ${this.color}, ${this.old}`)
    },
    say: function () {
        console.log('кря кря')
    }
};

Duck.toStr();
Duck.say();