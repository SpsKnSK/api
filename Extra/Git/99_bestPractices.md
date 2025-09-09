# 🚀 Best Practices in Git

Using Git well helps keep your projects organized, teamwork smooth, and history clean. Here are some simple tips to follow:

## 1. Commit Often and with Clear Messages

Make small, frequent commits with descriptive messages.
Example:
```bash
git commit -m "Fix login button styling"
```

## 2. Use Branches for Features and Fixes

Keep your work separate by creating branches. This avoids messing up the main code.
Example:
```bash
git checkout -b feature/signup-form
```

## 3. Pull Before You Push

Always run `git pull` before pushing to avoid conflicts with others’ changes.

## 4. Write Good Commit Messages

Start with a short summary (50 characters max), then add details if needed.
Example:
```txt
Add user profile page

- Added profile picture upload  
- Created API endpoint for updating info
```
## 5. Review Changes Before Committing

Use g`it status` and `git diff` to check what you’re about to commit.

## 6. Don’t Commit Generated or Sensitive Files

Add files like build outputs or passwords to `.gitignore` to keep your repo clean and secure.

## 7. Use Pull Requests (PRs)

Collaborate by submitting PRs for teammates to review your changes before merging.

## 8. Resolve Conflicts Carefully

When conflicts happen, review and test the code before committing the resolved changes.

# 🎯 Summary
| Practice                      | Why?                              |
| ----------------------------- | --------------------------------- |
| Commit often & clear messages | Easier to track changes           |
| Use branches                  | Keep features isolated            |
| Pull before push              | Avoid conflicts                   |
| Write good messages           | Helps team understand changes     |
| Review before committing      | Prevent mistakes                  |
| Use `.gitignore`              | Keep repo clean & secure          |
| Use PRs                       | Improve collaboration and quality |
| Resolve conflicts carefully   | Keep code stable                  |
