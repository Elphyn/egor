const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const startCoordsInput = document.getElementById("startCoords");
const endCoordsInput = document.getElementById("endCoords");
const drawLineBtn = document.getElementById("drawLineBtn");
const ellipseCenterCoordsInput = document.getElementById("ellipseCenterCoords");
const ellipseRadiiInput = document.getElementById("ellipseRadii");
const drawEllipseBtn = document.getElementById("drawEllipseBtn");

function ddaLine(x0, y0, x1, y1) {
    let points = [];
    let dx = x1 - x0;
    let dy = y1 - y0;
    let steps = Math.max(Math.abs(dx), Math.abs(dy));

    let xIncrement = dx / steps;
    let yIncrement = dy / steps;

    let x = x0;
    let y = y0;

    for (let i = 0; i <= steps; i++) {
        points.push({ x: Math.round(x), y: Math.round(y) });
        x += xIncrement;
        y += yIncrement;
    }

    return points;
}

function drawGrid() {
    const gridSize = 1;
    ctx.strokeStyle = "#ccc";
    ctx.beginPath();
    for (let x = 0; x <= canvas.width; x += gridSize) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
    }
    for (let y = 0; y <= canvas.height; y += gridSize) {
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
    }
    ctx.stroke();
}

function drawLine(x0, y0, x1, y1) {
    let points = ddaLine(x0, y0, x1, y1);

    ctx.beginPath();

    for (let point of points) {
        ctx.rect(point.x * 10, point.y * 10, 10, 10);
    }

    ctx.fillStyle = "black";
    ctx.fill();
}
function parseCoordinates(input) {
    const coords = input.split(",").map(Number);
    if (coords.length !== 2 || coords.some(isNaN)) {
        return null;
    }
    return coords;
}

drawGrid();

drawLineBtn.addEventListener("click", () => {
    const startCoords = parseCoordinates(startCoordsInput.value);
    const endCoords = parseCoordinates(endCoordsInput.value);

    if (!startCoords || !endCoords) {
        alert("Invalid input. Please provide coordinates in the format x,y");
        return;
    }
    const [x0, y0] = startCoords;
    const [x1, y1] = endCoords;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawGrid();
    drawLine(x0, y0, x1, y1);
});


function bresenhamEllipse(x0, y0, a, b) {
    let points = [];

    let a2 = a * a;
    let b2 = b * b;
    let twoA2 = 2 * a2;
    let twoB2 = 2 * b2;
    let x = 0;
    let y = b;
    let px = 0;
    let py = twoA2 * y;


    // Region 1
    let p = Math.round(b2 - (a2 * b) + (0.25 * a2));
    while (px < py) {
        points.push({ x: x + x0, y: y + y0 });
        points.push({ x: -x + x0, y: y + y0 });
        points.push({ x: x + x0, y: -y + y0 });
        points.push({ x: -x + x0, y: -y + y0 });
        x++;
        px += twoB2;
        if (p < 0) {
            p += b2 + px;
        } else {
            y--;
            py -= twoA2;
            p += b2 + px - py;
        }
    }

    // Region 2
    p = Math.round(b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2);
    //было y > 0
    while (y >= 0) {
        points.push({ x: x + x0, y: y + y0 });
        points.push({ x: -x + x0, y: y + y0 });
        points.push({ x: x + x0, y: -y + y0 });
        points.push({ x: -x + x0, y: -y + y0 });
        y--;
        py -= twoA2;
        if (p > 0) {
            p += a2 - py;
        } else {
            x++;
            px += twoB2;
            p += a2 - py + px;
        }
    }
    return points;
}
function drawEllipse(x0, y0, a, b) {
    const points = bresenhamEllipse(x0, y0, a, b);

    ctx.beginPath();
    for (let point of points) {
        ctx.rect(point.x * 10, point.y * 10, 10, 10);
    }

    // Fill the missing pixels
    // ctx.rect((x0 + a) * 10, y0 * 10, 10, 10);
    // ctx.rect(x0 * 10, (y0 + b) * 10, 10, 10);//this is wrong

    ctx.fillStyle = "black";
    ctx.fill();
}






drawEllipseBtn.addEventListener("click", () => {
    const centerCoords = parseCoordinates(ellipseCenterCoordsInput.value);
    const radii = parseCoordinates(ellipseRadiiInput.value);
    
    if (!centerCoords || !radii) {
        alert("Invalid input. Please provide coordinates in the format x,y");
        return;
    }
    
    const [x0, y0] = centerCoords;
    const [a, b] = radii;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawGrid();
    drawEllipse(x0, y0, a, b);//here
});
