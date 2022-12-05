import { countFullOverlaps } from "./part1";

describe("countFullOverlaps", () => {
  it("returns 1 for a one-line input of full overlap", () => {
    expect(countFullOverlaps("2-8,3-7\n")).toBe(1);
    expect(countFullOverlaps("6-6,4-6\n")).toBe(1);
    expect(countFullOverlaps("2-6,4-8\n")).toBe(0);
  });
});
