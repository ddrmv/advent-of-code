import { readFileSync } from "fs";
import path from "path";
import { findStickerPrioritySum } from "./part2";

describe("findStickerPrioritySum", () => {
  it("returns 18 for first group in example", () => {
    const input =
      "vJrwpWtwJgWrhcsFMMfFFhFp\n\
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n\
PmmdzqPrVvPwwTWBwg\n";
    expect(findStickerPrioritySum(input)).toBe(18);
  });
});
