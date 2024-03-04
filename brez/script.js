const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const startCoordsInput = document.getElementById("startCoords");
const endCoordsInput = document.getElementById("endCoords");
const drawLineBtn = document.getElementById("drawLineBtn");
const ellipseCenterCoordsInput = document.getElementById("ellipseCenterCoords");
const ellipseRadiiInput = document.getElementById("ellipseRadii");
const drawEllipseBtn = document.getElementById("drawEllipseBtn");

function bresenhamLine(x0, y0, x1, y1) {
    let points = [];
    let dx = Math.abs(x1 - x0);
    let dy = Math.abs(y1 - y0);
    let sx = x0 < x1 ? 1 : -1;
    let sy = y0 < y1 ? 1 : -1;
    let err = dx - dy;

    while (true) {
        points.push({ x: x0, y: y0 });

        if (x0 === x1 && y0 === y1) break;

        let e2 = 2 * err;

        if (e2 > -dy) {
            err -= dy;
            x0 += sx;
        }

        if (e2 < dx) {
            err += dx;
            y0 += sy;
        }
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
    let points = bresenhamLine(x0, y0, x1, y1);

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

    const a2 = a * a;
    const b2 = b * b;
    let x = 0;
    let y = b;
    let sigma;

    // Points in the first region
    sigma = 2 * b2 + a2 * (1 - 2 * b);
    while (b2 * x <= a2 * y) {
        points.push({ x: x + x0, y: y + y0 });
        points.push({ x: -x + x0, y: y + y0 });
        points.push({ x: x + x0, y: -y + y0 });
        points.push({ x: -x + x0, y: -y + y0 });

        if (sigma >= 0) {
            sigma += a2 * (1 - y);
            y--;
        }
        sigma += b2 * (2 * x + 3);
        x++;
    }

    // Points in the second region
    sigma = 2 * a2 + b2 * (1 - 2 * a);
    x = a;
    y = 0;

    while (a2 * y <= b2 * x) {
        points.push({ x: x + x0, y: y + y0 });
        points.push({ x: -x + x0, y: y + y0 });
        points.push({ x: x + x0, y: -y + y0 });
        points.push({ x: -x + x0, y: -y + y0 });

        if (sigma >= 0) {
            sigma += b2 * (1 - x);
            x--;
        }
        sigma += a2 * (2 * y + 3);
        y++;
    }

    return points;
}

function drawEllipse(x0, y0, a, b) {
    const points = bresenhamEllipse(x0, y0, a, b);

    ctx.beginPath();
    for (let point of points) {
        ctx.rect(point.x * 10, point.y * 10, 10, 10);
    }
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
    drawEllipse(x0, y0, a, b);
});
