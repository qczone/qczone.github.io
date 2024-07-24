import {defineConfig} from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "博客",
  description: "记录点滴，分享知识",
  lang: "zh-CN",
  lastUpdated: true,
  head: [
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

    sidebar: [
      {
        text: "概览",
        link: "/overview/overview",
      },
      {
        text: "Mac",
        items: [
          {
            text: "Mac 自定义 Edge 在菜单栏中的名称",
            link: "/mac/mac-customizing-edge-name-in-the-menu-bar",
          },
        ],
      },
      {
        text: "问题排查",
        items: [
          {
            text: "一次解决 JVM 线程数量过高问题的经历",
            link: "/problem-screening/an-experience-of-solving-the-problem-of-high-number-of-jvm-threads",
          },
        ],
      },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/qczone/qczone.github.io" },
    ],
  },
});
