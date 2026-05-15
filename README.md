# InData AI — Django Website

A responsive, dark-themed AI/Data company website built with Django.

## Pages
- `/` — Home (hero, stats, services, testimonials, blog preview, CTA)
- `/about/` — About (mission, values, team)
- `/services/` — All services with detailed descriptions
- `/blog/` — Blog listing
- `/contact/` — Contact form (with Django messages)

## Quick Start

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install Django
pip install django

# 3. Migrate & run
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000

## Structure
```
indataai_project/
├── core/                    # Main app
│   ├── templates/core/      # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── services.html
│   │   ├── blog.html
│   │   └── contact.html
│   ├── static/
│   │   ├── css/style.css    # All styles
│   │   └── js/main.js       # Navbar, animations
│   ├── views.py
│   └── urls.py
└── indataai_project/        # Django config
    ├── settings.py
    └── urls.py
```

## Design
- **Font**: Syne (headings) + DM Sans (body)
- **Palette**: Dark navy background with cyan (#00d4ff) and purple (#7b61ff) accents
- **Features**: Sticky navbar, scroll animations, responsive mobile menu, grain texture overlay
