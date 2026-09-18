# compiler.py - Core compiler for Picto language

# ============ UNICODE MAP ============
E = {
    "apple": "\U0001F34E",
    "banana": "\U0001F34C",
    "grapes": "\U0001F347",
    "orange": "\U0001F34A",
    "strawberry": "\U0001F353",
    "print": "\U0001F4E2",
    "add": "\u2795",
    "sub": "\u2796",
    "mul": "\u2716",
    "div": "\u2797",
}

R = {v: k for k, v in E.items()}


# ============ LEXER ============
def lexer(code):
    tokens = []
    for line in code.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = []
        for ch in line:
            if ch in R:
                parts.append(R[ch])
            elif ch == "=":
                parts.append("=")
            elif ch.isdigit():
                parts.append(ch)
        tokens.append(parts)
    return tokens


# ============ PARSER ============
def parser(tokens):
    ast = []
    for parts in tokens:
        if parts[0] == "print":
            ast.append(("print", parts[1:]))
        elif "=" in parts:
            var = parts[0]
            value = int(parts[2])
            ast.append(("assign", var, value))
    return ast


# ============ INTERPRETER ============
def execute(code):
    vars = {}
    tokens = lexer(code)
    ast = parser(tokens)
    output = []
    
    for node in ast:
        if node[0] == "assign":
            vars[node[1]] = node[2]
        elif node[0] == "print":
            expr = node[1]
            if len(expr) == 1:
                output.append(vars.get(expr[0], 0))
            else:
                op = expr[0]
                left = vars.get(expr[1], 0)
                right = vars.get(expr[2], 0)
                if op == "add": result = left + right
                elif op == "sub": result = left - right
                elif op == "mul": result = left * right
                elif op == "div": result = left // right
                else: result = 0
                output.append(result)
    
    return output