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

export const calculateTotalScoreOld = (input: string) => {
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

const findMyMoveFromElfMoveAndOutcome = (elfMove: Move, outcome: Outcome) => {
  let myMoveMap = new Map<string, Move>();
  myMoveMap.set("rock" + "loss", "scissors");
  myMoveMap.set("rock" + "draw", "rock");
  myMoveMap.set("rock" + "win", "paper");
  myMoveMap.set("paper" + "loss", "rock");
  myMoveMap.set("paper" + "draw", "paper");
  myMoveMap.set("paper" + "win", "scissors");
  myMoveMap.set("scissors" + "loss", "paper");
  myMoveMap.set("scissors" + "draw", "scissors");
  myMoveMap.set("scissors" + "win", "rock");
  const myMove = myMoveMap.get(elfMove + outcome);
  if (myMove === undefined) {
    throw new Error("Assert: Move should not be undefined");
  } else {
    return myMove;
  }
};

export const calculateTotalScore = (input: string) => {
  const moveMap: { [key: string]: Move } = {
    A: "rock",
    B: "paper",
    C: "scissors",
  };

  const outcomeMap: { [key: string]: Outcome } = {
    X: "loss",
    Y: "draw",
    Z: "win",
  };

  let elfMove: Move;
  let myMove: Move;
  let outcome: Outcome;

  const matches = input.trim().split("\n");

  let total = 0;

  for (let match of matches) {
    elfMove = moveMap[match[0]];
    outcome = outcomeMap[match[2]];
    myMove = findMyMoveFromElfMoveAndOutcome(elfMove, outcome);
    total += calculateMatchOutcomePoints(elfMove, myMove);
    total += calculateMoveChoicePoints(myMove);
  }

  return total;
};
