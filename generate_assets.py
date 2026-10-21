import os
import random

ASSETS_DIR = r"D:\AndroidStudioProjects\Phnem\assets"
BASE64_PATH = os.path.join(ASSETS_DIR, "avatar-base64.txt")

with open(BASE64_PATH, "r", encoding="utf-8") as f:
    avatar_b64 = f.read().strip()

# Common styles & defs helper
def get_common_defs(clip_avatar=False):
    avatar_clip_def = """
    <!-- Avatar Circular Clip -->
    <clipPath id="avatarClip">
      <circle cx="85" cy="100" r="48"/>
    </clipPath>
    """ if clip_avatar else ""

    return f"""
  <defs>
    <!-- Card Border Gradient -->
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="35%" stop-color="#2563EB" stop-opacity="0.2"/>
      <stop offset="70%" stop-color="#8B5CF6" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#06B6D4" stop-opacity="0.4"/>
    </linearGradient>

    <!-- Inner Card Border -->
    <linearGradient id="innerBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.25"/>
    </linearGradient>

    <!-- Background Radial Glows -->
    <radialGradient id="leftGlow" cx="15%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="#0284C7" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="rightGlow" cx="88%" cy="70%" r="45%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <!-- Glow Filter -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    {avatar_clip_def}
  </defs>

  <style>
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: "JetBrains Mono", Consolas, "Fira Code", monospace; }}
  </style>
"""

# 1. HEADER SVG
header_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="880" height="200" fill="none">
{get_common_defs(clip_avatar=True)}

  <!-- Outer Glass Frame -->
  <rect x="1" y="1" width="878" height="198" rx="22" fill="#070A12" stroke="url(#cardBorder)" stroke-width="1.5"/>
  <rect x="1" y="1" width="878" height="198" rx="22" fill="url(#leftGlow)"/>
  <rect x="1" y="1" width="878" height="198" rx="22" fill="url(#rightGlow)"/>

  <!-- Inner Frame -->
  <rect x="16" y="16" width="848" height="168" rx="16" fill="#0A0E1A" fill-opacity="0.6" stroke="url(#innerBorder)" stroke-width="1"/>

  <!-- Avatar Circle with Glow -->
  <circle cx="85" cy="100" r="50" stroke="#38BDF8" stroke-width="2.5" fill="#000000" filter="url(#neonGlow)"/>
  <image href="data:image/png;base64,{avatar_b64}" x="37" y="52" width="96" height="96" clip-path="url(#avatarClip)"/>
  <circle cx="85" cy="100" r="48" stroke="rgba(255,255,255,0.2)" stroke-width="1" fill="none"/>

  <!-- Curved Accent Line Above Handle -->
  <path d="M 160 55 Q 260 38 380 65" stroke="rgba(148, 163, 184, 0.28)" stroke-width="1.5" fill="none"/>

  <!-- User Handle -->
  <text x="160" y="60" class="font-mono" font-size="13" font-weight="600" fill="#94A3B8" letter-spacing="1">@phnem</text>

  <!-- Name -->
  <text x="160" y="98" class="font-sans" font-size="34" font-weight="800" fill="#FFFFFF" letter-spacing="-0.5">levg</text>

  <!-- Tagline -->
  <text x="160" y="124" class="font-sans" font-size="13.5" font-weight="400" fill="#94A3B8">Building with C on GitHub.</text>

  <!-- Skill Badges -->
  <g transform="translate(160, 140)">
    <!-- Badge: C -->
    <g transform="translate(0, 0)">
      <rect width="68" height="25" rx="12.5" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.16)" stroke-width="1"/>
      <text x="34" y="16.5" class="font-sans" font-size="11.5" font-weight="700" fill="#E2E8F0" text-anchor="middle">C</text>
    </g>

    <!-- Badge: C++ -->
    <g transform="translate(76, 0)">
      <rect width="76" height="25" rx="12.5" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.16)" stroke-width="1"/>
      <text x="38" y="16.5" class="font-sans" font-size="11.5" font-weight="700" fill="#E2E8F0" text-anchor="middle">C++</text>
    </g>

    <!-- Badge: Assembly -->
    <g transform="translate(160, 0)">
      <rect width="94" height="25" rx="12.5" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.16)" stroke-width="1"/>
      <text x="47" y="16.5" class="font-sans" font-size="11.5" font-weight="700" fill="#E2E8F0" text-anchor="middle">Assembly</text>
    </g>

    <!-- Badge: Kotlin -->
    <g transform="translate(262, 0)">
      <rect width="82" height="25" rx="12.5" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.16)" stroke-width="1"/>
      <text x="41" y="16.5" class="font-sans" font-size="11.5" font-weight="700" fill="#E2E8F0" text-anchor="middle">Kotlin</text>
    </g>
  </g>

  <!-- Right Side Stat: Total Stars -->
  <g transform="translate(740, 100)">
    <circle cx="0" cy="0" r="48" fill="#38BDF8" fill-opacity="0.06"/>
    <text x="0" y="6" class="font-sans" font-size="44" font-weight="900" fill="#38BDF8" text-anchor="middle" letter-spacing="-1">66</text>
    <text x="0" y="28" class="font-sans" font-size="10.5" font-weight="700" fill="#64748B" text-anchor="middle" letter-spacing="1.5">TOTAL STARS</text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "header.svg"), "w", encoding="utf-8") as f:
    f.write(header_svg)


