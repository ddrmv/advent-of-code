type Move = "rock" | "paper" | "scissors";

type Outcome = "win" | "loss" | "draw";

export const resolveMatch = (elfMove: Move, myMove: Move): Outcome => {
  let outcomeMap = new Map<string, Outcome>();
  outcomeMap.set("rock" + "rock", "draw");
  outcomeMap.set("rock" + "paper", "win");
  outcomeMap.set("rock" + "scissors", "loss");
  outcomeMap.set("paper" + "rock", "loss");
  outcomeMap.set("paper" + "paper", "draw");
  outcomeMap.set("paper" + "scissors", "win");
  outcomeMap.set("scissors" + "rock", "win");
  outcomeMap.set("scissors" + "paper", "loss");
  outcomeMap.set("scissors" + "scissors", "draw");

  let outcome: Outcome | undefined;
  if (!outcomeMap.has(elfMove + myMove)) {
    throw new Error("Assert: Outcome should not be undefined");
  } else {
    outcome = outcomeMap.get(elfMove + myMove) as Outcome;
  }
  return outcome;
};

const calculateMatchOutcomePoints = (elfMove: Move, myMove: Move) => {
  const outcome = resolveMatch(elfMove, myMove);
  const outcomePoints = { win: 6, loss: 0, draw: 3 };
  return outcomePoints[outcome];
};

const calculateMoveChoicePoints = (myMove: Move) => {
  const moveChoicePoints = { rock: 1, paper: 2, scissors: 3 };
  return moveChoicePoints[myMove];
};

export const calculateTotalScore = (input: string) => {
  const moveMap: { [key: string]: Move } = {
    A: "rock",
    B: "paper",
    C: "scissors",
    X: "rock",
    Y: "paper",
    Z: "scissors",
  };

  let elfMove: Move;
  let myMove: Move;

  const matches = input.trim().split("\n");

  let total = 0;

  for (let match of matches) {
    elfMove = moveMap[match[0]];
    myMove = moveMap[match[2]];
    total += calculateMatchOutcomePoints(elfMove, myMove);
    total += calculateMoveChoicePoints(myMove);
  }

  return total;
};
