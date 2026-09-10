import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import { VPButton } from "vitepress/theme";
import "./custom.css";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("VPButton", VPButton);
  },
} satisfies Theme;
