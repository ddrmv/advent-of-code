import { readFileSync } from "fs";
import path from "path";
import { parseInput } from "./parseInput";
import { Ship } from "./ship";
import { Move, Stack, Supplies } from "./types";

describe("Ship", () => {
  it("executes move", () => {
    const move: Move = { amount: 2, from: 1, to: 0 };
    const supplies: Supplies = {
      stacks: [{ crates: ["Z", "N"] }, { crates: ["M", "C", "D"] }],
    };
    const ship = new Ship();
    ship.setSupplies(supplies);
    ship.doMove(move);
    expect(ship.getSuppliesTops()).toEqual("CM");
  });

  it("executes multiple moves", () => {
    const move1: Move = { amount: 1, from: 1, to: 0 };
    const move2: Move = { amount: 1, from: 1, to: 0 };

    const supplies: Supplies = {
      stacks: [{ crates: ["Z", "N"] }, { crates: ["M", "C", "D"] }],
    };
    const ship = new Ship();
    ship.setSupplies(supplies);
    ship.doManyMoves([move1, move2]);
    expect(ship.getSuppliesTops()).toEqual("CM");
  });

  it("returns answer to puzzle part 1", () => {
    const filePath = path.join(__dirname, "../../../input/day05");
    const fileString = readFileSync(filePath, "utf8");
    const [supplies, moves] = parseInput(fileString);
    const ship = new Ship();
    ship.setSupplies(supplies);
    ship.doManyMoves(moves);
    expect(ship.getSuppliesTops()).toEqual("VQZNJMWTR");
  });

  it("returns answer to puzzle part 1", () => {
    const filePath = path.join(__dirname, "../../../input/day05");
    const fileString = readFileSync(filePath, "utf8");
    const [supplies, moves] = parseInput(fileString);
    const ship = new Ship();
    ship.setSupplies(supplies);
    ship.doManyMoves9001(moves);
    expect(ship.getSuppliesTops()).toEqual("NLCDCLVMQ");
  });
});
