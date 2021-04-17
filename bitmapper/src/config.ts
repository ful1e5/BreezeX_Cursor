import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const breeze = "#4D4D4D";
const white = "#FFFFFF";

const config: Config[] = [
  {
    themeName: "BreezeX Dark",
    color: {
      base: breeze,
      outline: white,
    },
  },
  {
    themeName: "BreezeX Light",
    color: {
      base: white,
      outline: breeze,
    },
  },
];

export { config };
