import re


def analyze_code(code):
    lines = code.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    blank_lines = [
    line for line in lines
    if not line.strip()
    ]

    average_line_length = (
    sum(len(line) for line in non_empty_lines)
    / len(non_empty_lines)
    if non_empty_lines else 0
    )
    function_count = len(
    re.findall(
        r'\bdef\s+\w+|\bfunction\s+\w+|\b(public|private|protected)?\s*(static\s+)?\w+\s+\w+\s*\(',
        code
    )
    )
    loop_count = len(
    re.findall(
        r'\bfor\b|\bwhile\b',
        code
    )
    )

    conditional_count = len(
    re.findall(
        r'\bif\b|\belse\b|\belif\b|\bswitch\b|\bcase\b',
        code
    )
    )

    import_count = len(
    re.findall(
        r'\bimport\b|\bfrom\b|\binclude\b|\brequire\b',
        code
    )
    )

    comment_lines = [
    line for line in non_empty_lines
    if line.strip().startswith("#")
    or line.strip().startswith("//")
    ]

    class_count = len(
    re.findall(
        r'\bclass\s+\w+',
        code
    )
)

    exception_count = len(
    re.findall(
        r'\btry\b|\bexcept\b|\bcatch\b|\bfinally\b|\bthrow\b',
        code
    )
)
    token_count = len(
    re.findall(r'\b\w+\b', code)
)
    unique_tokens = len(
    set(re.findall(r'\b\w+\b', code))
)
    
    return {
        "total_characters": len(code),
        "total_lines": len(lines),
        "non_empty_lines": len(non_empty_lines),
        "comment_lines": len(comment_lines),
        "comment_ratio": round(
        len(comment_lines) / len(non_empty_lines) * 100, 2
        ) if non_empty_lines else 0,
        "blank_lines": len(blank_lines),
        "average_line_length": round(average_line_length, 2),
        "function_count": function_count,
        "loop_count": loop_count,
        "conditional_count": conditional_count,
        "import_count": import_count,
        "class_count": class_count,
        "exception_count": exception_count,
        "token_count": token_count,
        "unique_tokens": unique_tokens
        }

