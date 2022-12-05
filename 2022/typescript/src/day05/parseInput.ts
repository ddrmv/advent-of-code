import { Move, Stack, Supplies } from "./types";

export const parseInput = (input: string): [Supplies, Move[]] => {
  const [suppliesString, movesString] = input.trimEnd().split("\n\n");

  const moves = convertMoves(movesString);
  const supplies = suppliesStringToSupplies(suppliesString);

  return [supplies, moves];
};

const suppliesStringToSupplies = (suppliesString: string): Supplies => {
  const rows = suppliesString.split("\n");
  let supplies: Supplies = { stacks: [] };

  for (let column = 1; column < rows[0].length; column += 4) {
    const stack: Stack = { crates: [] };
    for (let row = rows.length - 2; row >= 0; row--) {
      if (rows[row][column] !== " ") {
        stack.crates.push(rows[row][column]);
      }
    }
    supplies.stacks.push(stack);
  }

  return supplies;
};

const convertMoves = (movesString: string): Move[] => {
  const moveRows = movesString.split("\n");

  let moves: Move[] = [];
  for (const moveRow of moveRows) {
    moves.push(moveStringToMove(moveRow));
  }

  return moves;
};

const moveStringToMove = (moveString: string): Move => {
  let move: Move;
  const numbersOnly = moveString
    .replace("move ", "")
    .replace("from ", "")
    .replace("to ", "");
  const numbers = numbersOnly.split(" ");
  move = {
    amount: Number(numbers[0]),
    from: Number(numbers[1]) - 1,
    to: Number(numbers[2]) - 1,
  };
  return move;
};
