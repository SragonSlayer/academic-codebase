# Academic Codebase

Central repository for organizing and tracking programming coursework across multiple classes.

## Directory Structure

```
├── courses/              # All coursework organized by course
│   ├── CS101/           # Example: Individual course folder
│   │   ├── assignments/ # Problem sets and homework
│   │   ├── projects/    # Larger programming projects
│   │   ├── labs/        # Lab assignments
│   │   └── README.md    # Course info and notes
│   ├── MATH201/
│   └── _template/       # Template for new courses
├── resources/           # Shared learning materials
│   ├── study-guides/
│   ├── reference-materials/
│   └── README.md
├── utils/               # Reusable code and utilities
│   └── shared-code/
└── COURSES.md           # Quick reference of all courses
```

## Getting Started

1. **Adding a course**: Copy `courses/_template/` to `courses/COURSE_ID` and customize
2. **Organizing assignments**: Use `assignments/`, `projects/`, or `labs/` subdirectories
3. **Tracking progress**: Update [COURSES.md](COURSES.md) with your enrolled courses
4. **Sharing utilities**: Store reusable code in `utils/shared-code/`

## Quick Links

- [Course Index](COURSES.md) - All courses and enrollment status
- [Resources](resources/) - Study materials and references
- [Shared Code](utils/shared-code/) - Common utilities
