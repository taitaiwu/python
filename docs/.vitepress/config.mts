import { defineConfig } from "vitepress";

export default defineConfig({
  lang: "zh-TW",
  title: "Python 程式存檔",
  description: "課堂習題與作業存檔",
  cleanUrls: true,

  themeConfig: {
    nav: [
      { text: "首頁", link: "/" },
      { text: "課程", link: "/its-python" },
    ],

    sidebar: [
      {
        text: "課程",
        items: [
          { text: "ITS-Python 證照班", link: "/its-python" },
          { text: "現代程式語言", link: "/modern-programming-language" },
          { text: "計算機演算法", link: "/computer-algorithms" },
          { text: "人工智慧導論", link: "/ai-intro" },
          { text: "機器學習", link: "/machine-learning" },
          { text: "網路安全", link: "/network-security" },
          { text: "社會網路分析與地理應用", link: "/social-network-analysis" },
        ],
      },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/taitaiwu/python" },
    ],

    search: {
      provider: "local",
    },

    outline: {
      label: "本頁大綱",
    },

    docFooter: {
      prev: "上一篇",
      next: "下一篇",
    },
  },
});
