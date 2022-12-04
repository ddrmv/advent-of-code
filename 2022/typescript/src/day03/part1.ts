export const producePriorityHashMap = (): { [key: string]: number } => {
  let hashMap: { [key: string]: number } = {};

  for (let i = 0; i < 26; i++) {
    hashMap[`${String.fromCharCode(97 + i)}`] = i + 1;
    hashMap[`${String.fromCharCode(65 + i)}`] = i + 27;
  }

  return hashMap;
};

export const findPrioritySum = (input: string): number => {
  const priorityHashMap = producePriorityHashMap();
  return priorityHashMap["p"];
};
