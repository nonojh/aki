""" Default ignore patterns for Gitingest. """

from typing import Set

DEFAULT_IGNORE_PATTERNS: Set[str] = {
    # Extension
    "*.txt",
    # General
    "private/",
    "private/*",
    "private/**",
    ".*",  # Ignore all dotfiles
    "*/.*",  # Ignore dotfiles in subdirectories
    ".*/*",  # Ignore dotfolders and their contents
    "*.bin",  # Ignore binary files
    "*.zip",
    "*.tar.gz",
    "*.dat",
    # Python
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "__pycache__",
    ".pytest_cache",
    ".coverage",
    ".tox",
    ".nox",
    ".mypy_cache",
    ".ruff_cache",
    ".hypothesis",
    "poetry.lock",
    "Pipfile.lock",
    "__init__.py",
    # JavaScript/FileSystemNode
    "node_modules",
    "bower_components",
    "package-lock.json",
    "yarn.lock",
    ".npm",
    ".yarn",
    ".pnpm-store",
    "bun.lock",
    "bun.lockb",
    # Java
    "*.class",
    "*.jar",
    "*.war",
    "*.ear",
    "*.nar",
    ".gradle/",
    "build/",
    "build/*",
    "build/**",
    ".settings/",
    ".classpath",
    "gradle-app.setting",
    "*.gradle",
    # IDEs and editors / Java
    ".project",
    # C/C++
    "*.o",
    "*.obj",
    "*.dll",
    "*.dylib",
    "*.exe",
    "*.lib",
    "*.out",
    "*.a",
    "*.pdb",
    # Swift/Xcode
    ".build/",
    "*.xcodeproj/",
    "*.xcworkspace/",
    "*.pbxuser",
    "*.mode1v3",
    "*.mode2v3",
    "*.perspectivev3",
    "*.xcuserstate",
    "xcuserdata/",
    ".swiftpm/",
    # Ruby
    "*.gem",
    ".bundle/",
    "vendor/bundle",
    "Gemfile.lock",
    ".ruby-version",
    ".ruby-gemset",
    ".rvmrc",
    # Rust
    "Cargo.lock",
    "**/*.rs.bk",
    # Java / Rust
    "target/",
    # Go
    "pkg/",
    # .NET/C#
    "obj/",
    "*.suo",
    "*.user",
    "*.userosscache",
    "*.sln.docstates",
    "packages/",
    "*.nupkg",
    # Go / .NET / C#
    "bin/",
    # Version control
    ".git",
    ".svn",
    ".hg",
    ".gitignore",
    ".gitattributes",
    ".gitmodules",
    # Images and media
    "*.svg",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.gif",
    "*.ico",
    "*.pdf",
    "*.mov",
    "*.mp4",
    "*.mp3",
    "*.wav",
    # Virtual environments
    "venv",
    ".venv",
    "env",
    ".env",
    "virtualenv",
    # IDEs and editors
    ".idea",
    ".vscode",
    ".vs",
    "*.swo",
    "*.swn",
    ".settings",
    "*.sublime-*",
    # Temporary and cache files
    "*.log",
    "*.bak",
    "*.swp",
    "*.tmp",
    "*.temp",
    ".cache",
    ".sass-cache",
    ".eslintcache",
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
    # Build directories and artifacts
    "build",
    "build/*",
    "build/**",
    "dist",
    "target",
    "out",
    "*.egg-info",
    "*.egg",
    "*.whl",
    "*.so",
    # Documentation
    "site-packages",
    ".docusaurus",
    ".next",
    ".nuxt",
    # Other common patterns
    ## Minified files
    "*.min.js",
    "*.min.css",
    ## Source maps
    "*.map",
    ## Terraform
    ".terraform",
    "*.tfstate*",
    ## Dependencies in various languages
    "vendor/",
    # Gitingest
    "digest.txt",
}
