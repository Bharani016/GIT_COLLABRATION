# Git Collaboration Demo

A demonstration project showcasing a professional Git collaboration workflow using Git and GitHub. This repository demonstrates feature branching, pull requests, Conventional Commits, merge conflict resolution, and semantic versioning through a simple calculator application.

---

# Project Overview

This project was created to demonstrate industry-standard Git collaboration practices followed by software development teams.

The project includes a simple Python calculator application while focusing on the complete Git workflow rather than application complexity.

## Objectives

- Initialize a Git repository
- Manage source code using Git
- Create and work with feature branches
- Use Conventional Commit messages
- Collaborate using Pull Requests
- Resolve merge conflicts
- Manage project releases using Git tags

---

# Features

## Calculator

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%)

## Git Collaboration

- Repository initialization
- Feature branch workflow
- Pull Request workflow
- Conventional Commits
- Merge conflict demonstration
- Semantic version tagging
- Documentation updates

---

# Project Structure

```text
.
├── LICENSE
├── README.md
├── .gitignore
└── src
    └── calc.py
```

---

# Git Collaboration Workflow

This project follows a feature-based development workflow commonly used in professional software teams.

```text
                main
                  │
     ┌────────────┴────────────┐
     │                         │
feature/calculator-modules  docs/readme-update
     │                         │
     └──────────┬──────────────┘
                │
         Pull Request (PR)
                │
          Code Review
                │
             Merge
                │
              main
```

---

# Branching Strategy

## Main Branch

```text
main
```

The **main** branch always contains stable and production-ready code.

## Feature Branches

Feature branches are created from the main branch for developing new features or documentation.

Examples:

```text
feature/calculator-modules
docs/readme-update
feature/conflict-demo
```

Development workflow:

1. Create a feature branch from `main`
2. Implement the required changes
3. Test the changes
4. Commit using Conventional Commits
5. Push the branch to GitHub
6. Create a Pull Request
7. Review the changes
8. Merge into `main`

---

# Conventional Commits

All commits follow the Conventional Commits specification.

Format:

```text
type: description
```

## Commit Types

| Type | Description |
|------|-------------|
| feat | Introduces a new feature |
| fix | Fixes a bug |
| docs | Documentation updates |
| refactor | Code restructuring without changing functionality |
| test | Adds or updates tests |
| chore | Maintenance tasks |

## Example Commit Messages

```text
feat: add calculator with basic operators
feat: add modulus operation
docs: update project README
fix: resolve merge conflict
```

---

# Pull Request Workflow

All new features are integrated into the **main** branch through Pull Requests.

Workflow:

1. Create a feature branch
2. Develop the feature
3. Commit changes
4. Push the branch
5. Open a Pull Request
6. Review the changes
7. Merge into `main`

---

# Merge Conflict Resolution

A merge conflict occurs when two branches modify the same section of a file.

Example conflict markers:

```text
<<<<<<< HEAD
Current branch changes
=======
Incoming branch changes
>>>>>>> feature/conflict-demo
```

Resolution process:

1. Identify conflicting files
2. Edit the file
3. Remove conflict markers
4. Keep the required code
5. Stage the resolved file
6. Commit the resolution

Example:

```bash
git add .
git commit -m "fix: resolve merge conflict"
```

---

# Semantic Versioning

This project follows Semantic Versioning.

Format:

```text
MAJOR.MINOR.PATCH
```

Current versions:

| Version | Description |
|----------|-------------|
| v1.0.0 | Initial calculator release |
| v2.0.0 | Added modulus operation |

Create a release tag:

```bash
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0
```

---

# Common Git Commands

## Create a Feature Branch

```bash
git switch -c feature/branch-name
```

## Stage Changes

```bash
git add .
```

## Commit Changes

```bash
git commit -m "feat: add new feature"
```

## Push Branch

```bash
git push -u origin feature/branch-name
```

## Create Pull Request

```bash
gh pr create
```

## Merge Pull Request

```bash
gh pr merge --merge
```

## Create Version Tag

```bash
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0
```

---

# Development Workflow

```text
Create Repository
        │
        ▼
Clone Repository
        │
        ▼
Create Feature Branch
        │
        ▼
Develop Feature
        │
        ▼
Commit Changes
        │
        ▼
Push Branch
        │
        ▼
Create Pull Request
        │
        ▼
Code Review
        │
        ▼
Merge into Main
        │
        ▼
Create Release Tag
```

---

# Team Guidelines

- Keep the `main` branch stable.
- Create a separate branch for every feature.
- Use meaningful Conventional Commit messages.
- Review code through Pull Requests.
- Keep commits focused and atomic.
- Resolve merge conflicts before merging.
- Create version tags for stable releases.

---

# Technologies Used

- Git
- GitHub
- GitHub CLI (gh)
- Python

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.