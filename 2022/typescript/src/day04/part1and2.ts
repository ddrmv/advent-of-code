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

const isInRange = (number: number, range: Range): boolean => {
  return number >= range.min && number <= range.max;
};

const isPartialOverlap = (RangeA: Range, RangeB: Range): boolean => {
  return (
    isInRange(RangeA.min, RangeB) ||
    isInRange(RangeA.max, RangeB) ||
    isInRange(RangeB.min, RangeA) ||
    isInRange(RangeB.max, RangeA)
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
  return countOverlaps(input, isFullOverlap);
};

export const countPartialOverlaps = (input: string): number => {
  return countOverlaps(input, isPartialOverlap);
};

const countOverlaps = (
  input: string,
  comparatorFunction: (RangeA: Range, RangeB: Range) => boolean
) => {
  let overlaps = 0;
  const elfPairStrings = input.trimEnd().split("\n");

  for (let pairString of elfPairStrings) {
    if (comparatorFunction(...rowToRanges(pairString))) {
      overlaps++;
    }
  }

  return overlaps;
};
