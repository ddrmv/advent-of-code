const isMarker = (sequence: string, markerLength = 4) => {
  return new Set(sequence).size === markerLength;
};

export const detectMarker = (input: string, size = 4): number => {
  for (let i = 0; i <= input.length - size; i++) {
    if (isMarker(input.slice(i, i + size), size)) {
      return i + size;
    }
  }
  throw new Error("No marker in signal");
};
