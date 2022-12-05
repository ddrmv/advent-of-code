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
  if (isFullOverlap(...rowToRanges(input.trimEnd()))) {
    fullOverlaps++;
  }

  return fullOverlaps;
};
