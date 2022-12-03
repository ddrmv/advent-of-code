import { readFileSync } from "fs";
import { findHeaviest } from "./part1";
import path from "path";

describe("findHeaviest", () => {
  it("returns total for one elf", () => {
    expect(findHeaviest("1\n2\n3\n")).toBe(6);
  });

  it("returns bigger total out of two elves", () => {
    expect(findHeaviest("1\n2\n\n5\n6\n")).toBe(11);
  });

  it("returns bigger total out of two elves", () => {
    const filePath = path.join(__dirname, "../../../input/day01");
    const fileString = readFileSync(filePath, "utf8");
    expect(findHeaviest(fileString)).toBe(75622);
  });
});
