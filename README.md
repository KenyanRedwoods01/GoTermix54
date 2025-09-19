# GoTermix54 CLI Command Hierarchy

## 🧭 Root Command: `gotermix54`

```sh
gotermix54 [OPTIONS] <COMMAND> [ARGS...]
```

### Global Options (Apply to all subcommands)
- `-h, --help` → Show help for command
- `-v, --version` → Show version
- `--verbose` → Enable verbose logging
- `--quiet` → Suppress non-essential output
- `--config <path>` → Use custom config file
- `--ai-model <mistral|codestral|auto>` → Override default AI model
- `--no-ai` → Bypass AI layer, passthrough only

---

## 🖥️ 1. SYSTEM — Linux & Termux Passthrough + AI Assist

### `gotermix54 sys <command> [args...]`
> Execute native shell commands with optional AI context.

```sh
gotermix54 sys ls -la
gotermix54 sys top
gotermix54 sys grep "error" /var/log/syslog
```

### `gotermix54 explain <command-or-query>`
> Get AI-powered explanation of command, output, or concept.

```sh
gotermix54 explain "df -h"
gotermix54 explain "why is my disk full?"
gotermix54 explain process 1234
```

### `gotermix54 man <command>`
> AI-enhanced manual pages with examples, pitfalls, and modern alternatives.

```sh
gotermix54 man awk
gotermix54 man systemctl
```

### `gotermix54 fix <issue-type>`
> Auto-diagnose and fix common system issues.

```sh
gotermix54 fix perms        # Fix file permissions recursively
gotermix54 fix port 3000    # Kill process using port 3000
gotermix54 fix disk         # Clean temp/cache if disk full
```

### `gotermix54 process [options]`
> List and analyze running processes with AI insights.

```sh
gotermix54 process                  # List top resource-consuming processes
gotermix54 process --all            # Show all processes
gotermix54 process --pid 1234       # Explain specific PID
gotermix54 process --kill 1234      # Ask AI if safe, then kill
```

### `gotermix54 cron <action> [args]`
> Manage cron jobs with natural language.

```sh
gotermix54 cron create "backup /home at 2am daily" --name=backup-home
gotermix54 cron list
gotermix54 cron remove backup-home
gotermix54 cron edit backup-home --time="3am"
```

---

## 🏗️ 2. DEV — Project Generation & Code Management

### `gotermix54 create <project-name> [options]`
> Scaffold full-stack projects with AI.

```sh
gotermix54 create myapp --stack=react,node,postgres
gotermix54 create blog --stack=nextjs,prisma
gotermix54 create api --stack=fastapi --auth=jwt
gotermix54 create mobile --stack=react-native
```

#### Options:
- `--stack <tech1,tech2,...>` → e.g., `react,node,mongo`
- `--auth <type>` → `jwt`, `oauth2`, `session`
- `--ui <type>` → `tailwind`, `mui`, `bootstrap`
- `--deploy <target>` → `vercel`, `heroku`, `netlify`
- `--template <url>` → Custom starter template

---

### `gotermix54 gen <type> <description>`
> Generate code, components, tests, or features.

```sh
gotermix54 gen component "ProductCard with image, title, price"
gotermix54 gen feature "real-time chat with socket.io"
gotermix54 gen test "unit test for login function"
gotermix54 gen migration "add user_role column to users table"
```

#### Types:
- `component`
- `feature`
- `test`
- `hook`
- `migration`
- `config`
- `script`

---

### `gotermix54 edit <file> [options]`
> AI-powered code refactoring and editing.

```sh
gotermix54 edit src/utils.py --instruction="convert sync to async"
gotermix54 edit App.js --refactor="use hooks instead of class"
gotermix54 edit .env --secure="encrypt secrets"
```

#### Options:
- `--instruction <text>` → What to change
- `--refactor` → Suggest modern patterns
- `--secure` → Flag and fix security issues
- `--dry-run` → Show diff without applying

---

### `gotermix54 debug <file-or-log> [options]`
> AI-assisted debugging.

```sh
gotermix54 debug src/server.js
gotermix54 debug logs/error.log --filter="timeout"
gotermix54 debug --last-error   # Auto-detect last crash/error
```

---

### `gotermix54 test <action> [files...]`
> Generate and run tests with AI.

```sh
gotermix54 test add authController.js     # Generate missing tests
gotermix54 test run                       # Run all tests
gotermix54 test coverage                  # Show coverage + AI gaps
gotermix54 test fix failing.test.js       # Auto-fix failing test
```

---

## 🚀 3. OPS — DevOps, Deployment & CI/CD

### `gotermix54 run [options]`
> Start dev server with AI-configured defaults.

```sh
gotermix54 run
gotermix54 run --port 8080
gotermix54 run --inspect   # Attach debugger
```

### `gotermix54 build [options]`
> Build for production.

```sh
gotermix54 build
gotermix54 build --minify
gotermix54 build --analyze   # Show bundle size + AI optimization tips
```

### `gotermix54 dockerize [options]`
> Generate Dockerfile and docker-compose.yml.

```sh
gotermix54 dockerize
gotermix54 dockerize --multi-stage
gotermix54 dockerize --nginx
```

### `gotermix54 ci <provider> [options]`
> Generate CI/CD config.

```sh
gotermix54 ci github
gotermix54 ci gitlab --test --deploy
gotermix54 ci bitbucket --branch=main
```

### `gotermix54 deploy <target> [options]`
> Deploy to cloud with one command.

```sh
gotermix54 deploy vercel
gotermix54 deploy heroku --env=production
gotermix54 deploy netlify --dir=out
gotermix54 deploy ssh user@host:/var/www --key=~/.ssh/deploy_key
```

