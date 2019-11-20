const foods = ['молоко', 'пиво', 'пиво', 'молоко', 'молоко', 'молоко'];

foods.forEach(function (item) {
    if(item === 'молоко'){
        console.log('Хорошо');
    }
    else if(item === 'пиво'){
        console.log('Плохо');
    }
    });