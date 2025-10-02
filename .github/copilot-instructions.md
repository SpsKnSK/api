# GitHub Copilot Instructions

This repository contains a **multilingual Python programming curriculum** for 2nd-grade students at SK API (Slovak/Hungarian educational context). The codebase is structured as a comprehensive learning platform with lessons, exercises, and supplementary materials.

## Repository Structure & Conventions

### Multilingual Content Organization
- **Lessons_hu/**: Hungarian lessons (primary language)
- **Lessons_sk/**: Slovak lessons (mirror structure)
- **Exercises/**: Practice problems organized by topic (`05_if/`, `06_for/`, etc.)
- Each lesson follows consistent numbering: `00_VsCode`, `01_Algorithms`, `02_Terminal_print`, etc.

### File Naming Patterns
- Lessons: `{number}_{topic}_{lang}.md` (e.g., `02_Terminal_print_hu.md`)
- Exercises: `e{number}_{description}.md` (e.g., `e01_car.md`, `e02_textType.md`)
- Python examples: `{number}_{concept}.py` (e.g., `01_break.py`, `02_continue.py`)

### Content Structure Standards
- **Bilingual exercises**: Each exercise file contains both Slovak and Hungarian versions
- **Code examples**: Use simple, educational Python with clear variable names
- **Progressive difficulty**: Topics build from basic (`print`, `input`) to advanced (`classes`, `inheritance`)

## Development Workflows

### When Adding New Content
1. **Lessons**: Create both `_hu.md` and `_sk.md` versions maintaining parallel structure
2. **Exercises**: Include both Slovak ("Úloha") and Hungarian ("Feladat") sections in single files
3. **Python examples**: Keep code simple, well-commented, following beginner-friendly patterns

### Educational Code Style
- Use descriptive variable names in context language (`cislo1`, `szam1` for numbers)
- Prefer explicit over implicit (avoid advanced Python features)
- Include multiple solution approaches when pedagogically valuable
- Format: Use VS Code's auto-format (`CTRL+SHIFT+F`) as referenced in `UsefulStuff/00_Cheat_sheet.md`

## Key Components

### Extra/ Directory
Contains advanced projects beyond core curriculum:
- **WebWithFlask/**: Flask web applications
- **SQLiteDB_basics/**, **SqLiteDbHandling_python/**, **SqLiteDbHandling_withSqlAlchemy/**: Database examples
- **UnitTesting/**: Testing examples
- **DataFiles/**: File processing examples

### UsefulStuff/ Directory  
Reference materials and cheat sheets:
- `00_Cheat_sheet.md`: VS Code shortcuts and formatting
- `00_LogicalOperators.md`: Python operators reference
- Topic-specific quick references

## Integration Points

- **VS Code Integration**: Curriculum assumes VS Code as primary IDE
- **Educational Context**: Content designed for classroom use with Discord community support
- **Assessment System**: Exercises support EduPage integration for homework submission
- **Multi-format Support**: Lessons support both individual and group learning approaches

## Project-Specific Patterns

When contributing educational content, maintain the **parallel language structure** and ensure examples are **classroom-appropriate** with **step-by-step progression**. Reference existing exercises in `Exercises/05_if/` for formatting and complexity standards.