#### Supported Targets:
- `vercel`
- `heroku`
- `netlify`
- `aws`
- `gcp`
- `ssh`
- `dockerhub`

---

## 📦 4. PKG — Unified Package Management

### `gotermix54 install <package> [options]`
> Auto-detect package manager and install.

```sh
gotermix54 install docker         # → apt install docker
gotermix54 install numpy          # → pip install numpy
gotermix54 install express        # → npm install express
gotermix54 install @types/react   # → npm install -D
```

#### Options:
- `--global` → Install globally
- `--dev` → Install as dev dependency
- `--force` → Force reinstall
- `--dry-run` → Simulate install

### `gotermix54 uninstall <package>`
> Remove package.

### `gotermix54 update <package>`
> Update package.

### `gotermix54 search <query>`
> Search across apt, npm, pip, pkg.

```sh
gotermix54 search image processing
```

---

## 🎓 5. LEARN — Teaching & Quizzing Assistant

### `gotermix54 tutor <topic> [options]`
> Start interactive tutorial.

```sh
gotermix54 tutor linux
gotermix54 tutor python --level=intermediate
gotermix54 tutor kubernetes --hands-on
```

#### Options:
- `--level <beginner|intermediate|advanced>`
- `--hands-on` → Include mini-exercises
- `--cheatsheet` → Output summary cheatsheet

---

### `gotermix54 quiz <topic> [options]`
> Generate and run quiz.

```sh
gotermix54 quiz bash
gotermix54 quiz javascript --num=10
gotermix54 quiz docker --adaptive   # Adjust difficulty based on performance
```

#### Options:
- `--num <N>` → Number of questions
- `--adaptive` → AI adjusts difficulty
- `--review` → Show explanations after each question

---

### `gotermix54 explain <concept>`
> Deep-dive explanation (alias of root `explain`).

```sh
gotermix54 learn explain "how does DNS work?"
gotermix54 learn explain "what is middleware in Express?"
```

---

## 🛠️ 6. CONFIG — Project & Tool Configuration

### `gotermix54 init [options]`
> Initialize `.gotermix54` config in current directory.

```sh
gotermix54 init
gotermix54 init --ai-model=codestral
gotermix54 init --stack=python,fastapi
```

### `gotermix54 config <get|set|list> [key] [value]`
> Manage config values.

```sh
gotermix54 config set ai.model mistral
gotermix54 config get deploy.target
gotermix54 config list
```

### `gotermix54 context [options]`
> Show or reset AI context (current project, files, goals).

```sh
gotermix54 context          # Show current context
gotermix54 context reset    # Clear memory/context
gotermix54 context add-file important.py
```

---

## 🧩 Plugin System (Advanced)

### `gotermix54 plugin <install|remove|list> <name>`
> Extend CLI with plugins.

```sh
gotermix54 plugin install k8s
gotermix54 plugin remove aws
gotermix54 plugin list
```

Plugins live in `~/.gotermix54/plugins/` and expose new subcommands.

---

## 🧪 Example Full Workflow

```sh
# Initialize project
mkdir myproject && cd myproject
gotermix54 init --stack=react,node

# Create app
gotermix54 create myproject --stack=react,node,sqlite

# Add auth feature
gotermix54 gen feature "JWT auth with refresh tokens"

# Edit config
gotermix54 edit config.js --instruction="increase timeout to 30s"

# Run locally
gotermix54 run

# Add tests
gotermix54 test add src/auth.js

# Deploy
gotermix54 deploy vercel

# Learn while you wait
gotermix54 tutor react-hooks --level=intermediate
```

---

## 📁 Filesystem Structure (Per Project)

```
myproject/
├── .gotermix54/
│   ├── config.json          # Project-specific settings
│   ├── context.json         # AI context: goals, files, memory
│   ├── history.log          # Command history
│   └── plugins/             # Local plugins (if any)
├── src/
├── public/
├── package.json
└── ...
```

Global config: `~/.gotermix54/config.json`

---

## ✅ Validation Rules

- All AI edits require `--yes` or interactive confirmation unless `--force`.
- `--dry-run` must show full diff/output without side effects.
- System commands (`sys`, `fix`, `process`) must never break system without confirmation.
- Respect `.gitignore` and `node_modules/` in AI context unless explicitly included.

---

## 🧭 Navigation & Help Conventions

```sh
gotermix54 help             # Show all commands
gotermix54 help dev         # Show dev subcommands
gotermix54 help create      # Show detailed create usage

gotermix54 --help           # Same as help
gotermix54 create --help    # Help for specific subcommand
```

---

## 🧠 AI Model Routing Logic

- `create`, `gen`, `edit`, `test` → Prefer **Codestral** (code generation)
- `explain`, `tutor`, `quiz`, `man`, `debug` → Prefer **Mistral** (reasoning/NL)
- `sys`, `fix`, `process`, `cron` → Use **Mistral** for analysis, passthrough for execution
- Fallback: if model unavailable → use `auto` → pick best available

Configurable via:
- CLI flag: `--ai-model <model>`
- Config file: `ai.model`
- Env var: `GOTERMIX54_AI_MODEL`

```

---

✅ **You now have a complete, production-grade CLI specification** — ready for engineering teams or AI agents to implement.

---

## 🚀 Next Steps?

Would you like me to now generate:

1. **The actual Python/Node.js skeleton code** for the CLI parser (using `click`, `argparse`, or `commander`)?
2. **The `.gotermix54/config.json` schema** (with JSON Schema)?
3. **Mock implementation of 1–2 core commands** (e.g., `create` and `explain`)?
4. **Termux-specific installer script** (`install-gotermix54.sh`)?

Let me know which piece you want built next — I’ll generate it in full working code.  
This project is 🔥 ready to be coded.

```
