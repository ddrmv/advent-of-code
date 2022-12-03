import { calculateTotalScore, resolveMatch } from "./part1";

describe("resolveMatch", () => {
  it("returns win correctly", () => {
    expect(resolveMatch("paper", "scissors")).toEqual("win");
    expect(resolveMatch("rock", "paper")).toEqual("win");
    expect(resolveMatch("scissors", "rock")).toEqual("win");
  });
  it("returns loss correctly", () => {
    expect(resolveMatch("paper", "rock")).toEqual("loss");
    expect(resolveMatch("rock", "scissors")).toEqual("loss");
    expect(resolveMatch("scissors", "paper")).toEqual("loss");
  });
  it("returns draw correctly", () => {
    expect(resolveMatch("paper", "paper")).toEqual("draw");
    expect(resolveMatch("rock", "rock")).toEqual("draw");
    expect(resolveMatch("scissors", "scissors")).toEqual("draw");
  });
});

describe("calculateTotalScore", () => {
  it("returns total score for one round", () => {
    expect(calculateTotalScore("A Y\n")).toBe(8);
  });

  it("returns total score for three rounds", () => {
    expect(calculateTotalScore("A Y\nB X\nC Z\n")).toBe(15);
  });
});
