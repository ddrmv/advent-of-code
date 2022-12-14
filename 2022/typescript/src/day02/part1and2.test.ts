import {
  calculateTotalScoreOld,
  calculateTotalScore,
  resolveMatch,
} from "./part1and2";
import { readFileSync } from "fs";
import path from "path";

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

describe("calculateTotalScoreOld", () => {
  it("returns total score for one round", () => {
    expect(calculateTotalScoreOld("A Y\n")).toBe(8);
  });

  it("returns total score for three rounds", () => {
    expect(calculateTotalScoreOld("A Y\nB X\nC Z\n")).toBe(15);
  });

  it("returns correct solution to puzzle", () => {
    const filePath = path.join(__dirname, "../../../input/day02");
    const fileString = readFileSync(filePath, "utf8");
    expect(calculateTotalScoreOld(fileString)).toBe(14827);
  });
});

describe("calculateTotalScore", () => {
  it("returns total score for three rounds", () => {
    expect(calculateTotalScore("A Y\nB X\nC Z\n")).toBe(12);
  });

  it("returns correct solution to puzzle", () => {
    const filePath = path.join(__dirname, "../../../input/day02");
    const fileString = readFileSync(filePath, "utf8");
    expect(calculateTotalScore(fileString)).toBe(13889);
  });
});
