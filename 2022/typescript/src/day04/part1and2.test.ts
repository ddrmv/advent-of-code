import { readFileSync } from "fs";
import path from "path";
import { countFullOverlaps, countPartialOverlaps } from "./part1and2";

describe("countFullOverlaps", () => {
  it("returns 1 for a one-line input of full overlap", () => {
    expect(countFullOverlaps("2-8,3-7\n")).toBe(1);
    expect(countFullOverlaps("6-6,4-6\n")).toBe(1);
    expect(countFullOverlaps("2-6,4-8\n")).toBe(0);
  });

  it("returns 2 for specs example input", () => {
    const input =
      "2-4,6-8\n\
2-3,4-5\n\
5-7,7-9\n\
2-8,3-7\n\
6-6,4-6\n\
2-6,4-8\n";
    expect(countFullOverlaps(input)).toBe(2);
  });

  it("returns answer for puzzle part 1", () => {
    const filePath = path.join(__dirname, "../../../input/day04");
    const fileString = readFileSync(filePath, "utf8");
    expect(countFullOverlaps(fileString)).toBe(599);
  });
});

describe("countPartialOverlaps", () => {
  it("returns 4 for specs in example input", () => {
    const input =
      "2-4,6-8\n\
2-3,4-5\n\
5-7,7-9\n\
2-8,3-7\n\
6-6,4-6\n\
2-6,4-8\n";
    expect(countPartialOverlaps(input)).toBe(4);
  });

  it("returns answer for puzzle part 2", () => {
    const filePath = path.join(__dirname, "../../../input/day04");
    const fileString = readFileSync(filePath, "utf8");
    expect(countPartialOverlaps(fileString)).toBe(928);
  });
});
