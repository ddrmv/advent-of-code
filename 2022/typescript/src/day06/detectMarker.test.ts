import { readFileSync } from "fs";
import path from "path";
import { detectMarker } from "./detectMarker";

describe("detectMarker", () => {
  it("retuns 4 when signal is at start", () => {
    expect(detectMarker("abcd")).toBe(4);
  });

  it("retuns 5 for exmaple bvwbjplbgvbhsrlpgdmjqwftvncz", () => {
    expect(detectMarker("bvwbjplbgvbhsrlpgdmjqwftvncz")).toBe(5);
  });

  it("retuns 5 for exmaple nppdvjthqldpwncqszvftbrmjlhg", () => {
    expect(detectMarker("nppdvjthqldpwncqszvftbrmjlhg")).toBe(6);
  });

  it("retuns 5 for exmaple nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", () => {
    expect(detectMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")).toBe(10);
  });

  it("retuns 5 for exmaple zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", () => {
    expect(detectMarker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")).toBe(11);
  });

  it("returns answer for puzzle part 1", () => {
    const filePath = path.join(__dirname, "../../../input/day06");
    const fileString = readFileSync(filePath, "utf8");
    expect(detectMarker(fileString)).toBe(1235);
  });
});
