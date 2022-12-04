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

  it("returns 18 for first group in example", () => {
    const input =
      "vJrwpWtwJgWrhcsFMMfFFhFp\n\
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n\
PmmdzqPrVvPwwTWBwg\n\
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n\
ttgJtRGJQctTZtZT\n\
CrZsJsPPZsGzwwsLwLmpwMDw\n";
    expect(findStickerPrioritySum(input)).toBe(70);
  });

  it("returns answer for puzzle", () => {
    const filePath = path.join(__dirname, "../../../input/day03");
    const fileString = readFileSync(filePath, "utf8");
    expect(findStickerPrioritySum(fileString)).toBe(2838);
  });
});
