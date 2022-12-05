import { Supplies, Move, Stack } from "./types";

export class Ship {
  _supplies: Supplies;

  constructor() {
    this._supplies = { stacks: [] };
  }

  setSupplies = (supplies: Supplies) => {
    this._supplies = supplies;
  };

  doMove = (move: Move) => {
    for (let i = 0; i < move.amount; i++) {
      this._supplies.stacks[move.to].crates.push(
        this._supplies.stacks[move.from].crates.pop() as string
      );
    }
  };

  doManyMoves = (moves: Move[]) => {
    for (const move of moves) {
      this.doMove(move);
    }
  };

  doMove9001 = (move: Move) => {
    this._supplies.stacks[move.to].crates.push(
      ...this._supplies.stacks[move.from].crates.splice(-move.amount)
    );
  };

  doManyMoves9001 = (moves: Move[]) => {
    for (const move of moves) {
      this.doMove9001(move);
    }
  };

  getSuppliesTops = () => {
    let result = "";
    for (const stack of this._supplies.stacks) {
      result += stack.crates.pop();
    }
    return result;
  };
}
