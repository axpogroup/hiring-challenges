// Canvas setup
const canvas = document.getElementById('pong-canvas');
const ctx = canvas.getContext('2d');

// Game state
let gameRunning = false;
let playerScore = 0;
let computerScore = 0;

// Paddle properties
const paddleWidth = 10;
const paddleHeight = 100;
const paddleSpeed = 6;

// Player paddle (left)
const player = {
    x: 20,
    y: canvas.height / 2 - paddleHeight / 2,
    width: paddleWidth,
    height: paddleHeight,
    dy: 0
};

// Computer paddle (right)
const computer = {
    x: canvas.width - 30,
    y: canvas.height / 2 - paddleHeight / 2,
    width: paddleWidth,
    height: paddleHeight,
    dy: 4
};

// Ball properties
const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 8,
    speed: 5,
    dx: 5,
    dy: 5
};

// Keyboard state
const keys = {};

// Event listeners
document.addEventListener('keydown', (e) => {
    keys[e.key.toLowerCase()] = true;
});

document.addEventListener('keyup', (e) => {
    keys[e.key.toLowerCase()] = false;
});

document.getElementById('start-btn').addEventListener('click', startGame);
document.getElementById('reset-btn').addEventListener('click', resetGame);

// Draw functions
function drawRect(x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
}

function drawCircle(x, y, r, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
}

function drawNet() {
    const netWidth = 4;
    const netHeight = 10;
    const gap = 15;
    
    for (let i = 0; i < canvas.height; i += netHeight + gap) {
        drawRect(canvas.width / 2 - netWidth / 2, i, netWidth, netHeight, '#ffffff40');
    }
}

function draw() {
    // Clear canvas
    drawRect(0, 0, canvas.width, canvas.height, '#000000');
    
    // Draw net
    drawNet();
    
    // Draw paddles
    drawRect(player.x, player.y, player.width, player.height, '#ffffff');
    drawRect(computer.x, computer.y, computer.width, computer.height, '#ffffff');
    
    // Draw ball
    drawCircle(ball.x, ball.y, ball.radius, '#ffffff');
}

// Update functions
function updatePlayer() {
    if (keys['w'] && player.y > 0) {
        player.y -= paddleSpeed;
    }
    if (keys['s'] && player.y + player.height < canvas.height) {
        player.y += paddleSpeed;
    }
}

function updateComputer() {
    // Simple AI: follow the ball
    const computerCenter = computer.y + computer.height / 2;
    
    if (computerCenter < ball.y - 35) {
        computer.y += computer.dy;
    } else if (computerCenter > ball.y + 35) {
        computer.y -= computer.dy;
    }
    
    // Keep computer paddle within bounds
    if (computer.y < 0) computer.y = 0;
    if (computer.y + computer.height > canvas.height) {
        computer.y = canvas.height - computer.height;
    }
}

function updateBall() {
    ball.x += ball.dx;
    ball.y += ball.dy;
    
    // Ball collision with top and bottom walls
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.dy *= -1;
    }
    
    // Ball collision with player paddle
    if (ball.x - ball.radius < player.x + player.width &&
        ball.y > player.y &&
        ball.y < player.y + player.height) {
        ball.dx = Math.abs(ball.dx); // Ensure ball moves right
        
        // Add some variation based on where it hits the paddle
        const hitPos = (ball.y - player.y) / player.height;
        ball.dy = (hitPos - 0.5) * 10;
    }
    
    // Ball collision with computer paddle
    if (ball.x + ball.radius > computer.x &&
        ball.y > computer.y &&
        ball.y < computer.y + computer.height) {
        ball.dx = -Math.abs(ball.dx); // Ensure ball moves left
        
        // Add some variation based on where it hits the paddle
        const hitPos = (ball.y - computer.y) / computer.height;
        ball.dy = (hitPos - 0.5) * 10;
    }
    
    // Ball goes out of bounds (scoring)
    if (ball.x - ball.radius < 0) {
        // Computer scores
        computerScore++;
        updateScore();
        resetBall();
        checkWinner();
    } else if (ball.x + ball.radius > canvas.width) {
        // Player scores
        playerScore++;
        updateScore();
        resetBall();
        checkWinner();
    }
}

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.dx = (Math.random() > 0.5 ? 1 : -1) * ball.speed;
    ball.dy = (Math.random() * 2 - 1) * ball.speed;
}

function updateScore() {
    document.getElementById('player-score').textContent = playerScore;
    document.getElementById('computer-score').textContent = computerScore;
}

function checkWinner() {
    const winScore = 5;
    if (playerScore >= winScore) {
        gameRunning = false;
        showMessage('You Win! 🎉');
    } else if (computerScore >= winScore) {
        gameRunning = false;
        showMessage('Computer Wins! 🤖');
    }
}

function showMessage(msg) {
    const messageEl = document.getElementById('game-message');
    messageEl.textContent = msg;
    messageEl.style.display = 'block';
    setTimeout(() => {
        messageEl.style.display = 'none';
    }, 3000);
}

function startGame() {
    if (!gameRunning) {
        gameRunning = true;
        gameLoop();
    }
}

function resetGame() {
    gameRunning = false;
    playerScore = 0;
    computerScore = 0;
    updateScore();
    resetBall();
    player.y = canvas.height / 2 - paddleHeight / 2;
    computer.y = canvas.height / 2 - paddleHeight / 2;
    draw();
}

function gameLoop() {
    if (!gameRunning) return;
    
    updatePlayer();
    updateComputer();
    updateBall();
    draw();
    
    requestAnimationFrame(gameLoop);
}

// Initial draw
draw();
