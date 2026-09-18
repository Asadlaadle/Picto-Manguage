# main.py - Interface for Picto language

import sys
from compiler import execute, E


def print_banner():
    print("=" * 40)
    print("  🍎 PICTO LANGUAGE 🍌")
    print("  A minimal emoji programming language")
    print("=" * 40)


def print_help():
    print("\nCommands:")
    print("  run <file>   - Run a .picto file")
    print("  repl         - Interactive mode")
    print("  help         - Show this help")
    print("  exit         - Quit")
    print("\nEmoji reference:")
    print("  🍎 = 5, 🍌 = 3, 🍇 = 10, 🍊 = 7, 🍓 = 2")
    print("  📢 print, ➕ add, ➖ sub, ✖️ mul, ➗ div")
    print("\nExample:")
    print("  🍎 = 5")
    print("  🍌 = 3")
    print("  📢 ➕ 🍎 🍌")
    print("  (output: 8)")


def repl():
    print("\nPicto REPL (type 'exit' to quit)")
    print("Type multiple lines. Press Enter twice to run.\n")
    
    while True:
        lines = []
        print("picto> ", end="")
        
        while True:
            try:
                line = input()
            except EOFError:
                return
            if line.lower() == "exit":
                return
            if line == "":
                break
            lines.append(line)
        
        if not lines:
            continue
        
        code = "\n".join(lines)
        try:
            results = execute(code)
            for r in results:
                print(f"  → {r}")
        except Exception as e:
            print(f"  Error: {e}")


def run_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
        results = execute(code)
        print(f"Output from {filename}:")
        for r in results:
            print(f"  → {r}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print_banner()
    
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "run":
        if len(sys.argv) < 3:
            print("Usage: python main.py run <file.picto>")
            return
        run_file(sys.argv[2])
    elif command == "repl":
        repl()
    elif command == "help":
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()