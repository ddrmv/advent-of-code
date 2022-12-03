export const findHeaviest = (input: string): number => {
  const numbers = input.split("\n").map((numberString) => Number(numberString));
  console.log(numbers);
  return numbers.reduce((sum, nextNumber) => sum + nextNumber);
};
