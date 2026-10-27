# Upload TopoFineMap to GitHub

Repository name: **TopoFineMap**

## Web upload

1. Sign in to GitHub.
2. Choose **New repository**.
3. Repository name: `TopoFineMap`.
4. Visibility: **Public**.
5. Do not initialize with another README, license or `.gitignore`.
6. Create the repository.
7. Extract `TopoFineMap.zip` locally.
8. Open the extracted `TopoFineMap` folder.
9. On GitHub select **Add file -> Upload files**.
10. Upload the contents of the extracted folder.
11. Commit message:
   `Initial public release for TopoFineMap Paper A`
12. Confirm that the repository is public.
13. Copy its URL and insert it into the manuscript Code availability section.

## Release tag

Recommended:
- tag: `v1.0.0-paperA`
- title: `TopoFineMap public release for Paper A`

## Local preflight

```bash
python scripts/reproduce/validate_release.py
pytest -q
python scripts/figures/build_all_figures.py
```