# 2. CONTRIBUTION ACTIVITY SVG
# Generate contribution grid mirroring the exact visual in screenshot
random.seed(42)
cols = 50
rows = 7
sq_size = 11
gap = 4.5
start_x = 42
start_y = 82

colors = [
    "#0B132B", # empty / dark
    "#0B132B",
    "#0E2145", # very light
    "#1D4ED8", # mid blue
    "#0284C7", # brighter blue
    "#38BDF8", # neon cyan
    "#60A5FA"  # bright blue
]

squares_svg = []
for c in range(cols):
    for r in range(rows):
        # bias density: active towards the right side (recent activity)
        prob = (c / cols) ** 1.3
        if random.random() < 0.25 + prob * 0.55:
            color = random.choice(colors[2:])
        else:
            color = random.choice(colors[:2])
            
        x = start_x + c * (sq_size + gap)
        y = start_y + r * (sq_size + gap)
        opacity = 0.9 if color in ("#38BDF8", "#60A5FA", "#0284C7") else 0.4
        squares_svg.append(f'<rect x="{x}" y="{y}" width="{sq_size}" height="{sq_size}" rx="2.5" fill="{color}" fill-opacity="{opacity}"/>')

contribution_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="880" height="200" fill="none">
{get_common_defs()}

  <!-- Outer Glass Frame -->
  <rect x="1" y="1" width="878" height="198" rx="22" fill="#070A12" stroke="url(#cardBorder)" stroke-width="1.5"/>
  <rect x="1" y="1" width="878" height="198" rx="22" fill="url(#leftGlow)"/>
  <rect x="1" y="1" width="878" height="198" rx="22" fill="url(#rightGlow)"/>

  <!-- Inner Frame -->
  <rect x="16" y="16" width="848" height="168" rx="16" fill="#0A0E1A" fill-opacity="0.6" stroke="url(#innerBorder)" stroke-width="1"/>

  <!-- Title & Subtitle -->
  <text x="42" y="48" class="font-sans" font-size="18" font-weight="700" fill="#FFFFFF">Contribution Activity</text>
  <text x="42" y="66" class="font-sans" font-size="12" font-weight="400" fill="#94A3B8">831 contributions in the last year</text>

  <!-- Legend -->
  <g transform="translate(730, 48)">
    <text x="-8" y="9" class="font-sans" font-size="10.5" font-weight="500" fill="#64748B" text-anchor="end">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" fill="#0B132B" fill-opacity="0.6"/>
    <rect x="14" y="0" width="10" height="10" rx="2" fill="#1D4ED8"/>
    <rect x="28" y="0" width="10" height="10" rx="2" fill="#0284C7"/>
    <rect x="42" y="0" width="10" height="10" rx="2" fill="#38BDF8"/>
    <text x="60" y="9" class="font-sans" font-size="10.5" font-weight="500" fill="#64748B">More</text>
  </g>

  <!-- Matrix Grid -->
  {''.join(squares_svg)}
