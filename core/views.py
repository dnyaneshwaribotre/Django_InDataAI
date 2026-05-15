from django.shortcuts import render, redirect
from django.contrib import messages

SERVICES_LIST = [
    {
        'icon': '🧠', 'title': 'Machine Learning',
        'desc': 'We design and deploy custom ML models — from tabular data classifiers to complex deep learning systems — trained specifically on your data.',
        'points': ['Supervised & unsupervised learning', 'Deep neural networks', 'Transfer learning & fine-tuning', 'Model monitoring & retraining'],
        'stat': '94%', 'stat_label': 'Average model accuracy improvement',
    },
    {
        'icon': '📊', 'title': 'Data Analytics',
        'desc': 'Transform your raw data into actionable insights with advanced analytics, statistical modeling, and beautiful interactive dashboards.',
        'points': ['Descriptive & predictive analytics', 'Real-time dashboards', 'A/B testing frameworks', 'Self-service BI tools'],
        'stat': '3x', 'stat_label': 'Faster time-to-insight',
    },
    {
        'icon': '💡', 'title': 'AI Solutions',
        'desc': 'End-to-end AI products including NLP pipelines, computer vision systems, recommendation engines, and intelligent automation.',
        'points': ['Natural language processing', 'Computer vision', 'Recommendation systems', 'Conversational AI / chatbots'],
        'stat': '60%', 'stat_label': 'Average operational cost reduction',
    },
    {
        'icon': '☁️', 'title': 'Cloud Data Engineering',
        'desc': 'Scalable, reliable data infrastructure on AWS, GCP, and Azure — from ingestion pipelines to data warehouses and streaming systems.',
        'points': ['Data lake & warehouse design', 'ETL/ELT pipelines', 'Real-time streaming with Kafka', 'Multi-cloud architecture'],
        'stat': '99.9%', 'stat_label': 'Pipeline uptime SLA',
    },
    {
        'icon': '🛡️', 'title': 'Data Governance',
        'desc': 'Establish data quality, lineage, privacy compliance, and access control frameworks that protect your most valuable asset.',
        'points': ['GDPR / HIPAA compliance', 'Data cataloguing & lineage', 'Role-based access control', 'Data quality monitoring'],
        'stat': '100%', 'stat_label': 'Compliance audit pass rate',
    },
    {
        'icon': '📈', 'title': 'Business Intelligence',
        'desc': 'BI dashboards, reports, and self-service analytics that translate complex data into clear stories for every stakeholder.',
        'points': ['Tableau, Power BI, Looker', 'KPI framework design', 'Executive reporting suites', 'Embedded analytics'],
        'stat': '5x', 'stat_label': 'ROI on analytics investment',
    },
]

BLOG_POSTS = [
    {'icon': '🤖', 'tag': 'AI Trends', 'title': 'The Future of Generative AI in Enterprise', 'excerpt': 'How large language models are reshaping workflows — and what your business should do today to stay ahead.', 'date': 'May 10, 2025', 'read_time': 8},
    {'icon': '⚡', 'tag': 'Engineering', 'title': 'Building Real-Time Data Pipelines with Apache Kafka', 'excerpt': 'A practical guide to streaming data architectures for high-throughput analytics at any scale.', 'date': 'April 28, 2025', 'read_time': 12},
    {'icon': '🔍', 'tag': 'Machine Learning', 'title': 'Explainable AI: Making Models You Can Trust', 'excerpt': 'Why model transparency matters — and the techniques that make black-box models interpretable.', 'date': 'April 14, 2025', 'read_time': 10},
    {'icon': '🏗️', 'tag': 'Architecture', 'title': 'Data Mesh vs. Data Lake: Choosing the Right Architecture', 'excerpt': 'A decision framework to help you pick the right data architecture for your organization\'s maturity.', 'date': 'April 2, 2025', 'read_time': 9},
    {'icon': '🎯', 'tag': 'Strategy', 'title': 'Building an AI Roadmap That Actually Gets Executed', 'excerpt': 'The gap between AI strategy and delivery is wide. Here\'s how leading companies bridge it.', 'date': 'March 20, 2025', 'read_time': 7},
    {'icon': '🔐', 'tag': 'Data Governance', 'title': 'GDPR in the Age of AI: What You Need to Know', 'excerpt': 'How to design ML systems that are both powerful and compliant with modern privacy regulations.', 'date': 'March 5, 2025', 'read_time': 11},
]

def home(request):
    context = {
        'page': 'home',
        'stats': [
            {'number': '500+', 'label': 'Projects Delivered'},
            {'number': '98%', 'label': 'Client Satisfaction'},
            {'number': '12+', 'label': 'Years Experience'},
            {'number': '80+', 'label': 'Expert Team Members'},
        ],
        'services': SERVICES_LIST[:6],
        'testimonials': [
            {'name': 'Sarah Johnson', 'role': 'CTO, FinTech Corp', 'avatar': 'SJ', 'text': 'InData AI transformed our fraud detection system. Their ML model reduced false positives by 60% and saved us millions annually.'},
            {'name': 'Michael Chen', 'role': 'VP of Operations, RetailMax', 'avatar': 'MC', 'text': 'The demand forecasting solution they built is remarkable. We now predict inventory needs with 94% accuracy.'},
            {'name': 'Priya Kapoor', 'role': 'Head of Data, HealthNet', 'avatar': 'PK', 'text': 'Their team delivered a comprehensive data platform in just 3 months. The quality and communication were exceptional throughout.'},
        ],
        'blog_posts': BLOG_POSTS[:3],
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html', {
        'page': 'about',
        'team': [
            {'name': 'Alex Rivera', 'role': 'CEO & Co-Founder', 'initials': 'AR'},
            {'name': 'Lena Müller', 'role': 'Chief Data Scientist', 'initials': 'LM'},
            {'name': 'James Okafor', 'role': 'VP of Engineering', 'initials': 'JO'},
            {'name': 'Aisha Patel', 'role': 'Head of AI Research', 'initials': 'AP'},
            {'name': 'Daniel Park', 'role': 'Lead ML Engineer', 'initials': 'DP'},
            {'name': 'Sofia Torres', 'role': 'Head of Design', 'initials': 'ST'},
        ],
    })


def services(request):
    return render(request, 'core/services.html', {'page': 'services', 'services_list': SERVICES_LIST})


def blog(request):
    return render(request, 'core/blog.html', {'page': 'blog', 'posts': BLOG_POSTS})


def contact(request):
    return render(request, 'core/contact.html', {'page': 'contact'})


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        messages.success(request, f"Thanks {name}! We'll be in touch at {email} within 24 hours.")
        return redirect('contact')
    return redirect('contact')
