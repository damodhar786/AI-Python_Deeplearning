# Copilot Instructions - Logic Building 101 DAY07

## Project Overview
This is a pattern generation logic exercise demonstrating how to create ASCII art patterns using nested loops. The project provides parallel implementations in Python and JavaScript to teach fundamental programming concepts across languages.

## Key Patterns & Architecture

### Pattern Types
Three core pattern types are implemented across both languages:
1. **Inverted Right-Angled Triangle**: Decreases stars row-by-row (uses `range(rows, 0, -1)` in Python)
2. **Triangle (Pyramid)**: Centered pyramid with leading spaces and increasing stars
3. **Inverted Triangle**: Centered pyramid inverted

### Implementation Approach
- **Python** ([Solution.py](Solution.py)): Uses direct loop iteration with `print(..., end=" ")` for spacing control
  - Example: `for i in range(rows, 0, -1):` for decreasing iterations
  - Spacing: `print(" ", end=" ")` for padding
- **JavaScript** ([Solutions.js](Solutions.js)): Builds row strings then outputs them
  - Uses `rowPattern` accumulation pattern
  - Uses `.trim()` to clean trailing spaces before console output

## Developer Workflow

### Running Solutions
- **Python**: `python Solution.py` - prompts for number of rows via `input()`
- **JavaScript**: `node Solutions.js` - hardcoded test calls (e.g., `Pattern1(5)`)

### Expected Behavior
- Patterns require integer input (number of rows)
- Output uses `*` for pattern characters
- JavaScript uses `.` as placeholder for spaces in visual demos

## Code Conventions

| Aspect | Convention | Example |
|--------|-----------|---------|
| **Loop Structure** | Nested loops for rows & columns | Pattern 1: outer loop rows, inner loop stars |
| **Spacing** | Space after each character (star or space) | `print("*", end=" ")` (Python) or `"* "` concatenation |
| **Borders** | Use `"-" * 65` to separate pattern blocks | Clear visual separation between solutions |
| **Comments** | `#` in Python, `//` in JavaScript; mark pattern sections clearly | `## Pattern 1:` followed by expected output |
| **Output Cleanup** | JavaScript uses `.trim()` to remove trailing spaces | `console.log(rowPattern.trim())` |

## When Adding New Patterns

1. Document pattern in [Questions.md](Questions.md) with ASCII visualization
2. Implement in [Solution.py](Solution.py) with nested loops, add separator line
3. Implement in [Solutions.js](Solutions.js) with string accumulation approach
4. Test with sample input (e.g., `5` rows) to verify alignment and spacing
5. Ensure both implementations produce identical visual output

## Integration Points
- **No external dependencies** - uses only standard `print()` (Python) and `console.log()` (JavaScript)
- **No data persistence** - all solutions are stateless, input-driven demonstrations
- **Educational focus** - patterns teach: loop nesting, string manipulation, condition logic
