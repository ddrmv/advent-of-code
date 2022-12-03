export const findHeaviest = (input: string): number => {
  const elfBags = input.trim().split("\n\n");
  console.log(elfBags);
  const elfTotals: number[] = [];

  for (let i = 0; i < elfBags.length; i++) {
    let bag = elfBags[i].split("\n").map((calories) => Number(calories));
    elfTotals.push(sum(bag));
  }
  return Math.max(...elfTotals);
};

const sum = (numbers: number[]): number => {
  return numbers.reduce((sum, nextNumber) => sum + nextNumber);
};
