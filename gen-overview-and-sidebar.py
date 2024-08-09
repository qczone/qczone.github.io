sidebar = [
    {
        "text": "概览",
        "link": "/overview/overview",
    }
]
heading = "# 概览\n"
subheading = "## {}\n"
link = "- [{}]({})\n"
newline = "\n"
import json
import os
dir_map = json.load(open("docs/.vitepress/dir-map.json", "r", encoding="utf-8"))
overview = heading + newline
dirs = [x for x in os.listdir("docs") if x != ".vitepress" and x != "overview" and x != ".DS_Store" and x != "index.md"]
for dir in dirs:
    dir_name = dir_map[dir]
    if dir == None:
        dir_name = dir
    overview += subheading.format(dir_name) + newline
    items= []
    files = sorted(
        [x for x in os.listdir("docs/" + dir) if x.endswith(".md")],
        key=lambda x: os.path.getctime(os.path.join("docs/" + dir, x))
    )
    for file in files:
        filepath = "docs/" + dir + "/" + file
        with open(filepath, "r", encoding="utf-8") as f:
            line = f.readline().split("\n")[0]
            title = line.split("# ")[1]
            overview += link.format(title, "../" + dir + "/" + file)
            items.append({
                "text": title,
                "link": dir + "/" + file
            })
    overview += newline
    sidebar.append({
        "text": dir_name,
        "items": items
    })
with open("docs/overview/overview.md", "w", encoding="utf-8") as f:
    f.write(overview)
with open("docs/.vitepress/sidebar.json", "w", encoding="utf-8") as f:
    json.dump(sidebar, f, ensure_ascii=False, indent=4)