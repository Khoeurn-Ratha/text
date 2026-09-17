from flask import Flask, render_template_string, jsonify, url_for

app = Flask(__name__)

# Configurable Social Media & Trading Details
CONFIG = {
    "trader_name": "THA.FX-MSNR",
    "primary_asset": "XAUUSD (Gold)",
    "market_style": "Smart Money Concepts & Technical Analysis",
    "bio": "Specializing in technical market analysis, high-probability execution setups, and systematic risk management.",
    "profile_video": "photo_2026-09-17_14-06-03.mp4", 
    "social_links": {
        "telegram": "https://t.me/k_Tha1",
        "tiktok": "https://www.tiktok.com/@carrot..6?is_from_webapp=1&sender_device=pc",
        "youtube": "https://youtube.com/@your_channel",
        "facebook": "https://www.facebook.com/GenrotZ/"
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ config.trader_name }} | THA-MSNR </title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #030712;
            --card-bg: rgba(17, 24, 39, 0.85);
            --card-border: rgba(255, 255, 255, 0.12);
            --card-border-hover: #f59e0b;
            --accent-gold: #fbbf24;
            --accent-gold-glow: rgba(251, 191, 36, 0.35);
            --accent-green: #10b981;
            --accent-green-glow: rgba(16, 185, 129, 0.4);
            --text-main: #f9fafb;
            --text-muted: #9ca3af;
            --text-sub: #d1d5db;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            display: flex;
            justify-content: center;
            min-height: 100vh;
            padding: 40px 20px;
            position: relative;
            overflow-x: hidden;
        }

        #bg-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            pointer-events: none;
        }

        .bg-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
            background-size: 35px 35px;
            z-index: -1;
            pointer-events: none;
        }

        .glow-orb {
            position: fixed;
            width: 400px;
            height: 400px;
            border-radius: 50%;
            filter: blur(140px);
            z-index: -1;
            opacity: 0.35;
            pointer-events: none;
        }

        .glow-gold {
            top: -80px;
            left: -80px;
            background: #d97706;
        }

        .glow-green {
            bottom: -80px;
            right: -80px;
            background: #059669;
        }

        .container {
            max-width: 820px;
            width: 100%;
            z-index: 1;
        }

        .hero, .card, .social-section {
            background: var(--card-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--card-border);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }

        .hero {
            text-align: center;
            margin-bottom: 24px;
            padding: 40px 24px;
            border-radius: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }

        .hero:hover {
            border-color: rgba(251, 191, 36, 0.3);
            box-shadow: 0 12px 35px rgba(251, 191, 36, 0.15);
        }

        /* Profile Video Container - STATIC (No Hover) */
        .profile-video-wrapper {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            overflow: hidden;
            margin-bottom: 20px;
            border: 3px solid var(--accent-gold);
            box-shadow: 0 0 20px var(--accent-gold-glow);
            background: #000;
            position: relative;
            -webkit-mask-image: -webkit-radial-gradient(white, black);
            cursor: default;
        }

        .profile-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* Badge */
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(251, 191, 36, 0.12);
            color: var(--accent-gold);
            border: 1px solid rgba(251, 191, 36, 0.4);
            font-size: 0.78rem;
            font-weight: 800;
            padding: 5px 14px;
            border-radius: 20px;
            margin-bottom: 16px;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            box-shadow: 0 0 12px var(--accent-gold-glow);
            transition: transform 0.25s ease, background-color 0.25s ease, box-shadow 0.25s ease;
            cursor: default;
        }

        .badge:hover {
            transform: translateY(-2px);
            background: rgba(251, 191, 36, 0.25);
            box-shadow: 0 0 20px var(--accent-gold-glow);
        }

        h1 {
            font-size: 2.6rem;
            font-weight: 800;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #ffffff 30%, var(--accent-gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            transition: filter 0.3s ease;
        }

        h1:hover {
            filter: drop-shadow(0 0 10px rgba(251, 191, 36, 0.4));
        }

        .bio {
            color: var(--text-sub);
            font-size: 1.05rem;
            line-height: 1.6;
            max-width: 620px;
            margin: 0 auto 24px;
        }

        /* Status Card */
        .status-card {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(31, 41, 55, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 20px;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--text-main);
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
            cursor: pointer;
        }

        .status-card:hover {
            transform: translateY(-2px) scale(1.03);
            border-color: var(--accent-green);
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        }

        .pulse-dot {
            width: 10px;
            height: 10px;
            background-color: var(--accent-green);
            border-radius: 50%;
            box-shadow: 0 0 12px var(--accent-green);
            animation: pulse 1.8s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.9); box-shadow: 0 0 0 0 var(--accent-green-glow); }
            70% { transform: scale(1.1); box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        .trading-highlights {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 20px;
            margin-bottom: 24px;
        }

        .card {
            padding: 26px 20px;
            border-radius: 16px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .card:hover {
            transform: translateY(-8px);
            background: rgba(31, 41, 55, 0.95);
            border-color: var(--card-border-hover);
            box-shadow: 0 14px 30px rgba(0, 0, 0, 0.6), 0 0 20px var(--accent-gold-glow);
        }

        .card:hover::before {
            opacity: 1;
        }

        .card-icon {
            font-size: 2rem;
            color: var(--accent-gold);
            margin-bottom: 14px;
            filter: drop-shadow(0 0 8px var(--accent-gold-glow));
            transition: transform 0.3s ease, filter 0.3s ease;
        }

        .card:hover .card-icon {
            transform: scale(1.18) rotate(-5deg);
            filter: drop-shadow(0 0 14px rgba(251, 191, 36, 0.8));
        }

        .card h3 {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 8px;
            transition: color 0.3s ease;
        }

        .card:hover h3 {
            color: var(--accent-gold);
        }

        .card p {
            color: var(--text-muted);
            font-size: 0.92rem;
            line-height: 1.4;
            transition: color 0.3s ease;
        }

        .card:hover p {
            color: var(--text-sub);
        }

        .social-section {
            border-radius: 20px;
            padding: 32px 24px;
            text-align: center;
        }

        .social-section h2 {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 8px;
        }

        .social-section p {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 26px;
        }

        .social-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
        }

        .social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 14px 20px;
            border-radius: 12px;
            text-decoration: none;
            color: #ffffff;
            font-weight: 700;
            font-size: 0.95rem;
            border: 1px solid rgba(255, 255, 255, 0.15);
            position: relative;
            overflow: hidden;
            transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.25s ease, filter 0.25s ease;
        }

        .social-btn::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -60%;
            width: 40%;
            height: 200%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), transparent);
            transform: rotate(25deg);
            transition: left 0.6s ease;
        }

        .social-btn:hover::after {
            left: 130%;
        }

        .social-btn:hover {
            transform: translateY(-4px) scale(1.04);
            filter: brightness(1.18);
        }

        .social-btn i {
            transition: transform 0.25s ease;
        }

        .social-btn:hover i {
            transform: scale(1.25) rotate(-8deg);
        }

        .telegram { 
            background: linear-gradient(135deg, #229ed9 0%, #0088cc 100%);
            box-shadow: 0 4px 15px rgba(0, 136, 204, 0.35);
        }
        .telegram:hover {
            box-shadow: 0 8px 25px rgba(0, 136, 204, 0.6);
        }

        .tiktok { 
            background: linear-gradient(135deg, #000000 0%, #25f4ee 50%, #fe2c55 100%);
            box-shadow: 0 4px 15px rgba(254, 44, 85, 0.35);
        }
        .tiktok:hover {
            box-shadow: 0 8px 25px rgba(254, 44, 85, 0.6);
        }

        .youtube { 
            background: linear-gradient(135deg, #ff0000 0%, #dc2626 100%);
            box-shadow: 0 4px 15px rgba(239, 68, 68, 0.35);
        }
        .youtube:hover {
            box-shadow: 0 8px 25px rgba(239, 68, 68, 0.6);
        }

        .facebook { 
            background: linear-gradient(135deg, #1877f2 0%, #1d4ed8 100%);
            box-shadow: 0 4px 15px rgba(24, 119, 242, 0.35);
        }
        .facebook:hover {
            box-shadow: 0 8px 25px rgba(24, 119, 242, 0.6);
        }

        footer {
            text-align: center;
            margin-top: 32px;
            color: var(--text-muted);
            font-size: 0.85rem;
        }
    </style>
</head>
<body>
    <canvas id="bg-canvas"></canvas>
    <div class="bg-grid"></div>
    <div class="glow-orb glow-gold"></div>
    <div class="glow-orb glow-green"></div>

    <div class="container">
        <!-- Hero Section -->
        <header class="hero">
            <!-- Profile Video Circle (Static) -->
            <div class="profile-video-wrapper">
                <video class="profile-video" autoplay loop muted playsinline preload="auto">
                    <source src="{{ url_for('static', filename=config.profile_video) }}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>

            <div class="badge"><i class="fa-solid fa-chart-line"></i> Welcome to my Website</div>
            <h1>{{ config.trader_name }}</h1>
            <p class="bio">{{ config.bio }}</p>
            
            <div id="live-status" class="status-card">
                <span class="pulse-dot"></span>
                <span id="status-text">Loading market session...</span>
            </div>
        </header>

        <!-- Highlights Section -->
        <section class="trading-highlights">
            <div class="card">
                <i class="fa-solid fa-coins card-icon"></i>
                <h3>Main Asset</h3>
                <p>{{ config.primary_asset }}</p>
            </div>
            <div class="card">
                <i class="fa-solid fa-brain card-icon"></i>
                <h3>Strategy</h3>
                <p>{{ config.market_style }}</p>
            </div>
            <div class="card">
                <i class="fa-solid fa-shield-halved card-icon"></i>
                <h3>Risk Management</h3>
                <p>Strict Risk-to-Reward & Capital Protection</p>
            </div>
        </section>

        <!-- Social Media Links Section -->
        <section class="social-section">
            <h2>MY context </h2>
            <p>Join the community for chart breakdowns, updates, and trade ideas.</p>

            <div class="social-grid">
                <a href="{{ config.social_links.telegram }}" target="_blank" class="social-btn telegram">
                    <i class="fa-brands fa-telegram"></i>
                    <span>Telegram Channel</span>
                </a>
                <a href="{{ config.social_links.tiktok }}" target="_blank" class="social-btn tiktok">
                    <i class="fa-brands fa-tiktok"></i>
                    <span>TikTok</span>
                </a>
                <a href="{{ config.social_links.youtube }}" target="_blank" class="social-btn youtube">
                    <i class="fa-brands fa-youtube"></i>
                    <span>YouTube</span>
                </a>
                <a href="{{ config.social_links.facebook }}" target="_blank" class="social-btn facebook">
                    <i class="fa-brands fa-facebook"></i>
                    <span>Facebook</span>
                </a>
            </div>
        </section>

        <footer>
            <p>&copy; 2026 {{ config.trader_name }}. All rights reserved.</p>
        </footer>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const profileVid = document.querySelector('.profile-video');
            if (profileVid) {
                profileVid.play().catch(error => {
                    console.log("Autoplay prevented or video load failed:", error);
                });
            }

            fetch('/api/status')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('status-text').textContent = `${data.session} | ${data.notice}`;
                })
                .catch(() => {
                    document.getElementById('status-text').textContent = "Community active on Telegram";
                });

            initBackgroundChart();
        });

        function initBackgroundChart() {
            const canvas = document.getElementById('bg-canvas');
            const ctx = canvas.getContext('2d');

            function resize() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            const points = [];
            const count = 45;
            const step = canvas.width / (count - 1);

            for (let i = 0; i < count; i++) {
                points.push({
                    x: i * step,
                    y: canvas.height * 0.5 + (Math.random() - 0.5) * 160,
                    targetY: canvas.height * 0.5 + (Math.random() - 0.5) * 160,
                    speed: 0.01 + Math.random() * 0.02
                });
            }

            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                ctx.beginPath();
                ctx.moveTo(0, canvas.height);

                for (let i = 0; i < points.length; i++) {
                    const pt = points[i];
                    pt.y += (pt.targetY - pt.y) * pt.speed;
                    if (Math.abs(pt.targetY - pt.y) < 2) {
                        pt.targetY = canvas.height * 0.45 + (Math.random() - 0.5) * 220;
                    }
                    if (i === 0) {
                        ctx.lineTo(pt.x, pt.y);
                    } else {
                        const prev = points[i - 1];
                        const cx = (prev.x + pt.x) / 2;
                        const cy = (prev.y + pt.y) / 2;
                        ctx.quadraticCurveTo(prev.x, prev.y, cx, cy);
                    }
                }

                ctx.lineTo(canvas.width, canvas.height);
                ctx.closePath();

                const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
                gradient.addColorStop(0, 'rgba(251, 191, 36, 0.18)');
                gradient.addColorStop(1, 'rgba(3, 7, 18, 0)');
                ctx.fillStyle = gradient;
                ctx.fill();

                ctx.lineWidth = 2.5;
                ctx.strokeStyle = 'rgba(251, 191, 36, 0.5)';
                ctx.stroke();

                requestAnimationFrame(animate);
            }

            animate();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, config=CONFIG)

@app.route('/api/status')
def status():
    return jsonify({
        "status": "active",
        "session": "London / New York Session",
        "notice": "Daily updates on Telegram"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
