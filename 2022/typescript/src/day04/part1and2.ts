interface Range {
  min: number;
  max: number;
}

const isFullOverlap = (RangeA: Range, RangeB: Range): boolean => {
  return (
    (RangeA.min >= RangeB.min && RangeA.max <= RangeB.max) ||
    (RangeB.min >= RangeA.min && RangeB.max <= RangeA.max)
  );
};

const isPartialOverlap = (RangeA: Range, RangeB: Range): boolean => {
  return (
    (RangeA.min >= RangeB.min && RangeA.min <= RangeB.max) ||
    (RangeA.max >= RangeB.min && RangeA.max <= RangeB.max) ||
    (RangeB.min >= RangeA.min && RangeB.min <= RangeA.max) ||
    (RangeB.max >= RangeA.min && RangeB.max <= RangeA.max)
  );
};

const rangeStringToArray = (range: string): Range => {
  const minMax = range.split("-");
  const min = Number(minMax[0]);
  const max = Number(minMax[1]);
  return { min, max };
};

const rowToRanges = (input: string): [Range, Range] => {
  const elfRanges = input.trimEnd().split(",");
  const rangeOne = rangeStringToArray(elfRanges[0]);
  const rangeTwo = rangeStringToArray(elfRanges[1]);

  return [rangeOne, rangeTwo];
};

export const countFullOverlaps = (input: string): number => {
  let fullOverlaps = 0;
  const elfPairStrings = input.trimEnd().split("\n");

  for (let pairString of elfPairStrings) {
    if (isFullOverlap(...rowToRanges(pairString))) {
      fullOverlaps++;
    }
  }

  return fullOverlaps;
};

export const countPartialOverlaps = (input: string): number => {
  let partialOverlaps = 0;
  const elfPairStrings = input.trimEnd().split("\n");

  for (let pairString of elfPairStrings) {
    if (isPartialOverlap(...rowToRanges(pairString))) {
      partialOverlaps++;
    }
  }

  return partialOverlaps;
};
