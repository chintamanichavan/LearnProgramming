let defaultResult = 0;
let currentResult = defaultResult;

currentResult = (currentResult +10) * 3 / 2 -1;

function add(){
    return currentResult + userInput.value;
}

function subtract(){
    return currentResult - userInput.value;
}

function multiply(){
    return currentResult * userInput.value;
}

function divide(){
    return currentResult + userInput.value;
}

addBtn.addEventListener('click', add);
subtractBtn.addEventListener('click', subtract);
multiplyBtn.addEventListener('click', multiply);
divideBtn.addEventListener('click', divide);


let calculateDescription = `(${defaultResult} + 10) * 3 / 2 - 1`;
outputResult(currentResult, calculateDescription)