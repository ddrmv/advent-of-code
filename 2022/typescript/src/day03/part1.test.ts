import { findPrioritySum, producePriorityHashMap } from "./part1";

describe("producePriorityHash", () => {
  it("returns 42 for vJrwpWtwJgWrhcsFMMfFFhFp", () => {
    const hashMap = producePriorityHashMap();
    expect(hashMap.p).toBe(16);
  });
});

describe("findPrioritySum", () => {
  it("returns 16 for vJrwpWtwJgWrhcsFMMfFFhFp", () => {
    expect(findPrioritySum("vJrwpWtwJgWrhcsFMMfFFhFp\n")).toBe(16);
  });

  it("returns 38 for jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", () => {
    expect(findPrioritySum("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n")).toBe(38);
  });

  it("returns 157 for provided example", () => {
    const input =
      "vJrwpWtwJgWrhcsFMMfFFhFp\n\
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n\
PmmdzqPrVvPwwTWBwg\n\
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n\
ttgJtRGJQctTZtZT\n\
CrZsJsPPZsGzwwsLwLmpwMDw\n";
    expect(findPrioritySum(input)).toBe(157);
  });
});
