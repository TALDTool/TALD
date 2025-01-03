import re
import os
from colorama import Fore, Style, init
from TALDCommands import SUSPICIOUS_PATTERNS
init()

# Logo TALD
def display_logo():
    logo = f"""
{Fore.LIGHTGREEN_EX}
            ╔══════════════════════════════════════╗
            ║ ████████  █████  ██     ██████       ║
            ║    ██    ██   ██ ██     ██   ██      ║
            ║    ██    ███████ ██     ██   ██      ║
            ║    ██    ██   ██ ██     ██   ██      ║
            ║    ██    ██   ██ ██████ ██████  v1.0 ║
            ╚══════════════════════════════════════╝
                   -- {Fore.GREEN}Script Analysis Tool{Fore.LIGHTGREEN_EX} --
{Fore.LIGHTCYAN_EX}  
                   By {Fore.LIGHTBLUE_EX}Mohamed Rayan Ettaldi
{Fore.LIGHTCYAN_EX} [!] Visit {Fore.LIGHTGREEN_EX}https://github.com/ettaldi/TALDTool{Fore.LIGHTCYAN_EX} to update the tool
    """
    print(logo)

# Analyze a file
def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    results = []
    for i, line in enumerate(lines, start=1):
        for category, patterns in SUSPICIOUS_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, line):
                    results.append((i, line.strip(), category, pattern))
    return results

# Display the results
def display_results(file_path, results):
    if results:
        print(f"{Fore.RED}\n[!] Risks detected in the file: {file_path}{Style.RESET_ALL}")
        print("-" * 80)
        for line_no, line, category, pattern in results:
            print(f"{Fore.YELLOW}  - Line {line_no}: {line}{Style.RESET_ALL}")
            print(f"    → Category: {Fore.CYAN}{category}{Style.RESET_ALL}")
            print(f"    → Suspicious Pattern: {Fore.MAGENTA}{pattern}{Style.RESET_ALL}")
        print("-" * 80)

# Main function
def main():
    display_logo()

    while True:
        print(f"{Fore.LIGHTCYAN_EX}          1. Analyze a directory                2. Analyze a specific file") 
        print(f"{Fore.LIGHTCYAN_EX}          3. Exit")
        print()
        choice = input(f"{Fore.CYAN}Choose an option: {Style.RESET_ALL}")

        if choice == '1':
            directory = input(f"{Fore.LIGHTCYAN_EX}Enter the directory path to analyze: {Style.RESET_ALL}")
            if not os.path.isdir(directory):
                print(f"{Fore.RED}[!] The specified path is not a valid directory: {directory}{Style.RESET_ALL}")
                continue

            print(f"{Fore.LIGHTCYAN_EX}Scanning directory: {directory}{Style.RESET_ALL}")
            all_results = []
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.endswith(('.sh', '.py', '.bat', '.ps1')):
                        print(f"{Fore.GREEN}\n[+] Analyzing file: {file_path}{Style.RESET_ALL}")
                        results = analyze_file(file_path)
                        all_results.extend(results)
            if all_results:
                display_results(directory, all_results)
            else:
                print(f"{Fore.RED}[!] No suspicious patterns found in the directory.{Style.RESET_ALL}")

        elif choice == '2':
            file_path = input(f"{Fore.LIGHTCYAN_EX}Enter the file path to analyze: {Style.RESET_ALL}")
            if not os.path.isfile(file_path):
                print(f"{Fore.RED}[!] The specified path is not a valid file: {file_path}{Style.RESET_ALL}")
                continue
            results = analyze_file(file_path)
            display_results(file_path, results)
            if not results:
                print(f"{Fore.RED}[!] No suspicious patterns found in the file.{Style.RESET_ALL}")

        elif choice == '3':
            print(f"{Fore.GREEN}Exiting the tool. {Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}[!] Please choose a valid option.{Style.RESET_ALL}")

# Run the program
if __name__ == "__main__":
    main()
