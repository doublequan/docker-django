
var firNum = 0;
var operator = "";
var enterNumFlag = true;

function numberOnClick(button) {
    var display = document.getElementById("display");
    var value = button.innerHTML;
    if (display.innerHTML == "0" || enterNumFlag) {
        display.innerHTML = value;
        enterNumFlag = false;
    } else {
        var str = display.innerHTML + value;
        if (str.length > 14) return;
        else display.innerHTML = str;
    }
}

function operatorOnClick(button) {
    var display = document.getElementById("display");
    var op = button.innerHTML;
    switch (op) {
        case ".":
            var str = display.innerHTML;
            if (enterNumFlag) {
                display.innerHTML = "0.";
                enterNumFlag = false;
                return;
            } else if (str == "-") {
                display.innerHTML = "-0.";
                return;
            }
            if (str.indexOf(".") >= 0) return;
            else display.innerHTML += op;
            break;
        case "-":
            if (enterNumFlag) {
                display.innerHTML = "-";
                enterNumFlag = false;
                break;
            }
        case "+":
        case "*":
        case "/":
            operator = op;
            firNum = parseFloat(display.innerHTML);
            enterNumFlag = true;
            break;
        case "=":
            enterNumFlag = true;
            if (operator == "") return;
            var rst = calculate(parseFloat(firNum), parseFloat(display.innerHTML), operator);
            firNum = 0;
            operator = "";
            updateDisplay(rst);
            break;
    }
}

function calculate(n1, n2, op) {
    console.log(n1 + op + n2);
    switch (op) {
        case "+":
            return n1 + n2;
        case "-":
            return n1 - n2;
        case "*":
            return n1 * n2;
        case "/":
            return n1 / n2;
    }
}

function updateDisplay(rst) {
    var display = document.getElementById("display");
    var str = rst.toString();
    if (str.length <= 14) {
        display.innerHTML = rst;
    } else {
        var index = str.indexOf(".");
        if (index < 0 || index > 14) {
            display.innerHTML = "EXCEED LIMIT";
        } else {
            console.log(14 - index);
            display.innerHTML = rst.toFixed(14 - index);
        }

    }

}