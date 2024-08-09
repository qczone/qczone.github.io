import {defineConfig} from "vitepress";
import sidebar from "./sidebar.json" assert { type: "json" };
const sidebarArr = sidebar;
// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "qczone",
  description: "qczone's blog",
  lang: "zh-CN",
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', href: 'https://github.githubassets.com/favicons/favicon.svg' }],
    [
      'script',
      { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-LN1CDPD1N4' }
    ],
    [
      'script',
      {},
      `window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-LN1CDPD1N4');`
    ]
  ],
  themeConfig: {
    search: {
      provider: "local",
    },
    docFooter: {
      prev: "上一页",
      next: "下一页",
    },
    outline: {
      label: "目录",
      level: "deep",
    },
    lastUpdated: {
      text: "最后更新于",
      formatOptions: {
        dateStyle: "short"
      },
    },
    langMenuLabel: "多语言",
    returnToTopLabel: "回到顶部",
    sidebarMenuLabel: "菜单",
    darkModeSwitchLabel: "主题",
    lightModeSwitchTitle: "切换到浅色模式",
    darkModeSwitchTitle: "切换到深色模式",
    // https://vitepress.dev/reference/default-theme-config
    nav: [{text: "列表", link: "/overview/overview"}],

    sidebar: sidebarArr,

    socialLinks: [
      { icon: "github", link: "https://github.com/qczone/qczone.github.io" },
    ],
  },
});
