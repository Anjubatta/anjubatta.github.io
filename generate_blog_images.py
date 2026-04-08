#!/usr/bin/env python3
"""
Generate professional featured images for all 20 blog posts
Creates 1200x630px images with topic-specific colors and designs
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create images folder if it doesn't exist
images_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(images_dir, exist_ok=True)

# Define blog images with their properties
blog_images = [
    {
        'filename': 'blog-xml-sitemap.png',
        'title': 'XML Sitemap\nStrategy 2026',
        'subtitle': 'Advanced Crawl Budget Optimization',
        'color1': '#1e3a8a',  # Deep blue
        'color2': '#3b82f6',  # Bright blue
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-seo-audit.png',
        'title': 'Technical SEO\nAudit Checklist',
        'subtitle': 'Complete Site Analysis Guide',
        'color1': '#065f46',  # Deep green
        'color2': '#10b981',  # Bright green
        'accent': '#f59e0b',  # Orange
    },
    {
        'filename': 'blog-nextjs-seo.png',
        'title': 'Next.js SEO\nArchitecture',
        'subtitle': 'Modern Framework Optimization',
        'color1': '#1f2937',  # Dark gray
        'color2': '#374151',  # Gray
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-aeo-geo.png',
        'title': 'AEO & GEO\nOptimization',
        'subtitle': 'AI-Enhanced Search Strategy',
        'color1': '#5b21b6',  # Deep purple
        'color2': '#a855f7',  # Bright purple
        'accent': '#ec4899',  # Pink
    },
    {
        'filename': 'blog-cloudflare.png',
        'title': 'Cloudflare\nOptimization',
        'subtitle': 'Performance & Security Guide',
        'color1': '#0c4a6e',  # Deep sky
        'color2': '#0ea5e9',  # Sky blue
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-ai-agents.png',
        'title': 'AI Agent\nArchitecture',
        'subtitle': 'Building Autonomous Systems',
        'color1': '#1e293b',  # Slate dark
        'color2': '#64748b',  # Slate light
        'accent': '#06b6d4',  # Cyan
    },
    {
        'filename': 'blog-schema.png',
        'title': 'Schema\nEngineering',
        'subtitle': 'Structured Data Mastery',
        'color1': '#7c2d12',  # Brown
        'color2': '#ea580c',  # Orange
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-wordpress.png',
        'title': 'WordPress\nHooks Guide',
        'subtitle': 'Plugin Development Essentials',
        'color1': '#1e3a3a',  # Teal dark
        'color2': '#20a39e',  # Teal light
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-ghost.png',
        'title': 'Ghost CMS\nGuide',
        'subtitle': 'Modern Publishing Platform',
        'color1': '#1a1a2e',  # Dark blue
        'color2': '#16213e',  # Darker blue
        'accent': '#e94560',  # Red
    },
    {
        'filename': 'blog-ionic.png',
        'title': 'Ionic\nFramework',
        'subtitle': 'Cross-Platform Mobile Apps',
        'color1': '#3880ff',  # Ionic blue
        'color2': '#5a9eff',  # Light blue
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-frameworks.png',
        'title': 'Frameworks\nComparison',
        'subtitle': 'Ionic vs Flutter vs React Native',
        'color1': '#2d3436',  # Dark gray
        'color2': '#636e72',  # Light gray
        'accent': '#00b894',  # Green
    },
    {
        'filename': 'blog-app-store.png',
        'title': 'App Store\nSubmission',
        'subtitle': 'Complete Checklist Guide',
        'color1': '#000000',  # Black
        'color2': '#2d2d2d',  # Dark gray
        'accent': '#34c759',  # Apple green
    },
    {
        'filename': 'blog-app-cost.png',
        'title': 'Ionic App\nDevelopment Cost',
        'subtitle': 'Budget Planning Guide',
        'color1': '#1e40af',  # Blue
        'color2': '#3b82f6',  # Light blue
        'accent': '#10b981',  # Green
    },
    {
        'filename': 'blog-ionic-laravel.png',
        'title': 'Ionic + Laravel\nIntegration',
        'subtitle': 'API Connection Guide',
        'color1': '#3880ff',  # Ionic blue
        'color2': '#ff2d55',  # Laravel red
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-capacitor.png',
        'title': 'Capacitor\nPlugins Guide',
        'subtitle': 'Native Features for Web Apps',
        'color1': '#119eff',  # Capacitor blue
        'color2': '#73b1ff',  # Light blue
        'accent': '#fbbf24',  # Amber
    },
    {
        'filename': 'blog-claude-ai.png',
        'title': 'Claude AI for\nDevelopers',
        'subtitle': 'Building with Claude API',
        'color1': '#0d0d0d',  # Black
        'color2': '#1a1a1a',  # Dark gray
        'accent': '#ff6b35',  # Orange
    },
    {
        'filename': 'blog-claude-code.png',
        'title': 'Claude Code\nCLI Guide',
        'subtitle': 'Command Line Development Tool',
        'color1': '#0d0d0d',  # Black
        'color2': '#1a1a1a',  # Dark gray
        'accent': '#4ecdc4',  # Teal
    },
    {
        'filename': 'blog-ai-comparison.png',
        'title': 'Claude vs\nChatGPT vs Gemini',
        'subtitle': 'AI Models Comparison 2026',
        'color1': '#111827',  # Gray
        'color2': '#374151',  # Light gray
        'accent': '#06b6d4',  # Cyan
    },
    {
        'filename': 'blog-claude-api.png',
        'title': 'Building with\nClaude API',
        'subtitle': 'Complete Integration Guide',
        'color1': '#0d0d0d',  # Black
        'color2': '#1a1a1a',  # Dark gray
        'accent': '#ff9500',  # Orange
    },
    {
        'filename': 'blog-openclaw.png',
        'title': 'OpenClaw\nAI',
        'subtitle': 'Advanced AI Framework',
        'color1': '#1f2937',  # Dark gray
        'color2': '#374151',  # Gray
        'accent': '#8b5cf6',  # Purple
    },
]

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_featured_image(config):
    """Create a single featured image"""
    width, height = 1200, 630

    # Create image with gradient background
    img = Image.new('RGB', (width, height), color=hex_to_rgb(config['color1']))
    draw = ImageDraw.Draw(img, 'RGBA')

    # Draw gradient overlay (simple color blend)
    color1 = hex_to_rgb(config['color1'])
    color2 = hex_to_rgb(config['color2'])

    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Add accent shapes
    accent = hex_to_rgb(config['accent'])

    # Top-left circle
    draw.ellipse([(-100, -100), (150, 150)], fill=accent)

    # Bottom-right circle
    draw.ellipse([(width - 150, height - 150), (width + 100, height + 100)], fill=accent)

    # Add semi-transparent rectangles
    draw.rectangle([0, 0, width, 100], fill=(0, 0, 0, 20))

    # Draw title text
    try:
        # Try to use a nice font, fall back to default if not available
        title_font = ImageFont.truetype("arial.ttf", 72)
        subtitle_font = ImageFont.truetype("arial.ttf", 32)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Title
    title_text = config['title']
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = 120

    draw.text((title_x, title_y), title_text, fill=(255, 255, 255), font=title_font)

    # Subtitle
    subtitle_text = config['subtitle']
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = 350

    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=accent, font=subtitle_font)

    # Add bottom accent bar
    draw.rectangle([0, height - 8, width, height], fill=accent)

    return img

# Generate all images
print("Generating 20 blog featured images...")
for i, config in enumerate(blog_images, 1):
    try:
        img = create_featured_image(config)
        filepath = os.path.join(images_dir, config['filename'])
        img.save(filepath, 'PNG', quality=95)
        print(f"[OK] {i}/20 - {config['filename']}")
    except Exception as e:
        print(f"[ERROR] {i}/20 - {config['filename']} - Error: {e}")

print(f"\nDone! All images saved to: {images_dir}")
print(f"Ready for use in og:image meta tags!")
