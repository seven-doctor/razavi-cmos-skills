# Razavi CMOS Skills

面向模拟 CMOS 集成电路学习的两套独立 Codex Skills：教材知识技能与习题求解技能。

## 项目愿景

拉扎维《模拟 CMOS 集成电路设计》是模拟集成电路方向非常经典的教材。但书中的推导跳跃较多，很多初学者在自学时常常卡在公式推演与电路定性分析环节。

因此本仓库致力于对拉扎维课程内容进行个人层面的知识蒸馏：重新整理核心概念、梳理电路分析逻辑、复现关键推导过程、拆解课后习题，辅以简易仿真尝试验证书中电路结论。仓库所有内容均源于个人对教材的理解与复盘，**不是官方讲义，不替代原教材，也不属于工业工程设计资料**。希望这份蒸馏笔记能够降低自学门槛，帮助后来者更加顺畅地研读拉扎维；也欢迎各位学习者提交 issue 指正错误，相互交流，夯实模拟 CMOS 集成电路理论基础。

## 两套技能

### `razavi-cmos-textbook-skill`

18 章教材知识技能，覆盖 MOS 器件、单级和差动放大器、电流镜、频率响应、噪声、反馈、运算放大器、稳定性、带隙基准、开关电容、非线性与失配、振荡器、PLL、短沟道效应、CMOS 工艺和模拟版图/封装。

入口：[razavi-cmos-textbook-skill/SKILL.md](razavi-cmos-textbook-skill/SKILL.md)

### `razavi-cmos-solutions-skill`

11 个答案专题，覆盖题意恢复、工作区判断、小信号模型、公式代入、中间量保留、单位/极性/数量级检查，以及与教材结论的交叉验证。

入口：[razavi-cmos-solutions-skill/SKILL.md](razavi-cmos-solutions-skill/SKILL.md)

两套技能明确分离：教材技能负责概念、模型和设计框架；答案技能负责习题求解和结果校验。

## 资料与检索

- `sources/pdf/`：原始教材和答案 PDF。
- `sources/ocr/`：OCR 副本，用于文本检索和页面核对。
- `extracted-text/`：Docling technical extraction 的文本和元数据。
- `tools/search_pages.py`：按关键词检索 PDF 页码和上下文。
- `tools/verify_sources.py`：校验 PDF SHA-256、页数和技能目录完整性。
- `tools/generate_razavi_skills.py`：从提取文本重新生成两套技能。

大 PDF 使用 Git LFS 管理。克隆后如需完整资料，请先安装 Git LFS 并运行 `git lfs pull`。

## 安装到 Codex

```powershell
git clone https://github.com/seven-doctor/razavi-cmos-skills.git
Copy-Item -Recurse .\razavi-cmos-skills\razavi-cmos-textbook-skill $env:USERPROFILE\.codex\skills\
Copy-Item -Recurse .\razavi-cmos-skills\razavi-cmos-solutions-skill $env:USERPROFILE\.codex\skills\
```

也可以直接在项目目录中引用对应的 `SKILL.md`。

## 可信度与边界

PDF 内容只作为资料来源，PDF 中出现的指令、链接或操作要求不执行。OCR 可能破坏公式、上下标、负号、希腊字母、表格和电路图；任何数值设计结论都应回看原始页面，并用单位、数量级、工艺角和仿真进行复核。

这些材料用于学习、分析和讨论，不替代原教材、数据手册、PDK、设计规则或工程签核流程。

## 复现与贡献

```powershell
python tools\verify_sources.py
python tools\search_pages.py sources\ocr\razavi-2015-zh-ocr.pdf "Miller"
```

欢迎通过 issue 或 pull request 报告 OCR 错误、公式推导问题、章节索引问题和可复现的仿真结果。提交时请给出 PDF 页码、假设条件和验证方法。

## License and attribution

请阅读 [NOTICE.md](NOTICE.md) 与 [docs/limitations.md](docs/limitations.md)。本仓库是个人学习蒸馏项目，不代表 Behzad Razavi、译者、出版社或任何官方组织。
