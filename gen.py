import json
import os

# 常量定义
SIDEBAR_FILE = "docs/.vitepress/sidebar.json"
OVERVIEW_FILE = "docs/overview/overview.md"
DIR_MAP_FILE = "docs/.vitepress/dir-map.json"
EXCLUDE_DIRS = {".vitepress", "overview", ".DS_Store", "index.md"}

def load_dir_map(file_path):
    """加载目录映射文件"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_valid_dirs(base_path):
    """获取有效目录列表"""
    return [dir for dir in os.listdir(base_path) if dir not in EXCLUDE_DIRS]

def generate_overview_and_sidebar(dirs, dir_map):
    """生成 overview 和 sidebar 内容"""
    sidebar = [{"text": "概览", "link": "/overview/overview"}]
    heading = "# 概览\n"
    subheading = "## {}\n"
    link = "- [{}]({})\n"
    newline = "\n"
    overview = heading + newline

    for dir in dirs:
        dir_name = dir_map.get(dir, dir)  # 如果 dir_map 中没有映射，使用原目录名
        overview += subheading.format(dir_name) + newline
        items = []

        files = sorted(
            [file for file in os.listdir(f"docs/{dir}") if file.endswith(".md")],
            key=lambda file: os.path.getctime(os.path.join(f"docs/{dir}", file))
        )

        for file in files:
            filepath = f"docs/{dir}/{file}"
            with open(filepath, "r", encoding="utf-8") as f:
                title = f.readline().strip().split("# ")[1]  # 读取文件标题
                overview += link.format(title, f"../{dir}/{file}")
                items.append({"text": title, "link": f"{dir}/{file}"})

        overview += newline
        sidebar.append({"text": dir_name, "items": items})

    return overview, sidebar

def write_to_file(file_path, content):
    """将内容写入文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def save_sidebar(file_path, sidebar):
    """保存 sidebar 到 JSON 文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(sidebar, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    dir_map = load_dir_map(DIR_MAP_FILE)
    dirs = get_valid_dirs("docs")
    overview, sidebar = generate_overview_and_sidebar(dirs, dir_map)
    write_to_file(OVERVIEW_FILE, overview)
    save_sidebar(SIDEBAR_FILE, sidebar)
