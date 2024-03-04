var isValid = function(s) {
    // string to array
    //loop over array
    //if first index of an array is one of these: ),},], return false
    //if not loop over array looking for closing parenthesis, if not found return false
    
    const array = [...s]
    if (array[0] == ')' || array[0] == ']' || array[0] == '}')
        return false

    for (let i = 0; i < array.length; i++){
        for(let j = i; j < array.length; j = 2*j -1)
    }
    
    
    
    
};

// isValid('[]')
console.log(
    isValid('()')
)