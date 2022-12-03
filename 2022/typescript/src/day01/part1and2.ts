const findElfTotals = (input: string): number[] => {
  const elfBags = input.trim().split("\n\n");
  const elfTotals: number[] = [];

  for (let i = 0; i < elfBags.length; i++) {
    let bag = elfBags[i].split("\n").map((calories) => Number(calories));
    elfTotals.push(sum(bag));
  }

  return elfTotals;
};

export const findHeaviest = (input: string): number => {
  return Math.max(...findElfTotals(input));
};

export const findThreeHeaviest = (input: string): number => {
  const elfTotals = findElfTotals(input).sort((a, b) => b - a);
  return sum(elfTotals.slice(0, 3));
};

const sum = (numbers: number[]): number => {
  return numbers.reduce((sum, nextNumber) => sum + nextNumber);
};
