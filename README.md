# MyGit CLI

A simple Git CLI that helps users create well-formatted commit messages with ease. This tool simplifies the process of making meaningful commits by allowing users to choose commit types and add detailed commit messages.

## Technologies

- Python3
- VSCode (or any other code editor)

## How to Install

To install and use the **MyGit CLI**, follow these steps:

### 1. Clone the Repository (if applicable)

If you're getting this tool from a Git repository:

```bash
git clone https://github.com/guiandradedev/mygit-cli.git
cd mygit-cli
```

### 2. Install Dependencies

Install the required Python libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Install Globally (Optional)

If you want to use the `mgt` command globally, move the Python script to a directory in your PATH:

```bash
mv mgt.py ~/.local/bin/mgt
chmod +x ~/.local/bin/mgt
```

Add `~/.local/bin` to your PATH if it's not already included. You can do this by adding the following line to your `~/.bashrc` or `~/.zshrc` file:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then, source your shell configuration:

```bash
source ~/.bashrc   # or source ~/.zshrc
```

## How to Use

Once installed, you can use the **MyGit CLI** to easily commit changes to your Git repository with custom messages.

### Command Syntax

```bash
mgt c
```

### Options:

- `-t` or `--type`: The type of the commit (e.g., `feat`, `fix`, `chore`, etc.). If not provided, you'll be prompted to select from a list of common commit types.
- `-m` or `--message`: The commit message. If not provided, you'll be prompted to enter one.
- `-c` or `--content`: Files to include in the commit. You can specify multiple files by repeating the flag.
- `--dry`: If set, will only display the commands without executing them.

### Example Usage:

1. **Basic commit:**

```bash
mgt c -t feat -m "Add new feature"
```

2. **Commit with content (files):**

```bash
mgt c -t fix -m "Fix bug in feature" -c file1.py file2.py
```

3. **Dry-run commit (no changes made):**

```bash
mgt c -t chore -m "Update README" --dry
```

## Contribution

If you want to contribute to the development of this tool, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and write tests if necessary.
4. Submit a pull request with a clear description of your changes.

---

Thank you for using **MyGit CLI**. Happy committing! 🎉
