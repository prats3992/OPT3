const symbolSelection = document.getElementById("symbol-selection");
const symbolSelect = document.getElementById("symbol");

const board = document.getElementById("board");
const cells = document.querySelectorAll(".cell");
const result = document.getElementById("result");
const resetButton = document.getElementById("reset");

let userSymbol = "X";
let currentPlayer = userSymbol;
let gameBoard = ["", "", "", "", "", "", "", "", ""];
let gameOver = false;

function handleSymbolChange(e) {
    userSymbol = e.target.value;
    currentPlayer = userSymbol;
    cells.forEach((cell) => (cell.textContent = ""));
    resetGame();
}

symbolSelect.addEventListener("change", handleSymbolChange);

function checkWin() {
    const winPatterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
            return gameBoard[a];
        }
    }

    if (!gameBoard.includes("")) {
        return "Draw";
    }

    return null;
}

function handleCellClick(e) {
    const cellIndex = parseInt(e.target.id.split("-")[1]);

    if (gameBoard[cellIndex] === "" && !gameOver) {
        gameBoard[cellIndex] = currentPlayer;
        cells[cellIndex].textContent = currentPlayer;
        currentPlayer = currentPlayer === "X" ? "O" : "X";

        const winner = checkWin();
        if (winner) {
            gameOver = true;
            if (winner === "Draw") {
                result.textContent = "It's a draw!";
            } else {
                result.textContent = `${winner} wins!`;
            }
        }
    }
}

function resetGame() {
    gameBoard = ["", "", "", "", "", "", "", "", ""];
    cells.forEach((cell) => (cell.textContent = ""));
    result.textContent = "";
    gameOver = false;
    currentPlayer = userSymbol;
}

board.addEventListener("click", handleCellClick);
resetButton.addEventListener("click", resetGame);
