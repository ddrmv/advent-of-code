import { producePriorityHashMap } from "./part1";

const intersect = (set1: Set<string>, set2: Set<string>): Set<string> => {
  const intersection = new Set<string>();
  for (const element of set1) {
    if (set2.has(element)) {
      intersection.add(element);
    }
  }
  return intersection;
};

const findSticker = (bag1: string, bag2: string, bag3: string): string => {
  const items1 = new Set(bag1);
  const items2 = new Set(bag2);
  const items3 = new Set(bag3);
  const intersection = intersect(intersect(items1, items2), items3);
  let sticker = intersection.values().next().value;
  return sticker;
};

export const findStickerPrioritySum = (input: string) => {
  const priorityMap = producePriorityHashMap();

  const bags = input.trimEnd().split("\n");

  let prioritySum = 0;
  let sticker: string;

  for (let i = 0; i < bags.length - 2; i += 3) {
    sticker = findSticker(bags[i], bags[i + 1], bags[i + 2]);
    prioritySum += priorityMap[sticker];
  }
  return prioritySum;
};
