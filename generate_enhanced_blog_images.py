#!/usr/bin/env python3
"""
Generate enhanced professional featured images for all 20 blog posts
Creates 1200x630px images with rich content, icons, diagrams, and topic details
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

# Create images folder if it doesn't exist
images_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(images_dir, exist_ok=True)

# Define blog images with their enhanced properties
blog_images = [
    {
        'filename': 'blog-xml-sitemap.png',
        'title': 'XML Sitemap',
        'subtitle': 'Strategy Guide 2026',
        'color1': '#0f172a',  # Dark slate
        'color2': '#1e3a8a',  # Deep blue
        'accent': '#06b6d4',  # Cyan
        'content': [
            'Dynamic Generation',
            'Crawl Budget Optimization',
            'Priority Algorithms',
            'Image Sitemaps'
        ],
        'metrics': ['37% Faster Indexing', '23% Improved Crawl', '18% Better Visibility']
    },
    {
        'filename': 'blog-seo-audit.png',
        'title': 'Technical SEO',
        'subtitle': 'Audit Checklist',
        'color1': '#065f46',  # Deep green
        'color2': '#10b981',  # Green
        'accent': '#34d399',  # Light green
        'content': [
            'Site Speed Analysis',
            'Mobile Responsiveness',
            'Structured Data',
            'Core Web Vitals'
        ],
        'metrics': ['50+ Checkpoints', 'Full Site Analysis', 'Actionable Reports']
    },
    {
        'filename': 'blog-nextjs-seo.png',
        'title': 'Next.js SEO',
        'subtitle': 'Architecture Guide',
        'color1': '#0f0f0f',  # Black
        'color2': '#1a1a1a',  # Dark gray
        'accent': '#fbbf24',  # Amber
        'content': [
            'SSR & Static Generation',
            'Dynamic Routes',
            'Meta Tags',
            'Image Optimization'
        ],
        'metrics': ['Faster Loading', 'Better Rankings', 'Perfect Lighthouse']
    },
    {
        'filename': 'blog-aeo-geo.png',
        'title': 'AEO & GEO',
        'subtitle': 'Optimization Guide',
        'color1': '#3f0f0f',  # Dark red
        'color2': '#7c2d12',  # Brown
        'accent': '#fb923c',  # Orange
        'content': [
            'AI-Enhanced Search',
            'Geographic Targeting',
            'Local Intent Signals',
            'Context Awareness'
        ],
        'metrics': ['+45% Local Traffic', 'Better SERP Position', 'Higher CTR']
    },
    {
        'filename': 'blog-cloudflare.png',
        'title': 'Cloudflare',
        'subtitle': 'Optimization Guide',
        'color1': '#0c4a6e',  # Deep sky
        'color2': '#0369a1',  # Sky blue
        'accent': '#fbbf24',  # Amber
        'content': [
            'CDN Optimization',
            'DDoS Protection',
            'Page Rules',
            'Analytics & Monitoring'
        ],
        'metrics': ['+99.9% Uptime', '60% Faster CDN', 'Global Coverage']
    },
    {
        'filename': 'blog-ai-agents.png',
        'title': 'AI Agent',
        'subtitle': 'Architecture Guide',
        'color1': '#0f172a',  # Slate dark
        'color2': '#1e293b',  # Slate
        'accent': '#06b6d4',  # Cyan
        'content': [
            'Agent Design Patterns',
            'Tool Integration',
            'Decision Trees',
            'Learning Loops'
        ],
        'metrics': ['Autonomous Systems', 'Self-Improving', 'Scalable']
    },
    {
        'filename': 'blog-schema.png',
        'title': 'Schema',
        'subtitle': 'Engineering Guide',
        'color1': '#1f1f1f',  # Dark
        'color2': '#2d2d2d',  # Gray
        'accent': '#f97316',  # Orange
        'content': [
            'Structured Data Markup',
            'Rich Snippets',
            'JSON-LD Implementation',
            'Validation Tools'
        ],
        'metrics': ['Rich Results', 'Better SERP', 'Higher CTR']
    },
    {
        'filename': 'blog-wordpress.png',
        'title': 'WordPress',
        'subtitle': 'Hooks Guide',
        'color1': '#001a26',  # Dark teal
        'color2': '#003d4d',  # Teal
        'accent': '#20b2aa',  # Light sea green
        'content': [
            'Action Hooks',
            'Filter Hooks',
            'Plugin Development',
            'Best Practices'
        ],
        'metrics': ['40+ Hook Types', 'Custom Plugins', 'Extensible']
    },
    {
        'filename': 'blog-ghost.png',
        'title': 'Ghost CMS',
        'subtitle': 'Publishing Guide',
        'color1': '#0a0a0a',  # Black
        'color2': '#1a1a1a',  # Dark gray
        'accent': '#e94560',  # Red
        'content': [
            'Membership Platform',
            'Email Newsletters',
            'Content Management',
            'Analytics Built-in'
        ],
        'metrics': ['Fast Publishing', 'Member Monetization', 'SEO Ready']
    },
    {
        'filename': 'blog-ionic.png',
        'title': 'Ionic',
        'subtitle': 'Framework Guide',
        'color1': '#1a3a5c',  # Dark blue
        'color2': '#3880ff',  # Ionic blue
        'accent': '#fbbf24',  # Amber
        'content': [
            'Cross-Platform Apps',
            'Native Components',
            'Performance',
            'App Store Ready'
        ],
        'metrics': ['Build Once, Deploy Everywhere', '1 Codebase', 'Production Ready']
    },
    {
        'filename': 'blog-frameworks.png',
        'title': 'Frameworks',
        'subtitle': 'Comparison Guide',
        'color1': '#0f0f0f',  # Black
        'color2': '#2d2d2d',  # Gray
        'accent': '#10b981',  # Green
        'content': [
            'Ionic vs Flutter',
            'vs React Native',
            'Performance Metrics',
            'Use Case Comparison'
        ],
        'metrics': ['Side-by-Side Analysis', 'Cost Comparison', 'Best Practices']
    },
    {
        'filename': 'blog-app-store.png',
        'title': 'App Store',
        'subtitle': 'Submission Checklist',
        'color1': '#000000',  # Black
        'color2': '#1a1a1a',  # Dark gray
        'accent': '#34c759',  # Green
        'content': [
            'iOS Submission Steps',
            'Android Deployment',
            'Review Guidelines',
            'Marketing Kit'
        ],
        'metrics': ['50+ Items to Check', 'Approval Guide', 'Optimization Tips']
    },
    {
        'filename': 'blog-app-cost.png',
        'title': 'Ionic App',
        'subtitle': 'Development Cost',
        'color1': '#0f1419',  # Dark
        'color2': '#1e3a5f',  # Blue
        'accent': '#10b981',  # Green
        'content': [
            'Cost Estimation',
            'Resource Planning',
            'Time Breakdown',
            'ROI Analysis'
        ],
        'metrics': ['Budget Calculator', 'Cost Reduction Tips', 'Team Structure']
    },
    {
        'filename': 'blog-ionic-laravel.png',
        'title': 'Ionic + Laravel',
        'subtitle': 'Integration Guide',
        'color1': '#1a2333',  # Dark
        'color2': '#3880ff',  # Ionic blue
        'accent': '#ff2d55',  # Red
        'content': [
            'API Connection Setup',
            'Authentication',
            'Data Synchronization',
            'Real-time Updates'
        ],
        'metrics': ['REST API', 'Token-based Auth', 'Websocket Support']
    },
    {
        'filename': 'blog-capacitor.png',
        'title': 'Capacitor',
        'subtitle': 'Plugins Guide',
        'color1': '#0a2540',  # Dark blue
        'color2': '#119eff',  # Capacitor blue
        'accent': '#fbbf24',  # Amber
        'content': [
            'Native Capabilities',
            'Device APIs',
            'Plugin Development',
            'Bridge Architecture'
        ],
        'metrics': ['50+ Plugins', 'Native Features', 'Cross-Platform']
    },
    {
        'filename': 'blog-claude-ai.png',
        'title': 'Claude AI for',
        'subtitle': 'Developers Guide',
        'color1': '#0d0d0d',  # Black
        'color2': '#1a1a1a',  # Dark
        'accent': '#ff6b35',  # Orange
        'content': [
            'API Integration',
            'Prompt Engineering',
            'Model Selection',
            'Use Cases'
        ],
        'metrics': ['100K+ Tokens', 'Multimodal', 'Production Ready']
    },
    {
        'filename': 'blog-claude-code.png',
        'title': 'Claude Code',
        'subtitle': 'CLI Tool Guide',
        'color1': '#0d0d0d',  # Black
        'color2': '#1a1a1a',  # Dark
        'accent': '#4ecdc4',  # Teal
        'content': [
            'Code Generation',
            'Local Development',
            'Terminal Integration',
            'Command Reference'
        ],
        'metrics': ['Real-time Coding', 'SSH Support', 'Project Aware']
    },
    {
        'filename': 'blog-ai-comparison.png',
        'title': 'Claude vs',
        'subtitle': 'ChatGPT vs Gemini',
        'color1': '#111827',  # Gray
        'color2': '#374151',  # Light gray
        'accent': '#06b6d4',  # Cyan
        'content': [
            'Capability Comparison',
            'Speed & Latency',
            'Cost Analysis',
            'Best Use Cases'
        ],
        'metrics': ['Feature Breakdown', 'Performance Metrics', 'Pricing Guide']
    },
    {
        'filename': 'blog-claude-api.png',
        'title': 'Building with',
        'subtitle': 'Claude API',
        'color1': '#0d0d0d',  # Black
        'color2': '#1a1a1a',  # Dark
        'accent': '#ff9500',  # Orange
        'content': [
            'API Endpoints',
            'Authentication',
            'Error Handling',
            'Best Practices'
        ],
        'metrics': ['Complete Documentation', 'Code Examples', 'SDKs Available']
    },
    {
        'filename': 'blog-openclaw.png',
        'title': 'OpenClaw',
        'subtitle': 'AI Framework',
        'color1': '#1f2937',  # Dark gray
        'color2': '#374151',  # Gray
        'accent': '#8b5cf6',  # Purple
        'content': [
            'AI Orchestration',
            'Workflow Automation',
            'Agent Framework',
            'Enterprise Features'
        ],
        'metrics': ['Multi-Agent', 'Scalable', 'Enterprise Ready']
    },
]

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def draw_icon(draw, x, y, size, icon_type, color):
    """Draw simple icons"""
    colors = hex_to_rgb(color)

    if icon_type == 'check':
        # Checkmark
        draw.line([(x, y + size//2), (x + size//3, y + size)], fill=colors, width=3)
        draw.line([(x + size//3, y + size), (x + size, y)], fill=colors, width=3)
    elif icon_type == 'gear':
        # Gear/settings icon
        draw.ellipse([x, y, x + size, y + size], outline=colors, width=2)
        draw.rectangle([x + size//4, y - 2, x + 3*size//4, y + 2], fill=colors)
        draw.rectangle([x - 2, y + size//4, x + 2, y + 3*size//4], fill=colors)
    elif icon_type == 'chart':
        # Bar chart
        bar_width = size // 5
        draw.rectangle([x, y + size//2, x + bar_width, y + size], fill=colors)
        draw.rectangle([x + bar_width + 2, y + size//3, x + 2*bar_width + 2, y + size], fill=colors)
        draw.rectangle([x + 2*bar_width + 4, y + size//4, x + 3*bar_width + 4, y + size], fill=colors)
    elif icon_type == 'lightning':
        # Lightning bolt
        points = [x + size//2, y, x + size, y + size//2, x + size//2, y + size//2, x, y + size]
        draw.polygon(points, fill=colors)
    elif icon_type == 'target':
        # Target/bullseye
        draw.ellipse([x, y, x + size, y + size], outline=colors, width=2)
        draw.ellipse([x + size//4, y + size//4, x + 3*size//4, y + 3*size//4], outline=colors, width=1)
    elif icon_type == 'rocket':
        # Simple rocket
        draw.polygon([(x + size//2, y), (x + size, y + 2*size//3), (x, y + 2*size//3)], fill=colors)
        draw.rectangle([x + 2*size//5, y + 2*size//3, x + 3*size//5, y + size], fill=colors)

def create_enhanced_featured_image(config):
    """Create an enhanced featured image with rich content"""
    width, height = 1200, 630

    # Create image with gradient background
    img = Image.new('RGB', (width, height), color=hex_to_rgb(config['color1']))
    draw = ImageDraw.Draw(img, 'RGBA')

    # Draw gradient background
    color1 = hex_to_rgb(config['color1'])
    color2 = hex_to_rgb(config['color2'])

    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    accent = hex_to_rgb(config['accent'])

    # Add decorative circles
    draw.ellipse([(width - 200, -100), (width + 150, 150)], fill=accent + (80,))
    draw.ellipse([(-100, height - 150), (100, height + 100)], fill=accent + (80,))

    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 64)
        subtitle_font = ImageFont.truetype("arial.ttf", 28)
        content_font = ImageFont.truetype("arial.ttf", 18)
        small_font = ImageFont.truetype("arial.ttf", 14)
    except:
        title_font = subtitle_font = content_font = small_font = ImageFont.load_default()

    # Draw main title
    title_y = 40
    title_text = config['title']
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = 50
    draw.text((title_x, title_y), title_text, fill=(255, 255, 255), font=title_font)

    # Draw subtitle
    subtitle_y = title_y + 70
    subtitle_text = config['subtitle']
    draw.text((title_x, subtitle_y), subtitle_text, fill=accent, font=subtitle_font)

    # Draw content items (left side)
    content_y = subtitle_y + 80
    content_x = 50
    item_height = 35

    for i, item in enumerate(config['content'][:4]):
        # Draw checkmark icon
        draw_icon(draw, content_x, content_y + i * item_height, 16, 'check', config['accent'])

        # Draw item text
        draw.text((content_x + 30, content_y + i * item_height - 5), f"• {item}", fill=(220, 220, 220), font=content_font)

    # Draw metrics (right side)
    metrics_x = width - 380
    metrics_y = 120
    metric_height = 120

    for i, metric in enumerate(config['metrics']):
        metric_box_y = metrics_y + i * metric_height

        # Draw rounded rectangle background
        box_color = (*accent, 30)
        draw.rectangle([metrics_x, metric_box_y, metrics_x + 320, metric_box_y + 90], fill=box_color, outline=accent, width=2)

        # Draw metric text
        metric_parts = metric.split()
        if metric_parts:
            draw.text((metrics_x + 15, metric_box_y + 10), metric_parts[0], fill=accent, font=subtitle_font)
            remaining = ' '.join(metric_parts[1:])
            if remaining:
                draw.text((metrics_x + 15, metric_box_y + 45), remaining, fill=(200, 200, 200), font=small_font)

    # Add bottom accent bar
    draw.rectangle([0, height - 10, width, height], fill=accent)

    return img

# Generate all images
print("Generating 20 enhanced blog featured images...")
for i, config in enumerate(blog_images, 1):
    try:
        img = create_enhanced_featured_image(config)
        filepath = os.path.join(images_dir, config['filename'])
        img.save(filepath, 'PNG', quality=95)
        print(f"[OK] {i}/20 - {config['filename']}")
    except Exception as e:
        print(f"[ERROR] {i}/20 - {config['filename']} - Error: {e}")

print(f"\nDone! Enhanced images saved to: {images_dir}")
print(f"Images now include topic-specific content, icons, and metrics!")