</svg>'''

with open(os.path.join(ASSETS_DIR, "contribution-activity.svg"), "w", encoding="utf-8") as f:
    f.write(contribution_svg)


# 3. PROFILE SIGNAL SVG
profile_signal_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 200" width="880" height="200" fill="none">
{get_common_defs()}

  <!-- Outer Glass Frame -->
  <rect x="1" y="1" width="878" height="198" rx="22" fill="#070A12" stroke="url(#cardBorder)" stroke-width="1.5"/>
  <rect x="1" y="1" width="878" height="198" rx="22" fill="url(#leftGlow)"/>
  <rect x="1" y="1" width="878" height="198" rx="22" fill="url(#rightGlow)"/>

  <!-- Inner Frame -->
  <rect x="16" y="16" width="848" height="168" rx="16" fill="#0A0E1A" fill-opacity="0.6" stroke="url(#innerBorder)" stroke-width="1"/>

  <!-- Header -->
  <text x="40" y="48" class="font-sans" font-size="22" font-weight="800" fill="#FFFFFF">Profile Signal</text>
  <text x="40" y="67" class="font-sans" font-size="12" font-weight="400" fill="#94A3B8">Live GitHub stats styled by GitSkins</text>

  <!-- Status Pulse Dot -->
  <circle cx="836" cy="46" r="4.5" fill="#38BDF8" filter="url(#neonGlow)"/>
  <circle cx="836" cy="46" r="8" stroke="#38BDF8" stroke-width="1" stroke-opacity="0.3" fill="none"/>

  <!-- 4 Metrics Cards -->
  <!-- Card 1: Stars -->
  <g transform="translate(38, 86)">
    <rect width="192" height="84" rx="14" fill="#0D1322" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
    <text x="20" y="24" class="font-sans" font-size="11.5" font-weight="600" fill="#94A3B8">Stars</text>
    <text x="20" y="56" class="font-sans" font-size="29" font-weight="800" fill="#38BDF8">66</text>
    <!-- Bar Track -->
    <rect x="20" y="68" width="152" height="4" rx="2" fill="#1E293B"/>
    <rect x="20" y="68" width="85" height="4" rx="2" fill="#38BDF8"/>
    <circle cx="105" cy="70" r="3" fill="#38BDF8" filter="url(#neonGlow)"/>
  </g>

  <!-- Card 2: Contributions -->
  <g transform="translate(244, 86)">
    <rect width="192" height="84" rx="14" fill="#0D1322" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
    <text x="20" y="24" class="font-sans" font-size="11.5" font-weight="600" fill="#94A3B8">Contributions</text>
    <text x="20" y="56" class="font-sans" font-size="29" font-weight="800" fill="#22D3EE">831</text>
    <!-- Bar Track -->
    <rect x="20" y="68" width="152" height="4" rx="2" fill="#1E293B"/>
    <rect x="20" y="68" width="144" height="4" rx="2" fill="#22D3EE"/>
  </g>

  <!-- Card 3: Repos -->
  <g transform="translate(450, 86)">
    <rect width="192" height="84" rx="14" fill="#0D1322" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
    <text x="20" y="24" class="font-sans" font-size="11.5" font-weight="600" fill="#94A3B8">Repos</text>
    <text x="20" y="56" class="font-sans" font-size="29" font-weight="800" fill="#C084FC">12</text>
    <!-- Bar Track -->
    <rect x="20" y="68" width="152" height="4" rx="2" fill="#1E293B"/>
    <rect x="20" y="68" width="55" height="4" rx="2" fill="#C084FC"/>
  </g>

  <!-- Card 4: Followers -->
  <g transform="translate(656, 86)">
    <rect width="186" height="84" rx="14" fill="#0D1322" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
    <text x="20" y="24" class="font-sans" font-size="11.5" font-weight="600" fill="#94A3B8">Followers</text>
    <text x="20" y="56" class="font-sans" font-size="29" font-weight="800" fill="#4ADE80">3</text>
    <!-- Bar Track -->
    <rect x="20" y="68" width="146" height="4" rx="2" fill="#1E293B"/>
    <rect x="20" y="68" width="35" height="4" rx="2" fill="#4ADE80"/>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "profile-signal.svg"), "w", encoding="utf-8") as f:
    f.write(profile_signal_svg)


# 4. LANGUAGE STACK SVG
language_stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 230" width="880" height="230" fill="none">
{get_common_defs()}

  <!-- Outer Glass Frame -->
  <rect x="1" y="1" width="878" height="228" rx="22" fill="#070A12" stroke="url(#cardBorder)" stroke-width="1.5"/>
  <rect x="1" y="1" width="878" height="228" rx="22" fill="url(#leftGlow)"/>
  <rect x="1" y="1" width="878" height="228" rx="22" fill="url(#rightGlow)"/>

  <!-- Inner Frame -->
  <rect x="16" y="16" width="848" height="198" rx="16" fill="#0A0E1A" fill-opacity="0.6" stroke="url(#innerBorder)" stroke-width="1"/>

  <!-- Header -->
  <text x="40" y="46" class="font-sans" font-size="20" font-weight="800" fill="#FFFFFF">Language Stack</text>
  <text x="40" y="65" class="font-sans" font-size="12" font-weight="400" fill="#94A3B8">Repository-weighted technologies</text>

  <!-- Scan prompt right -->
  <text x="836" y="46" class="font-mono" font-size="12.5" font-weight="600" fill="#38BDF8" text-anchor="end">&gt; stack.scan _</text>

  <!-- Language Rows -->
  <!-- Row 1: C (44%) -->
  <g transform="translate(42, 90)">
    <circle cx="5" cy="0" r="4.5" fill="#94A3B8"/>
    <text x="20" y="4" class="font-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">C</text>
    <text x="175" y="4" class="font-mono" font-size="11.5" font-weight="600" fill="#94A3B8" text-anchor="end">44%</text>
    <!-- Bar -->
    <rect x="195" y="-4" width="600" height="7" rx="3.5" fill="#1E293B"/>
    <rect x="195" y="-4" width="264" height="7" rx="3.5" fill="#94A3B8"/>
  </g>

  <!-- Row 2: C++ (20%) -->
  <g transform="translate(42, 114)">
    <circle cx="5" cy="0" r="4.5" fill="#F43F5E"/>
    <text x="20" y="4" class="font-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">C++</text>
    <text x="175" y="4" class="font-mono" font-size="11.5" font-weight="600" fill="#94A3B8" text-anchor="end">20%</text>
    <!-- Bar -->
    <rect x="195" y="-4" width="600" height="7" rx="3.5" fill="#1E293B"/>
    <rect x="195" y="-4" width="120" height="7" rx="3.5" fill="#F43F5E"/>
  </g>

  <!-- Row 3: Assembly (13%) -->
  <g transform="translate(42, 138)">
    <circle cx="5" cy="0" r="4.5" fill="#F59E0B"/>
    <text x="20" y="4" class="font-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">Assembly</text>
    <text x="175" y="4" class="font-mono" font-size="11.5" font-weight="600" fill="#94A3B8" text-anchor="end">13%</text>
    <!-- Bar -->
    <rect x="195" y="-4" width="600" height="7" rx="3.5" fill="#1E293B"/>
    <rect x="195" y="-4" width="78" height="7" rx="3.5" fill="#F59E0B"/>
  </g>

  <!-- Row 4: Kotlin (10%) -->
  <g transform="translate(42, 162)">
    <circle cx="5" cy="0" r="4.5" fill="#A855F7"/>
    <text x="20" y="4" class="font-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">Kotlin</text>
    <text x="175" y="4" class="font-mono" font-size="11.5" font-weight="600" fill="#94A3B8" text-anchor="end">10%</text>
    <!-- Bar -->
    <rect x="195" y="-4" width="600" height="7" rx="3.5" fill="#1E293B"/>
    <rect x="195" y="-4" width="60" height="7" rx="3.5" fill="#A855F7"/>
  </g>

  <!-- Row 5: Python (5%) -->
  <g transform="translate(42, 186)">
    <circle cx="5" cy="0" r="4.5" fill="#38BDF8"/>
    <text x="20" y="4" class="font-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">Python</text>
    <text x="175" y="4" class="font-mono" font-size="11.5" font-weight="600" fill="#94A3B8" text-anchor="end">5%</text>
    <!-- Bar -->
    <rect x="195" y="-4" width="600" height="7" rx="3.5" fill="#1E293B"/>
    <rect x="195" y="-4" width="30" height="7" rx="3.5" fill="#38BDF8"/>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "language-stack.svg"), "w", encoding="utf-8") as f:
    f.write(language_stack_svg)


# 5. KEEP IT MOVING (FOOTER) SVG
footer_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 110" width="880" height="110" fill="none">
{get_common_defs()}

  <!-- Outer Glass Frame -->
  <rect x="1" y="1" width="878" height="108" rx="22" fill="#070A12" stroke="url(#cardBorder)" stroke-width="1.5"/>
  <rect x="1" y="1" width="878" height="108" rx="22" fill="url(#leftGlow)"/>
  <rect x="1" y="1" width="878" height="108" rx="22" fill="url(#rightGlow)"/>

  <!-- Inner Frame -->
  <rect x="16" y="14" width="848" height="82" rx="16" fill="#0A0E1A" fill-opacity="0.6" stroke="url(#innerBorder)" stroke-width="1"/>

  <!-- Center Glossy Pill Button -->
  <g transform="translate(355, 33)">
    <rect width="170" height="44" rx="22" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5" stroke-opacity="0.5"/>
    <rect width="170" height="44" rx="22" fill="none" stroke="url(#cardBorder)" stroke-width="1"/>
    
    <!-- Octocat / G logo -->
    <circle cx="28" cy="22" r="11" fill="#FFFFFF"/>
    <path d="M 28 14 C 23.58 14 20 17.58 20 22 C 20 25.54 22.29 28.53 25.47 29.59 C 25.87 29.66 26.02 29.42 26.02 29.21 C 26.02 29.02 26.01 28.38 26.01 27.57 C 23.78 28.05 23.31 26.97 23.31 26.97 C 22.95 26.05 22.43 25.8 22.43 25.8 C 21.7 25.3 22.49 25.31 22.49 25.31 C 23.3 25.37 23.72 26.14 23.72 26.14 C 24.44 27.37 25.61 27.02 26.07 26.81 C 26.14 26.29 26.35 25.93 26.58 25.73 C 24.8 25.53 22.93 24.84 22.93 21.78 C 22.93 20.91 23.24 20.2 23.75 19.64 C 23.67 19.44 23.39 18.63 23.83 17.53 C 23.83 17.53 24.5 17.32 26.02 18.35 C 26.66 18.17 27.33 18.08 28 18.08 C 28.67 18.08 29.34 18.17 29.98 18.35 C 31.5 17.32 32.17 17.53 32.17 17.53 C 32.61 18.63 32.33 19.44 32.25 19.64 C 32.76 20.2 33.07 20.91 33.07 21.78 C 33.07 24.85 31.19 25.53 29.41 25.72 C 29.7 25.97 29.96 26.46 29.96 27.21 C 29.96 28.29 29.95 29.16 29.95 29.21 C 29.95 29.42 30.1 29.67 30.5 29.59 C 33.68 28.53 36 25.53 36 22 C 36 17.58 32.42 14 28 14 Z" fill="#0F172A"/>

    <!-- Text -->
    <text x="48" y="18" class="font-sans" font-size="10" font-weight="700" fill="#94A3B8" letter-spacing="0.5">GitHub</text>
    <text x="48" y="31" class="font-sans" font-size="12" font-weight="800" fill="#FFFFFF">@phnem</text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "keep-it-moving.svg"), "w", encoding="utf-8") as f:
    f.write(footer_svg)

print("All SVG assets successfully generated!")
