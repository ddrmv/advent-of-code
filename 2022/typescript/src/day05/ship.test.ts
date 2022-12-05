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
});
