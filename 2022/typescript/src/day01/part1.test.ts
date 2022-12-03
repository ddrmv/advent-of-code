import { findHeaviest } from "./part1";

describe("findHeaviest", () => {
  it("returns total for one elf", () => {
    expect(findHeaviest("1\n2\n3\n")).toBe(6);
  });
});
