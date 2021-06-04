import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const breezeColor = "#4D4D4D";
const whiteColor = "#FFFFFF";

const config: Config[] = [
  {
    themeName: "BreezeX-Dark",
    color: {
      base: breezeColor,
      outline: whiteColor,
    },
  },
  {
    themeName: "BreezeX-Light",
    color: {
      base: whiteColor,
      outline: breezeColor,
    },
  },
];

export { config };
