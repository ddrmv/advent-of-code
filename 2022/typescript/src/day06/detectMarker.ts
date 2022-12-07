const isMarker = (sequence: string) => {
  return new Set(sequence).size === 4;
};

export const detectMarker = (input: string): number => {
  for (let i = 0; i <= input.length - 4; i++) {
    if (isMarker(input.slice(i, i + 4))) {
      return i + 4;
    }
  }
  throw new Error("No marker in signal");
};
