import { parseInput } from "./parseInput";

describe("findStacksTops", () => {
  it("returns the top of a single stack", () => {
    const input =
      "    [D]\n\
[N] [C]\n\
[Z] [M]\n\
 1   2 \n\
\n\
move 1 from 2 to 1\n\
move 1 from 2 to 1\n";

    expect(parseInput(input)).toEqual([
      {
        stacks: [{ crates: ["Z", "N"] }, { crates: ["M", "C", "D"] }],
      },
      [
        { amount: 1, from: 1, to: 0 },
        { amount: 1, from: 1, to: 0 },
      ],
    ]);
  });
});
