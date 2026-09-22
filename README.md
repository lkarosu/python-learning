# 文件整理工具

一个基于 Python 标准库的命令行工具：扫描指定目录中的直接文件，并按文件扩展名生成整理预览或执行移动。工具会生成 JSON 报告和运行日志，便于检查本次处理结果。

## 功能

- 按扩展名分类文件；扩展名会转为小写。
- 无扩展名文件归入 `no_extension` 目录。
- 默认仅预览，不移动任何文件。
- 传入 `--apply` 后才创建分类目录并实际移动文件。
- 目标路径已存在同名文件时跳过，不覆盖原文件。
- 若分类目录名已被普通文件占用，保留所有相关文件，不创建或覆盖该分类目录，并在报告中记录错误。
- 在目标目录生成 `organizer_report.json`，记录逐文件结果和数量汇总。
- 在当前运行目录生成 `organizer.log`，记录扫描、预览、移动和跳过事件。

## 运行环境

- Python 3.10 或更高版本
- 无第三方依赖

可选：创建并激活虚拟环境。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 使用方法

在项目根目录运行。将 `demo_files` 替换为你要处理的目录路径。

### 预览模式

```powershell
python file_organizer.py demo_files
```

示例输出：

```text
以下是整理预览；目前不会移动任何文件：
notes.txt -> txt/notes.txt
photo.jpg -> jpg/photo.jpg
README -> no_extension/README
```

预览模式不会移动文件或创建分类目录，但会在目标目录写入 `organizer_report.json`。

### 执行模式

确认预览无误后，显式传入 `--apply`：

```powershell
python file_organizer.py demo_files --apply
```

例如，`demo_files/report.pdf` 会被移动到 `demo_files/pdf/report.pdf`。

## 分类与安全规则

- 仅扫描指定目录的直接文件，不递归扫描子目录。
- `archive.2026.zip` 归入 `zip`；只使用最后一个扩展名。
- `README` 归入 `no_extension`。
- 如果 `txt/notes.txt` 已存在，根目录的 `notes.txt` 会被标记为 `skipped`，不会覆盖或重命名任一文件。
- 如果根目录已有普通文件 `txt`，而 `notes.txt` 需要归入 `txt/`，则不会将 `txt` 覆盖或替换为目录：`txt` 会标记为 `skipped`，`notes.txt` 会标记为 `error`，两个文件均保留不变。该规则在预览和执行模式下都生效。
- 请先在演示目录中预览，确认结果后再使用 `--apply`；不要直接对重要目录执行移动。

## 报告与日志

`organizer_report.json` 写在被处理目录中，结构如下：

```json
{
  "mode": "apply",
  "summary": {
    "preview": 0,
    "moved": 1,
    "skipped": 0,
    "error": 0
  },
  "results": [
    {
      "source": "report.pdf",
      "target": "pdf/report.pdf",
      "status": "moved"
    }
  ]
}
```

状态说明：

- `preview`：仅展示计划，不移动文件。
- `moved`：已成功移动文件。
- `skipped`：目标位置已有同名文件，已安全跳过。
- `error`：无法完成整理，例如所需分类目录名已被普通文件占用；不会改动相关文件。

`organizer.log` 记录运行过程。日志与报告均在 `.gitignore` 中忽略，不会被提交到仓库。

## 测试

当前共有 9 项自动化测试。
使用标准库 `unittest` 运行全部测试：

```powershell
python -m unittest -v
```

当前测试覆盖：

- 有扩展名、多扩展名和无扩展名的分类。
- 预览不会移动文件。
- 实际移动文件与报告汇总。
- 重名文件不覆盖，并在报告中记录跳过状态。
- 分类目录名被普通文件占用时保留文件，并记录 `error` 状态。
- 预览报告的内容与数量汇总。

## 项目结构

```text
.
├── file_organizer.py       # 命令行工具
├── test_file_organizer.py  # 自动化测试
├── README.md
└── .gitignore
```
