export const producePriorityHashMap = (): { [key: string]: number } => {
  let hashMap: { [key: string]: number } = {};

  for (let i = 0; i < 26; i++) {
    hashMap[`${String.fromCharCode(97 + i)}`] = i + 1;
    hashMap[`${String.fromCharCode(65 + i)}`] = i + 27;
  }

  return hashMap;
};

export const findWrongItem = (rucksack: string) => {
  let halfLength = rucksack.length / 2;
  let firstHalfUnique = new Set(rucksack.slice(0, halfLength));
  const secondHalf = rucksack.slice(halfLength);
  for (let item of secondHalf) {
    if (firstHalfUnique.has(item)) {
      return item;
    }
  }
  throw new Error("Assertion: an item should repeat in first half of bag");
};

export const findPrioritySum = (input: string): number => {
  const priorityHashMap = producePriorityHashMap();
  const rucksacks = input.trim().split("\n");

  let totalPriority = 0;
  let wrongItem: string;

  for (let rucksack of rucksacks) {
    wrongItem = findWrongItem(rucksack);
    totalPriority += priorityHashMap[wrongItem];
  }
  return totalPriority;
};
