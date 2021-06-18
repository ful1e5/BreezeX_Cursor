import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const breeze = "#4D4D4D";
const white = "#FFFFFF";
const black = "#000000";

const config: Config[] = [
  {
    themeName: "BreezeX-Dark",
    color: {
      base: breeze,
      outline: white,
    },
  },
  {
    themeName: "BreezeX-Light",
    color: {
      base: white,
      outline: breeze,
    },
  },

  {
    themeName: "BreezeX-Black",
    color: {
      base: black,
      outline: white,
    },
  },
];

export { config };
