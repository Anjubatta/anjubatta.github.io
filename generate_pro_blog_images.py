#!/usr/bin/env python3
"""
Generate professional featured images for all 20 blog posts
Creates 1200x630px images with advanced graphics, icons, diagrams, charts
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

# Create images folder if it doesn't exist
images_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(images_dir, exist_ok=True)

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

class IconRenderer:
    @staticmethod
    def draw_sitemap(draw, x, y, size, color):
        """Draw sitemap/hierarchy icon"""
        c = hex_to_rgb(color)
        # Top box
        draw.rectangle([x + size//3, y, x + 2*size//3, y + size//4], outline=c, width=2, fill=(40,40,60))
        # Middle boxes
        draw.rectangle([x, y + size//2 - size//8, x + size//2 - 5, y + size//2 + size//8], outline=c, width=2, fill=(40,40,60))
        draw.rectangle([x + size//2 + 5, y + size//2 - size//8, x + size, y + size//2 + size//8], outline=c, width=2, fill=(40,40,60))
        # Lines
        draw.line([(x + size//2, y + size//4), (x + size//4, y + size//2 - size//8)], fill=c, width=2)
        draw.line([(x + size//2, y + size//4), (x + 3*size//4, y + size//2 - size//8)], fill=c, width=2)

    @staticmethod
    def draw_chart(draw, x, y, size, color, heights=[0.5, 0.7, 0.9, 0.6]):
        """Draw bar chart"""
        c = hex_to_rgb(color)
        bar_width = size // (len(heights) * 2)
        for i, height in enumerate(heights):
            bar_x = x + i * (bar_width + 10)
            bar_height = int(size * height)
            draw.rectangle([bar_x, y + size - bar_height, bar_x + bar_width, y + size], fill=c)

    @staticmethod
    def draw_speedometer(draw, x, y, size, color, value=0.75):
        """Draw speedometer/gauge"""
        c = hex_to_rgb(color)
        # Arc background
        draw.arc([x, y, x + size, y + size], 180, 360, fill=c, width=3)
        # Needle
        angle = 180 + (180 * value)
        rad = math.radians(angle)
        end_x = x + size//2 + (size//2 - 10) * math.cos(rad)
        end_y = y + size//2 + (size//2 - 10) * math.sin(rad)
        draw.line([(x + size//2, y + size//2), (end_x, end_y)], fill=c, width=3)
        # Center circle
        draw.ellipse([x + size//2 - 6, y + size//2 - 6, x + size//2 + 6, y + size//2 + 6], fill=c)

    @staticmethod
    def draw_network(draw, x, y, size, color):
        """Draw network/connection diagram"""
        c = hex_to_rgb(color)
        nodes = [(x + size//2, y), (x, y + size//2), (x + size, y + size//2), (x + size//2, y + size)]
        for node in nodes:
            draw.ellipse([node[0]-5, node[1]-5, node[0]+5, node[1]+5], fill=c)
        for i, n1 in enumerate(nodes):
            for n2 in nodes[i+1:]:
                draw.line([n1, n2], fill=c, width=1)

    @staticmethod
    def draw_rocket(draw, x, y, size, color):
        """Draw rocket icon"""
        c = hex_to_rgb(color)
        # Body
        draw.rectangle([x + size//3, y + size//4, x + 2*size//3, y + size], outline=c, width=2)
        # Head
        draw.ellipse([x + size//4, y, x + 3*size//4, y + size//4], outline=c, width=2)
        # Flame
        draw.polygon([(x + size//3, y + size), (x + 2*size//3, y + size), (x + size//2, y + size + size//3)], fill=c)

    @staticmethod
    def draw_shield(draw, x, y, size, color):
        """Draw security/shield icon"""
        c = hex_to_rgb(color)
        draw.rectangle([x, y, x + size, y + 2*size//3], outline=c, width=2)
        draw.arc([x, y + size//3, x + size, y + size], 0, 180, fill=c, width=2)

    @staticmethod
    def draw_code(draw, x, y, size, color):
        """Draw code brackets icon"""
        c = hex_to_rgb(color)
        # Left bracket
        draw.line([(x + size//3, y), (x, y), (x, y + size), (x + size//3, y + size)], fill=c, width=2)
        # Right bracket
        draw.line([(x + 2*size//3, y), (x + size, y), (x + size, y + size), (x + 2*size//3, y + size)], fill=c, width=2)

    @staticmethod
    def draw_database(draw, x, y, size, color):
        """Draw database icon"""
        c = hex_to_rgb(color)
        # Top ellipse
        draw.arc([x, y, x + size, y + size//3], 0, 180, fill=c, width=2)
        # Sides
        draw.line([(x, y + size//6), (x, y + 2*size//3)], fill=c, width=2)
        draw.line([(x + size, y + size//6), (x + size, y + 2*size//3)], fill=c, width=2)
        # Bottom ellipse
        draw.arc([x, y + size//2, x + size, y + size], 180, 360, fill=c, width=2)

    @staticmethod
    def draw_checkmark(draw, x, y, size, color):
        """Draw checkmark"""
        c = hex_to_rgb(color)
        draw.line([(x, y + size//2), (x + size//3, y + size)], fill=c, width=3)
        draw.line([(x + size//3, y + size), (x + size, y)], fill=c, width=3)

    @staticmethod
    def draw_phone(draw, x, y, size, color):
        """Draw phone/mobile icon"""
        c = hex_to_rgb(color)
        draw.rectangle([x, y, x + size, y + size], outline=c, width=2)
        draw.rectangle([x + 3, y + 3, x + size - 3, y + size - 8], outline=c, width=1)

    @staticmethod
    def draw_globe(draw, x, y, size, color):
        """Draw globe icon"""
        c = hex_to_rgb(color)
        draw.ellipse([x, y, x + size, y + size], outline=c, width=2)
        draw.line([(x, y + size//2), (x + size, y + size//2)], fill=c, width=1)
        draw.arc([x, y, x + size, y + size], 0, 360, fill=c, width=1)

    @staticmethod
    def draw_lightning(draw, x, y, size, color):
        """Draw lightning bolt"""
        c = hex_to_rgb(color)
        points = [(x + size//2, y), (x + size, y + size//2), (x + size//2, y + size//2), (x, y + size)]
        draw.polygon(points, fill=c)

    @staticmethod
    def draw_gear(draw, x, y, size, color):
        """Draw gear/settings icon"""
        c = hex_to_rgb(color)
        # Center circle
        r = size // 2
        draw.ellipse([x + r//2, y + r//2, x + r + r//2, y + r + r//2], outline=c, width=2)
        # Teeth
        for i in range(8):
            angle = (i * 360 // 8) * math.pi / 180
            x1 = x + r + (r + 5) * math.cos(angle)
            y1 = y + r + (r + 5) * math.sin(angle)
            x2 = x + r + r * math.cos(angle)
            y2 = y + r + r * math.sin(angle)
            draw.line([(x2, y2), (x1, y1)], fill=c, width=2)

    @staticmethod
    def draw_graph_line(draw, x, y, size, color, points_ratio=[0.2, 0.5, 0.3, 0.7, 0.6]):
        """Draw line graph"""
        c = hex_to_rgb(color)
        step = size // (len(points_ratio) - 1)
        coords = [(x + i * step, y + size - int(size * p)) for i, p in enumerate(points_ratio)]
        draw.line(coords, fill=c, width=2)
        for cx, cy in coords:
            draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill=c)

# Blog configurations with rich visual elements
blog_images = [
    {
        'filename': 'blog-xml-sitemap.png',
        'title': 'XML Sitemap Strategy 2026',
        'color1': '#0f172a',
        'color2': '#1e3a8a',
        'accent': '#06b6d4',
        'icon_type': 'sitemap',
        'content': ['Dynamic Generation', 'Crawl Budget Optimization', 'Priority Algorithms', 'Image Sitemaps'],
        'metrics': ['+37%', '+23%', '+18%'],
        'metric_labels': ['Faster Index', 'Better Crawl', 'Visibility'],
        'has_chart': True
    },
    {
        'filename': 'blog-seo-audit.png',
        'title': 'Technical SEO Audit Checklist',
        'color1': '#065f46',
        'color2': '#10b981',
        'accent': '#34d399',
        'icon_type': 'chart',
        'content': ['Site Speed', 'Mobile Check', 'Structured Data', 'Core Web Vitals'],
        'metrics': ['50+', '100%', 'Real-time'],
        'metric_labels': ['Checkpoints', 'Analysis', 'Monitoring'],
        'has_chart': True
    },
    {
        'filename': 'blog-nextjs-seo.png',
        'title': 'Next.js SEO Architecture',
        'color1': '#0f0f0f',
        'color2': '#1a1a1a',
        'accent': '#fbbf24',
        'icon_type': 'code',
        'content': ['SSR & Static', 'Dynamic Routes', 'Meta Tags', 'Image Optimization'],
        'metrics': ['3x Faster', '99/100', 'Optimal'],
        'metric_labels': ['Loading', 'Lighthouse', 'Performance'],
        'has_chart': True
    },
    {
        'filename': 'blog-aeo-geo.png',
        'title': 'AEO & GEO Optimization',
        'color1': '#3f0f0f',
        'color2': '#7c2d12',
        'accent': '#fb923c',
        'icon_type': 'globe',
        'content': ['AI-Enhanced', 'Geographic', 'Local Intent', 'Context Aware'],
        'metrics': ['+45%', '2.5x', 'Advanced'],
        'metric_labels': ['Local CTR', 'Relevance', 'Targeting'],
        'has_chart': True
    },
    {
        'filename': 'blog-cloudflare.png',
        'title': 'Cloudflare Optimization Guide',
        'color1': '#0c4a6e',
        'color2': '#0369a1',
        'accent': '#fbbf24',
        'icon_type': 'speedometer',
        'content': ['CDN Speed', 'DDoS Shield', 'Page Rules', 'Analytics'],
        'metrics': ['+60%', '99.9%', 'Global'],
        'metric_labels': ['CDN Speed', 'Uptime', 'Coverage'],
        'has_chart': True
    },
    {
        'filename': 'blog-ai-agents.png',
        'title': 'AI Agent Architecture',
        'color1': '#0f172a',
        'color2': '#1e293b',
        'accent': '#06b6d4',
        'icon_type': 'network',
        'content': ['Agent Design', 'Tool Integration', 'Decision Trees', 'Learning'],
        'metrics': ['Autonomous', 'Self-Improving', 'Scalable'],
        'metric_labels': ['Systems', 'AI Models', 'Architecture'],
        'has_chart': True
    },
    {
        'filename': 'blog-schema.png',
        'title': 'Schema Engineering Guide',
        'color1': '#1f1f1f',
        'color2': '#2d2d2d',
        'accent': '#f97316',
        'icon_type': 'database',
        'content': ['Structured Data', 'Rich Snippets', 'JSON-LD', 'Validation'],
        'metrics': ['Rich Results', '40%', 'Instant'],
        'metric_labels': ['Enabled', 'CTR Boost', 'Processing'],
        'has_chart': True
    },
    {
        'filename': 'blog-wordpress.png',
        'title': 'WordPress Hooks Guide',
        'color1': '#001a26',
        'color2': '#003d4d',
        'accent': '#20b2aa',
        'icon_type': 'code',
        'content': ['Action Hooks', 'Filter Hooks', 'Plugins', 'Best Practices'],
        'metrics': ['40+ Hooks', 'Custom Dev', 'Extensible'],
        'metric_labels': ['Types', 'Friendly', 'Framework'],
        'has_chart': True
    },
    {
        'filename': 'blog-ghost.png',
        'title': 'Ghost CMS Publishing Guide',
        'color1': '#0a0a0a',
        'color2': '#1a1a1a',
        'accent': '#e94560',
        'icon_type': 'rocket',
        'content': ['Membership', 'Email', 'Management', 'Analytics'],
        'metrics': ['Fast', 'Monetized', 'Built-in'],
        'metric_labels': ['Publishing', 'Platform', 'Tracking'],
        'has_chart': True
    },
    {
        'filename': 'blog-ionic.png',
        'title': 'Ionic Framework Guide',
        'color1': '#1a3a5c',
        'color2': '#3880ff',
        'accent': '#fbbf24',
        'icon_type': 'phone',
        'content': ['Cross-Platform', 'Native Comp', 'Performance', 'Production'],
        'metrics': ['1 Codebase', '50+', 'App Ready'],
        'metric_labels': ['All Platforms', 'Components', 'Deployment'],
        'has_chart': True
    },
    {
        'filename': 'blog-frameworks.png',
        'title': 'Frameworks Comparison',
        'color1': '#0f0f0f',
        'color2': '#2d2d2d',
        'accent': '#10b981',
        'icon_type': 'chart',
        'content': ['Ionic vs', 'Flutter vs', 'React Native', 'Comparison'],
        'metrics': ['3 Frameworks', 'Side-by-side', 'Analysis'],
        'metric_labels': ['Compared', 'Breakdown', 'Guide'],
        'has_chart': True
    },
    {
        'filename': 'blog-app-store.png',
        'title': 'App Store Submission Checklist',
        'color1': '#000000',
        'color2': '#1a1a1a',
        'accent': '#34c759',
        'icon_type': 'checkmark',
        'content': ['iOS Steps', 'Android', 'Guidelines', 'Marketing'],
        'metrics': ['50+ Items', 'Complete', 'Guide'],
        'metric_labels': ['Checklist', 'Process', 'Included'],
        'has_chart': True
    },
    {
        'filename': 'blog-app-cost.png',
        'title': 'Ionic App Development Cost',
        'color1': '#0f1419',
        'color2': '#1e3a5f',
        'accent': '#10b981',
        'icon_type': 'graph_line',
        'content': ['Cost Estimation', 'Resource Plan', 'Time Breakdown', 'ROI'],
        'metrics': ['Budget', 'Planning', 'Analysis'],
        'metric_labels': ['Calculator', 'Tools', 'Framework'],
        'has_chart': True
    },
    {
        'filename': 'blog-ionic-laravel.png',
        'title': 'Ionic + Laravel Integration',
        'color1': '#1a2333',
        'color2': '#3880ff',
        'accent': '#ff2d55',
        'icon_type': 'network',
        'content': ['API Setup', 'Auth Token', 'Sync Data', 'Real-time'],
        'metrics': ['REST API', 'Secure', 'Live Updates'],
        'metric_labels': ['Endpoints', 'Auth', 'Websockets'],
        'has_chart': True
    },
    {
        'filename': 'blog-capacitor.png',
        'title': 'Capacitor Plugins Guide',
        'color1': '#0a2540',
        'color2': '#119eff',
        'accent': '#fbbf24',
        'icon_type': 'rocket',
        'content': ['Native APIs', 'Device Access', 'Plugins', 'Bridge'],
        'metrics': ['50+ Plugins', 'Native Feat', 'Cross-Plat'],
        'metric_labels': ['Available', 'Access', 'Support'],
        'has_chart': True
    },
    {
        'filename': 'blog-claude-ai.png',
        'title': 'Claude AI for Developers',
        'color1': '#0d0d0d',
        'color2': '#1a1a1a',
        'accent': '#ff6b35',
        'icon_type': 'brain',
        'content': ['API Access', 'Prompting', 'Multimodal', 'Production'],
        'metrics': ['100K+', 'Advanced', 'Ready'],
        'metric_labels': ['Token Limit', 'Capabilities', 'Deployment'],
        'has_chart': True
    },
    {
        'filename': 'blog-claude-code.png',
        'title': 'Claude Code CLI Tool Guide',
        'color1': '#0d0d0d',
        'color2': '#1a1a1a',
        'accent': '#4ecdc4',
        'icon_type': 'code',
        'content': ['Code Gen', 'Local Dev', 'Terminal', 'SSH Ready'],
        'metrics': ['Real-time', 'Integrated', 'Productive'],
        'metric_labels': ['Generation', 'Development', 'Workflow'],
        'has_chart': True
    },
    {
        'filename': 'blog-ai-comparison.png',
        'title': 'Claude vs ChatGPT vs Gemini',
        'color1': '#111827',
        'color2': '#374151',
        'accent': '#06b6d4',
        'icon_type': 'chart',
        'content': ['Capability', 'Speed', 'Cost', 'Use Cases'],
        'metrics': ['3 Models', 'Detailed', 'Comparison'],
        'metric_labels': ['Compared', 'Analysis', 'Guide'],
        'has_chart': True
    },
    {
        'filename': 'blog-claude-api.png',
        'title': 'Building with Claude API',
        'color1': '#0d0d0d',
        'color2': '#1a1a1a',
        'accent': '#ff9500',
        'icon_type': 'code',
        'content': ['Endpoints', 'Auth', 'Error Handle', 'Examples'],
        'metrics': ['Complete', 'Documented', 'SDKs'],
        'metric_labels': ['API Docs', 'Reference', 'Available'],
        'has_chart': True
    },
    {
        'filename': 'blog-openclaw.png',
        'title': 'OpenClaw AI Framework',
        'color1': '#1f2937',
        'color2': '#374151',
        'accent': '#8b5cf6',
        'icon_type': 'network',
        'content': ['Orchestration', 'Workflows', 'Multi-Agent', 'Enterprise'],
        'metrics': ['Advanced', 'Scalable', 'Enterprise'],
        'metric_labels': ['Features', 'Architecture', 'Ready'],
        'has_chart': True
    },
]

def create_professional_image(config):
    """Create professional featured image with advanced graphics"""
    width, height = 1200, 630

    # Create base image
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

    # Add decorative circles with blur effect
    draw.ellipse([(width - 250, -100), (width + 150, 200)], fill=accent + (60,))
    draw.ellipse([(-150, height - 200), (150, height + 100)], fill=accent + (60,))

    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 56)
        content_font = ImageFont.truetype("arial.ttf", 18)
        metric_font = ImageFont.truetype("arial.ttf", 28)
        small_font = ImageFont.truetype("arial.ttf", 13)
    except:
        title_font = content_font = metric_font = small_font = ImageFont.load_default()

    # Draw title
    title_text = config['title']
    draw.text((50, 35), title_text, fill=(255, 255, 255), font=title_font)

    # Draw large icon (left side)
    icon_x, icon_y, icon_size = 60, 280, 120
    icon_type = config.get('icon_type', 'chart')

    try:
        if icon_type == 'sitemap':
            IconRenderer.draw_sitemap(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'chart':
            IconRenderer.draw_chart(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'speedometer':
            IconRenderer.draw_speedometer(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'network':
            IconRenderer.draw_network(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'rocket':
            IconRenderer.draw_rocket(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'shield':
            IconRenderer.draw_shield(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'code':
            IconRenderer.draw_code(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'database':
            IconRenderer.draw_database(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'checkmark':
            IconRenderer.draw_checkmark(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'phone':
            IconRenderer.draw_phone(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'globe':
            IconRenderer.draw_globe(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'lightning':
            IconRenderer.draw_lightning(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'gear':
            IconRenderer.draw_gear(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'graph_line':
            IconRenderer.draw_graph_line(draw, icon_x, icon_y, icon_size, config['accent'])
        elif icon_type == 'brain':
            # Simple brain icon
            draw.ellipse([icon_x, icon_y, icon_x + icon_size, icon_y + icon_size], outline=accent, width=2)
            draw.line([(icon_x + icon_size//2, icon_y), (icon_x + icon_size//2, icon_y + icon_size)], fill=accent, width=2)
    except:
        pass

    # Draw content items (middle/right side)
    content_x = 280
    content_y = 160
    item_spacing = 100

    for i, item in enumerate(config['content'][:4]):
        box_y = content_y + (i // 2) * 140
        box_x = content_x + (i % 2) * 410

        # Draw content box with border
        draw.rectangle([box_x, box_y, box_x + 390, box_y + 110], outline=accent, width=2, fill=(30, 30, 40))

        # Small icon in box
        small_icon_x = box_x + 15
        if i == 0:
            IconRenderer.draw_checkmark(draw, small_icon_x, box_y + 15, 25, config['accent'])
        elif i == 1:
            IconRenderer.draw_chart(draw, small_icon_x, box_y + 15, 25, config['accent'])
        elif i == 2:
            IconRenderer.draw_gear(draw, small_icon_x, box_y + 15, 25, config['accent'])
        elif i == 3:
            IconRenderer.draw_rocket(draw, small_icon_x, box_y + 15, 25, config['accent'])

        # Item text
        draw.text((box_x + 55, box_y + 25), item, fill=(220, 220, 220), font=content_font)

    # Draw metrics (bottom right)
    metrics_x = 280
    metrics_y = 480

    for i, (metric, label) in enumerate(zip(config['metrics'], config['metric_labels'])):
        metric_box_x = metrics_x + (i * 300)

        # Metric box
        draw.rectangle([metric_box_x, metrics_y, metric_box_x + 280, metrics_y + 120], outline=accent, width=2, fill=(30, 30, 40))

        # Metric value
        draw.text((metric_box_x + 20, metrics_y + 20), metric, fill=accent, font=metric_font)

        # Metric label
        draw.text((metric_box_x + 20, metrics_y + 65), label, fill=(200, 200, 200), font=small_font)

    # Add bottom accent bar
    draw.rectangle([0, height - 12, width, height], fill=accent)

    return img

# Generate all images
print("Generating 20 professional blog featured images with icons & graphs...")
for i, config in enumerate(blog_images, 1):
    try:
        img = create_professional_image(config)
        filepath = os.path.join(images_dir, config['filename'])
        img.save(filepath, 'PNG', quality=95)
        print(f"[OK] {i}/20 - {config['filename']}")
    except Exception as e:
        print(f"[ERROR] {i}/20 - {config['filename']} - {str(e)[:50]}")

print(f"\nDone! Professional images with icons & graphs!")
