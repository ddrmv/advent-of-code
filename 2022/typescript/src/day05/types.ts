export interface Move {
  amount: number;
  from: number;
  to: number;
}

export interface Stack {
  crates: string[];
}

export interface Supplies {
  stacks: Stack[];
}
