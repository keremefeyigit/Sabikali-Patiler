import re
import sys

def main():
    old_file = 'index_old.html'
    new_file = 'index.html'

    with open(old_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the Tailwind script
    html = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>', '', html)

    # Insert the CSS
    css_content = """
        /* -- START OF NEW CSS -- */
        .accessory { position: absolute; pointer-events: none; z-index: 10; user-select: none; filter: drop-shadow(0 4px 3px rgb(0 0 0 / 0.07)) drop-shadow(0 2px 2px rgb(0 0 0 / 0.06)); }
        .accessory.hat { top: -35%; left: 15%; transform: rotate(-10deg); font-size: 3.5rem; line-height: 1; }
        .accessory.glasses { top: 25%; left: 10%; width: 80%; text-align: center; font-size: 2.5rem; line-height: 1; }
        .accessory.monocle { top: 35%; right: 25%; width: 2rem; height: 2rem; border: 2px solid #f59e0b; border-radius: 50%; background-color: rgba(191, 219, 254, 0.2); box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05); }
        .monocle-string { position: absolute; bottom: -2rem; right: -0.5rem; width: 0.125rem; height: 2.5rem; background-color: #d97706; transform: rotate(-12deg); }
        .accessory.eyepatch { top: 30%; right: 30%; width: 2rem; height: 2rem; background-color: rgba(0, 0, 0, 0.9); border-radius: 50%; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); }
        .eyepatch-string { position: absolute; top: 1rem; left: -3rem; width: 5rem; height: 0.125rem; background-color: rgba(0, 0, 0, 0.8); transform: rotate(-12deg); }
        .accessory.tie { bottom: -15%; left: 25%; width: 50%; text-align: center; font-size: 2.5rem; line-height: 1; }

        .suspect-card { width: 14rem; padding: 0.5rem; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1); transform: rotate(1deg); transition: background-color 0.3s, border-color 0.3s; touch-action: none; user-select: none; position: relative; box-sizing: border-box; }
        @media (min-width: 640px) { .suspect-card { width: 16rem; padding: 0.75rem; } }
        .theme-suspicious { background-color: #e7e5e4; border: 2px solid #57534e; }
        .theme-innocent { background-color: #eff6ff; border: 1px solid #bfdbfe; }

        .card-header { padding: 0.25rem 0.5rem; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center; }
        .theme-suspicious .card-header { background-color: #292524; color: #e7e5e4; }
        .theme-innocent .card-header { background-color: #1d4ed8; color: #ffffff; }

        .card-label { font-family: 'Courier Prime', monospace; font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; }
        .card-id { font-family: 'Courier Prime', monospace; font-size: 10px; }

        .card-photo-box { position: relative; height: 10rem; width: 100%; overflow: visible; display: flex; align-items: center; justify-content: center; margin-bottom: 0.5rem; border-width: 2px; border-style: solid; box-sizing: border-box; }
        @media (min-width: 640px) { .card-photo-box { height: 12rem; } }
        .theme-suspicious .card-photo-box { background-color: #a8a29e; border-color: #44403c; }
        .theme-innocent .card-photo-box { background-color: #dbeafe; border-color: #93c5fd; }

        .bg-lines { position: absolute; inset: 0; z-index: 0; display: flex; flex-direction: column; justify-content: space-evenly; opacity: 0.3; pointer-events: none; }
        .line { border-bottom: 1px solid black; width: 100%; }

        .photo-wrapper { position: relative; z-index: 10; width: 7rem; height: 7rem; }
        @media (min-width: 640px) { .photo-wrapper { width: 8rem; height: 8rem; } }
        .suspect-img { width: 100%; height: 100%; transform: scale(1); transition: transform 0.3s; filter: drop-shadow(0 10px 8px rgb(0 0 0 / 0.04)); pointer-events: none; }
        .suspect-card:hover .suspect-img { transform: scale(1.05); }

        .guilty-stamp { position: absolute; inset: 0; z-index: 20; display: flex; align-items: center; justify-content: center; pointer-events: none; }
        .stamp-text { border: 4px solid #dc2626; color: #dc2626; font-weight: bold; font-size: 1.875rem; padding: 0.5rem; transform: rotate(-12deg); opacity: 0.8; background-color: rgba(255, 255, 255, 0.5); backdrop-filter: blur(4px); border-radius: 0.25rem; font-family: 'Google Sans Text', 'Google Sans', sans-serif;}
        @media (min-width: 640px) { .stamp-text { font-size: 2.25rem; } }

        .suspect-name { font-weight: bold; font-size: 1rem; border-bottom: 2px solid; margin-bottom: 0.25rem; margin-top: 0; text-transform: uppercase; font-family: 'Playfair Display', serif; letter-spacing: 0.025em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; padding-bottom: 2px;}
        @media (min-width: 640px) { .suspect-name { font-size: 1.125rem; } }
        .theme-suspicious .suspect-name { color: #1c1917; border-color: #292524; }
        .theme-innocent .suspect-name { color: #1e3a8a; border-color: #bfdbfe; }

        .record-box { margin-bottom: 0.5rem; background-color: rgba(255, 255, 255, 0.5); padding: 0.375rem; border-radius: 0.25rem; border: 1px solid rgba(0, 0, 0, 0.05); box-sizing: border-box; }
        .record-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.25rem; }
        .record-title { font-size: 10px; font-weight: bold; text-transform: uppercase; color: #78716c; }
        .record-badge { font-size: 10px; font-weight: bold; padding: 0 0.375rem; border-radius: 0.25rem; color: #ffffff; }
        .record-clean { background-color: #16a34a; }
        .record-dirty { background-color: #991b1b; }
        .record-text { font-size: 0.75rem; font-family: 'Courier Prime', monospace; line-height: 1.25; color: #44403c; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin: 0; }

        .statement-box { background-color: #ffffff; padding: 0.5rem; border: 1px solid #e7e5e4; font-size: 0.75rem; font-style: italic; font-family: 'Playfair Display', serif; line-height: 1.25; color: #292524; position: relative; box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05); box-sizing: border-box; min-height: 3em; }
        @media (min-width: 640px) { .statement-box { font-size: 0.875rem; } }
        .quote-start { font-size: 1.5rem; position: absolute; top: -0.5rem; left: -0.25rem; color: #e7e5e4; }
        .quote-end { font-size: 1.5rem; position: absolute; bottom: -1rem; right: 0.5rem; color: #e7e5e4; }
        @media (min-width: 640px) { .quote-start, .quote-end { font-size: 2.25rem; } }
        .statement-text { position: relative; z-index: 10; display: block; }

        .tape-strip { position: absolute; top: -0.75rem; left: 50%; transform: translateX(-50%) rotate(2deg); width: 4rem; height: 1.5rem; background-color: rgba(254, 240, 138, 0.8); box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05); border-left: 1px solid rgba(255, 255, 255, 0.5); border-right: 1px solid rgba(255, 255, 255, 0.5); pointer-events: none; }
        @media (min-width: 640px) { .tape-strip { width: 6rem; } }

        .zoom-btn { position: absolute; bottom: 0.5rem; right: 0.5rem; color: #ffffff; border-radius: 50%; width: 2rem; height: 2rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1); z-index: 30; transition: transform 0.3s; cursor: pointer; border: none; padding: 0; touch-action: auto; pointer-events: auto;}
        .zoom-btn:hover { transform: scale(1.1); }
        .theme-suspicious .zoom-btn { background-color: rgba(68, 64, 60, 0.9); }
        .theme-suspicious .zoom-btn:hover { background-color: #57534e; }
        .theme-innocent .zoom-btn { background-color: rgba(29, 78, 216, 0.9); }
        .theme-innocent .zoom-btn:hover { background-color: #2563eb; }

        .evidence-paper { width: 16rem; padding: 1rem; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1); font-size: 0.875rem; transition: background-color 0.3s, color 0.3s; position: relative; box-sizing: border-box; touch-action: none; user-select: none; }
        .evidence-report { background-color: #fff7ed; border-left: 4px solid #b91c1c; color: #292524; }
        .evidence-report .evidence-content { font-family: 'Courier Prime', monospace; }
        .evidence-flyer { background-color: #fef9c3; border: 1px solid #fde047; color: #1c1917; }
        .evidence-flyer .evidence-content { font-family: 'Google Sans Text', 'Google Sans', sans-serif; font-weight: bold; }
        .evidence-note { background-color: #ffffff; border-top: 8px solid #dbeafe; color: #1e3a8a; }
        .evidence-note .evidence-content { font-family: 'Playfair Display', serif; font-style: italic; }

        .evidence-header { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 0.5rem; padding-right: 2rem; }
        .evidence-id { font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.75rem; opacity: 0.7; }
        .evidence-title { font-weight: bold; margin-bottom: 0.5rem; font-size: 1rem; line-height: 1.25; margin-top: 0; font-family: 'Google Sans Text', 'Google Sans', sans-serif; }
        .evidence-content { white-space: pre-line; line-height: 1.625; margin: 0; }

        .secret-stamp { position: absolute; bottom: 0.5rem; right: 0.5rem; opacity: 0.2; transform: rotate(-12deg); pointer-events: none; }
        .stamp-circle { border: 4px solid #7f1d1d; color: #7f1d1d; border-radius: 50%; width: 6rem; height: 6rem; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.25rem; text-transform: uppercase; letter-spacing: 0.1em; }

        .zoom-btn.evidence-zoom { position: absolute; top: 0.5rem; right: 0.5rem; background-color: rgba(180, 83, 9, 0.9); bottom: auto; }
        .zoom-btn.evidence-zoom:hover { background-color: #d97706; }

        .zoom-overlay { position: fixed; inset: 0; z-index: 200; background-color: rgba(0, 0, 0, 0.95); display: flex; align-items: center; justify-content: center; padding: 1rem; touch-action: auto; overflow: hidden; box-sizing: border-box; }
        .zoom-container { position: relative; width: 100%; max-width: 32rem; max-height: 90vh; overflow-y: auto; }
        .zoom-close-btn { position: sticky; top: 0; float: right; color: #ffffff; background-color: #44403c; border-radius: 50%; padding: 0.5rem; z-index: 100; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); cursor: pointer; border: none; display: flex; align-items: center; justify-content: center; margin-bottom: -2rem; margin-right: -0.5rem;}
        .zoom-close-btn:hover { background-color: #57534e; }

        .zoom-box { padding: 1.5rem; box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25); width: 100%; box-sizing: border-box; border-radius: 0.25rem; }
        @media (min-width: 640px) { .zoom-box { padding: 2rem; } }

        .zoom-report { background-color: #fff7ed; border-left: 8px solid #b91c1c; color: #292524; }
        .zoom-flyer { background-color: #fef9c3; border: 2px solid #fde047; color: #1c1917; }
        .zoom-note { background-color: #ffffff; border-top: 8px solid #dbeafe; color: #1e3a8a; }

        .zoom-evidence-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.25rem; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 0.75rem; }
        .zoom-evidence-id { font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.875rem; opacity: 0.7; }
        .zoom-evidence-type { margin-left: auto; font-size: 0.75rem; opacity: 0.5; text-transform: uppercase; }
        .zoom-evidence-title { font-weight: bold; margin-bottom: 1rem; font-size: 1.5rem; line-height: 1.25; margin-top: 0; font-family: 'Google Sans Text', 'Google Sans', sans-serif; }
        .zoom-evidence-content { white-space: pre-line; line-height: 2; font-size: 1rem; margin: 0; }
        @media (min-width: 640px) { .zoom-evidence-content { font-size: 1.125rem; } }

        .zoom-report .zoom-evidence-content { font-family: 'Courier Prime', monospace; }
        .zoom-flyer .zoom-evidence-content { font-family: 'Google Sans Text', 'Google Sans', sans-serif; font-weight: bold; }
        .zoom-note .zoom-evidence-content { font-family: 'Playfair Display', serif; font-style: italic; }

        .suspect-zoom-box { background-color: #f5f5f4; }
        .zoom-suspect-header { display: flex; align-items: center; gap: 1.25rem; margin-bottom: 1.25rem; border-bottom: 1px solid #d6d3d1; padding-bottom: 1.25rem; }
        .zoom-suspect-img { width: 6rem; height: 6rem; object-fit: contain; flex-shrink: 0; }
        .zoom-suspect-info { display: flex; flex-direction: column; }
        .zoom-suspect-name { font-size: 1.5rem; font-weight: bold; font-family: 'Playfair Display', serif; color: #292524; text-transform: uppercase; line-height: 1.25; margin: 0; }
        .zoom-suspect-species { font-size: 0.875rem; color: #78716c; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.25rem; margin-bottom: 0; }
        .zoom-suspect-record-row { display: flex; align-items: center; gap: 0.5rem; margin-top: 0.5rem; }
        .zoom-suspect-record-text { font-size: 0.75rem; color: #78716c; font-family: 'Courier Prime', monospace; }

        .zoom-statement-box { background-color: #ffffff; padding: 1.25rem; border: 1px solid #e7e5e4; box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05); position: relative; margin-bottom: 1rem; box-sizing: border-box; }
        .zoom-quote-start { font-size: 3rem; color: #e7e5e4; line-height: 1; margin-bottom: 0.5rem; font-family: 'Playfair Display', serif; height: 1.5rem; }
        .zoom-statement-text { font-size: 1rem; font-family: 'Playfair Display', serif; font-style: italic; line-height: 1.625; color: #292524; margin: 0; }
        @media (min-width: 640px) { .zoom-statement-text { font-size: 1.125rem; } }
        .zoom-quote-end { font-size: 3rem; color: #e7e5e4; text-align: right; line-height: 1; margin-top: 0.5rem; font-family: 'Playfair Display', serif; height: 1.5rem; display: flex; justify-content: flex-end;}

        .zoom-traits { margin-bottom: 1rem; }
        .zoom-traits-label { font-size: 0.75rem; text-transform: uppercase; font-weight: bold; color: #78716c; margin-right: 0.5rem; }
        .zoom-trait { display: inline-block; background-color: #e7e5e4; color: #44403c; font-size: 0.75rem; padding: 0.125rem 0.5rem; border-radius: 9999px; margin-right: 0.25rem; margin-bottom: 0.25rem; }

        .zoom-guilty-badge { margin-top: 1rem; background-color: #fee2e2; border: 2px solid #ef4444; color: #b91c1c; text-align: center; font-weight: bold; font-size: 1.25rem; padding: 0.75rem; border-radius: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-family: 'Google Sans Text', 'Google Sans', sans-serif;}

        .intro-screen { min-height: 100vh; background-color: #1c1917; display: flex; align-items: center; justify-content: center; padding: 1rem; font-family: 'Playfair Display', serif; color: #e7e5e4; box-sizing: border-box; }
        .intro-box { max-width: 28rem; width: 100%; background-color: #292524; padding: 2rem; box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25); border-top: 4px solid #d97706; border-radius: 0.5rem; position: relative; overflow: hidden; box-sizing: border-box; }
        .intro-icon { display: flex; justify-content: center; margin-bottom: 1.5rem; }
        .intro-title { font-size: 1.875rem; font-weight: bold; text-align: center; margin-bottom: 0.5rem; letter-spacing: 0.05em; color: #f59e0b; margin-top: 0; font-family: 'Google Sans Text', 'Google Sans', sans-serif; }
        .intro-subtitle { font-size: 1.25rem; text-align: center; margin-bottom: 1.5rem; color: #a8a29e; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0; font-family: 'Google Sans Text', 'Google Sans', sans-serif;}
        .intro-body { font-size: 1.125rem; line-height: 1.625; margin-bottom: 2rem; color: #d6d3d1; font-style: italic; margin-top: 0; }
        .intro-btn { width: 100%; background-color: #b45309; color: #ffffff; font-weight: bold; padding: 1rem; border-radius: 0.25rem; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); transition: transform 0.1s, background-color 0.3s; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: center; gap: 0.5rem; cursor: pointer; border: none; font-size: 1rem; }
        .intro-btn:hover { background-color: #d97706; transform: scale(1.05); }

        .loading-screen { min-height: 100vh; background-color: #1c1917; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1rem; font-family: 'Playfair Display', serif; color: #f59e0b; box-sizing: border-box; text-align: center; }
        .loading-title { font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 1rem; margin-bottom: 0; font-family: 'Google Sans Text', 'Google Sans', sans-serif; }
        .loading-subtitle { color: #a8a29e; margin-top: 0.5rem; font-family: 'Google Sans Text', 'Google Sans', sans-serif; }

        .game-wrapper { min-height: 100vh; height: 100vh; background-color: #2c241b; overflow: hidden; position: relative; touch-action: none; font-family: 'Google Sans Text', 'Google Sans', sans-serif;}
        .game-wrapper ::selection { background-color: #fde68a; color: #78350f; }

        .game-bg-pattern { position: absolute; inset: 0; opacity: 0.1; pointer-events: none; background-image: url('https://www.transparenttextures.com/patterns/wood-pattern.png'); }

        .game-header { position: absolute; top: 0; left: 0; right: 0; height: 4rem; background-color: rgba(28, 25, 23, 0.95); backdrop-filter: blur(4px); z-index: 50; display: flex; align-items: center; justify-content: space-between; padding: 0 1rem; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1); border-bottom: 1px solid #44403c; box-sizing: border-box; }
        @media (min-width: 640px) { .game-header { padding: 0 1.5rem; } }

        .header-left { display: flex; align-items: center; gap: 1rem; color: #e7e5e4; }
        .header-logo { display: flex; align-items: center; gap: 0.5rem; }
        .logo-text { font-weight: bold; letter-spacing: 0.1em; text-transform: uppercase; font-size: 0.875rem; }
        .header-divider { height: 1.5rem; width: 1px; background-color: #44403c; margin: 0 0.5rem; }
        .header-case { font-size: 0.75rem; font-family: 'Courier Prime', monospace; color: #a8a29e; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        @media (min-width: 768px) { .header-case { max-width: 200px; } }
        .case-title { color: #ffffff; font-weight: bold; }

        .hide-mobile { display: none; }
        @media (min-width: 640px) { .hide-mobile { display: block; } }
        @media (min-width: 768px) { .header-case { display: block; } }

        .header-right { display: flex; align-items: center; gap: 0.5rem; }
        @media (min-width: 640px) { .header-right { gap: 1rem; } }

        .score-box { background-color: #292524; padding: 0.25rem 0.75rem; border-radius: 0.25rem; border: 1px solid #57534e; display: flex; flex-direction: column; align-items: flex-end; }
        .score-rank { font-size: 9px; color: #a8a29e; text-transform: uppercase; letter-spacing: 0.1em; }
        .score-value { font-family: 'Courier Prime', monospace; font-weight: bold; line-height: 1; font-size: 0.875rem; }
        .text-red { color: #f87171; }
        .text-green { color: #4ade80; }

        .accuse-btn { background-color: #b91c1c; color: #ffffff; padding: 0.5rem 1rem; border-radius: 0.25rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.75rem; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); transition: background-color 0.3s; border: 1px solid #ef4444; white-space: nowrap; cursor: pointer; }
        @media (min-width: 640px) { .accuse-btn { font-size: 0.875rem; } }
        .accuse-btn:hover { background-color: #dc2626; }

        .game-area { width: 100%; height: 100%; position: absolute; top: 0; left: 0; overflow: hidden; cursor: crosshair; touch-action: none; }

        .case-brief { position: absolute; top: 5rem; left: 1rem; right: 1rem; background-color: rgba(41, 37, 36, 0.9); color: #e7e5e4; padding: 0.75rem; border-radius: 0.25rem; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1); border: 1px solid rgba(120, 53, 15, 0.5); max-width: 42rem; text-align: center; z-index: 10; pointer-events: none; box-sizing: border-box; margin: 0 auto;}
        @media (min-width: 640px) { 
            .case-brief { left: 50%; right: auto; transform: translateX(-50%); padding: 1rem; }
        }
        .brief-title { color: #f59e0b; font-weight: bold; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem; margin-bottom: 0.25rem; margin-top: 0; }
        @media (min-width: 640px) { .brief-title { font-size: 0.875rem; } }
        .brief-desc { font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.75rem; margin: 0; }
        @media (min-width: 640px) { .brief-desc { font-size: 0.875rem; } }

        .modal-overlay { position: fixed; inset: 0; z-index: 100; background-color: rgba(0, 0, 0, 0.85); backdrop-filter: blur(12px); display: flex; align-items: center; justify-content: center; padding: 0.5rem; overflow-y: auto; touch-action: auto; box-sizing: border-box; }
        @media (min-width: 640px) { .modal-overlay { padding: 1rem; } }

        .modal-content { background-color: #f5f5f4; border-radius: 0.125rem; box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25); position: relative; box-sizing: border-box; margin: auto; }
        .accusation-content { max-width: 56rem; width: 100%; padding: 1rem; border: 4px solid #292524; }
        @media (min-width: 640px) { .accusation-content { padding: 2rem; border-width: 8px; } }

        .cancel-btn { position: absolute; top: 0.5rem; right: 0.5rem; color: #78716c; font-weight: bold; font-size: 0.875rem; background-color: #e7e5e4; padding: 0.25rem 0.5rem; border-radius: 0.25rem; border: none; cursor: pointer; z-index: 100;}
        .cancel-btn:hover { color: #292524; }
        @media (min-width: 640px) { .cancel-btn { top: 1rem; right: 1rem; } }

        .modal-title { font-size: 1.5rem; font-weight: bold; text-align: center; margin-bottom: 0.5rem; text-transform: uppercase; color: #292524; margin-top: 0; }
        @media (min-width: 640px) { .modal-title { font-size: 1.875rem; } }

        .modal-subtitle { text-align: center; color: #78716c; margin-bottom: 1rem; font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.75rem; margin-top: 0; }
        @media (min-width: 640px) { .modal-subtitle { margin-bottom: 2rem; font-size: 0.875rem; } }

        .suspect-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem; }
        @media (min-width: 640px) { .suspect-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); } }

        .suspect-select-btn { display: flex; flex-direction: column; align-items: center; position: relative; transition: all 0.2s; background-color: #ffffff; padding: 0.5rem; box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05); border: 1px solid #e7e5e4; cursor: pointer; width: 100%; box-sizing: border-box; }
        .suspect-select-btn:hover:not(.selected) { background-color: #fafaf9; }
        .suspect-select-btn.selected { box-shadow: 0 0 0 4px #dc2626; z-index: 10; }

        .suspect-select-photo { width: 100%; height: 6rem; padding: 0.25rem; background-color: #fffbeb; flex-shrink: 0; box-sizing: border-box; display: flex; align-items: center; justify-content: center; }
        @media (min-width: 640px) { .suspect-select-photo { height: 7rem; } }
        .suspect-select-photo img { width: 100%; height: 100%; object-fit: contain; }

        .suspect-select-info { text-align: center; padding: 0.25rem; }
        .suspect-select-name { font-size: 0.75rem; font-weight: bold; text-transform: uppercase; font-family: 'Playfair Display', serif; color: #292524; line-height: 1.25; margin: 0; }
        @media (min-width: 640px) { .suspect-select-name { font-size: 0.875rem; } }
        .suspect-select-species { font-size: 10px; color: #78716c; text-transform: uppercase; margin: 0; }

        .suspect-check-icon { position: absolute; top: -0.75rem; right: -0.75rem; background-color: #dc2626; color: #ffffff; border-radius: 50%; padding: 0.25rem; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); display: flex; justify-content: center; align-items: center;}

        .modal-actions { margin-top: 1.5rem; display: flex; justify-content: center; }
        @media (min-width: 640px) { .modal-actions { margin-top: 2rem; } }

        .confirm-btn { width: 100%; padding: 0.75rem 3rem; font-size: 1.125rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 0.25rem; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1); transition: all 0.3s; border: none; }
        @media (min-width: 640px) { .confirm-btn { width: auto; padding: 1rem 3rem; font-size: 1.25rem; } }
        .confirm-btn.active { background-color: #b91c1c; color: #ffffff; cursor: pointer; }
        .confirm-btn.active:hover { background-color: #991b1b; transform: translateY(-0.25rem); }
        .confirm-btn.disabled { background-color: #d6d3d1; color: #78716c; cursor: not-allowed; }

        .result-overlay { background-color: #1c1917; }
        .result-content { max-width: 42rem; width: 100%; padding: 1.5rem; border-radius: 0.5rem; box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25); border-left-width: 8px; border-left-style: solid; box-sizing: border-box;}
        @media (min-width: 640px) { .result-content { padding: 2rem; } }

        .result-success { background-color: #f0fdf4; border-left-color: #16a34a; }
        .result-failure { background-color: #fef2f2; border-left-color: #dc2626; }

        .result-header { display: flex; flex-direction: column; align-items: center; gap: 1rem; margin-bottom: 1.5rem; text-align: center; }
        @media (min-width: 640px) { .result-header { flex-direction: row; text-align: left; } }

        .result-title { font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; margin: 0; }
        @media (min-width: 640px) { .result-title { font-size: 1.875rem; } }
        .result-success .result-title { color: #166534; }
        .result-failure .result-title { color: #991b1b; }

        .result-badges { display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin-top: 0.25rem; }
        @media (min-width: 640px) { .result-badges { justify-content: flex-start; } }

        .point-badge { font-weight: bold; padding: 0.125rem 0.5rem; border-radius: 0.25rem; font-size: 0.875rem; color: #ffffff; }
        .result-success .point-badge { background-color: #15803d; }
        .result-failure .point-badge { background-color: #b91c1c; }

        .result-label { color: #78716c; font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.875rem; }

        .result-message { font-size: 1rem; color: #44403c; line-height: 1.625; font-family: 'Playfair Display', serif; border-top: 1px solid #e7e5e4; padding-top: 1rem; max-height: 40vh; overflow-y: auto; margin-bottom: 2rem; }
        @media (min-width: 640px) { .result-message { font-size: 1.125rem; } }

        .result-actions { display: flex; justify-content: center; }
        @media (min-width: 640px) { .result-actions { justify-content: flex-end; } }

        .next-btn { display: flex; align-items: center; gap: 0.5rem; padding: 0.75rem 2rem; border-radius: 0.25rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.1em; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); color: #ffffff; transition: transform 0.1s, background-color 0.3s; border: none; cursor: pointer; font-size: 1rem; }
        .next-btn:hover { transform: scale(1.05); }
        .result-success .next-btn { background-color: #15803d; }
        .result-success .next-btn:hover { background-color: #166534; }
        .result-failure .next-btn { background-color: #44403c; }
        .result-failure .next-btn:hover { background-color: #292524; }
        /* -- END OF NEW CSS -- */
"""

    html = html.replace("</style>", css_content + "\n    </style>")

    replacements = [
        # replace buildAccessory logic mappings
        (r'case \'hat\':[\s\S]*?return `<div[^>]*>🎩</div>`;', r"case 'hat':\n            return `<div class=\"accessory hat\">🎩</div>`;"),
        (r'case \'glasses\':[\s\S]*?return `<div[^>]*>👓</div>`;', r"case 'glasses':\n            return `<div class=\"accessory glasses\">👓</div>`;"),
        (r'case \'monocle\':[\s\S]*?return `<div[^>]*><div[^>]*></div></div>`;', r"case 'monocle':\n            return `<div class=\"accessory monocle\"><div class=\"monocle-string\"></div></div>`;"),
        (r'case \'eyepatch\':[\s\S]*?return `<div[^>]*><div[^>]*></div></div>`;', r"case 'eyepatch':\n            return `<div class=\"accessory eyepatch\"><div class=\"eyepatch-string\"></div></div>`;"),
        (r'case \'tie\':[\s\S]*?return `<div[^>]*>🎀</div>`;', r"case 'tie':\n            return `<div class=\"accessory tie\">🎀</div>`;"),

        # buildSuspectCard
        (r'function buildSuspectCard\(suspect, gameState\) \{[\s\S]*?return `[\s\S]*?</div>`;\n}', r'''function buildSuspectCard(suspect, gameState) {
    const isSuspicious = suspect.appearance === 'suspicious';
    const isGuiltyRevealed = suspect.isGuilty && (gameState === 'success' || gameState === 'failure' || gameState === 'game_over');
    
    // Convert logic to simple classes wrapper
    const themeClass = isSuspicious ? "theme-suspicious" : "theme-innocent";
    const bgLines = isSuspicious ? `<div class="bg-lines"><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div>` : '';
    const guiltyStamp = isGuiltyRevealed ? `<div class="guilty-stamp"><div class="stamp-text">SUÇLU</div></div>` : '';
    const recordTheme = (suspect.criminalRecord === 'Temiz' || suspect.criminalRecord.includes('Yok')) ? 'record-clean' : 'record-dirty';
    const recordLabel = (suspect.criminalRecord === 'Temiz' || suspect.criminalRecord.includes('Yok')) ? 'TEMİZ' : 'SABIKALI';

    return `
    <div class="suspect-card ${themeClass}">
        <div class="card-header">
            <span class="card-label">${isSuspicious ? 'GÖZALTI' : 'KİMLİK'}</span>
            <span class="card-id">${suspect.id.slice(0,4)}</span>
        </div>
        <div class="card-photo-box">
            ${bgLines}
            <div class="photo-wrapper">
                <img src="${getImageUrl(suspect.species)}" alt="${suspect.species}" class="suspect-img">
                ${buildAccessory(suspect.accessory)}
            </div>
            ${guiltyStamp}
        </div>
        <h3 class="suspect-name">${suspect.name}</h3>
        <div class="record-box">
            <div class="record-header">
                <span class="record-title">Sabıka:</span>
                <span class="record-badge ${recordTheme}">${recordLabel}</span>
            </div>
            <p class="record-text">${suspect.criminalRecord}</p>
        </div>
        <div class="statement-box">
            <span class="quote-start">"</span>
            <span class="statement-text">${suspect.statement}</span>
            <span class="quote-end">"</span>
        </div>
        <div class="tape-strip"></div>
        <button data-zoom-suspect="${suspect.id}" onpointerdown="event.stopPropagation()" class="zoom-btn" title="Tam Ekranda Görüntüle">
            ${ICONS.zoomIn}
        </button>
    </div>`;
}'''),
        # buildEvidencePaper
        (r'function buildEvidencePaper\(evidence\) \{[\s\S]*?return `[\s\S]*?</div>`;\n}', r'''function buildEvidencePaper(evidence) {
    let specificStyle = '', iconHtml = '';
    if (evidence.type === 'report') {
        specificStyle = 'evidence-report';
        iconHtml = ICONS.alertTriangle;
    } else if (evidence.type === 'flyer') {
        specificStyle = 'evidence-flyer';
        iconHtml = ICONS.mapPin;
    } else {
        specificStyle = 'evidence-note';
        iconHtml = ICONS.fileText;
    }
    const secretStamp = evidence.type === 'report' ? `<div class="secret-stamp"><div class="stamp-circle">GİZLİ</div></div>` : '';

    return `
    <div class="evidence-paper ${specificStyle}">
        <div class="evidence-header">
            ${iconHtml}
            <span class="evidence-id">Kanıt #${evidence.id}</span>
        </div>
        <h4 class="evidence-title">${evidence.title}</h4>
        <p class="evidence-content">${evidence.content}</p>
        ${secretStamp}
        <button data-zoom-evidence="${evidence.id}" onpointerdown="event.stopPropagation()" class="zoom-btn evidence-zoom" title="Tam Ekranda Görüntüle">
            ${ICONS.zoomIn}
        </button>
    </div>`;
}'''),
        # buildZoomModal
        (r'function buildZoomModal\(\) \{[\s\S]*?return `[\s\S]*?</div>`;\n}', r'''function buildZoomModal() {
    const { zoomItem, gameState } = state;
    if (!zoomItem) return '';
    const { type, data } = zoomItem;

    let innerHtml = '';
    if (type === 'evidence') {
        let bgClass = '', fontStyle = '', iconHtml = '';
        if (data.type === 'report') { bgClass = 'zoom-report'; iconHtml = ICONS.alertTriangleLg; }
        else if (data.type === 'flyer') { bgClass = 'zoom-flyer'; iconHtml = ICONS.mapPinLg; }
        else { bgClass = 'zoom-note'; iconHtml = ICONS.fileTextLg; }
        innerHtml = `
        <div class="zoom-box evidence-zoom-box ${bgClass}">
            <div class="zoom-evidence-header">
                ${iconHtml}
                <span class="zoom-evidence-id">Kanıt #${data.id}</span>
                <span class="zoom-evidence-type">${data.type}</span>
            </div>
            <h4 class="zoom-evidence-title">${data.title}</h4>
            <p class="zoom-evidence-content">${data.content}</p>
        </div>`;
    } else {
        const isGuiltyRevealed = data.isGuilty && (gameState === 'success' || gameState === 'failure' || gameState === 'game_over');
        const recordTheme = (data.criminalRecord === 'Temiz' || data.criminalRecord.includes('Yok')) ? 'record-clean' : 'record-dirty';
        const recordLabel = (data.criminalRecord === 'Temiz' || data.criminalRecord.includes('Yok')) ? 'TEMİZ' : 'SABIKALI';
        const traitsHtml = data.traits && data.traits.length > 0
            ? `<div class="zoom-traits"><span class="zoom-traits-label">Özellikler:</span>${data.traits.map(t => `<span class="zoom-trait">${t}</span>`).join('')}</div>` : '';
        const guiltyBadge = isGuiltyRevealed ? `<div class="zoom-guilty-badge">⚠️ SUÇLU ÇIKTI</div>` : '';
        innerHtml = `
        <div class="zoom-box suspect-zoom-box">
            <div class="zoom-suspect-header">
                <img src="${getImageUrl(data.species)}" alt="${data.species}" class="zoom-suspect-img">
                <div class="zoom-suspect-info">
                    <h3 class="zoom-suspect-name">${data.name}</h3>
                    <p class="zoom-suspect-species">${data.species}</p>
                    <div class="zoom-suspect-record-row">
                        <span class="record-badge ${recordTheme}">${recordLabel}</span>
                        <span class="zoom-suspect-record-text">${data.criminalRecord}</span>
                    </div>
                </div>
            </div>
            <div class="zoom-statement-box">
                <div class="zoom-quote-start">"</div>
                <p class="zoom-statement-text">${data.statement}</p>
                <div class="zoom-quote-end">"</div>
            </div>
            ${traitsHtml}
            ${guiltyBadge}
        </div>`;
    }

    return `
    <div id="zoom-modal" class="zoom-overlay">
        <div class="zoom-container" onclick="event.stopPropagation()">
            <button id="zoom-close" class="zoom-close-btn">
                ${ICONS.x}
            </button>
            ${innerHtml}
        </div>
    </div>`;
}'''),
        # Intro Screen
        (r'if \(gameState === \'intro\'\) \{[\s\S]*?root\.innerHTML = `[\s\S]*?</div>`;\n        document\.getElementById\(\'start-btn\'\)\.addEventListener\(\'click\', \(\) => loadNewCase\(\)\);\n        return;\n    }', r'''if (gameState === 'intro') {
        root.innerHTML = `
        <div class="intro-screen">
            <div class="intro-box">
                <div class="intro-icon">${ICONS.brainCircuit}</div>
                <h1 class="intro-title">${INTRO_TEXT.title}</h1>
                <h2 class="intro-subtitle">${INTRO_TEXT.subtitle}</h2>
                <p class="intro-body">"${INTRO_TEXT.body}"</p>
                <button id="start-btn" class="intro-btn">
                    ${INTRO_TEXT.button}
                </button>
            </div>
        </div>`;
        document.getElementById('start-btn').addEventListener('click', () => loadNewCase());
        return;
    }'''),
        # Loading Screen
        (r'if \(gameState === \'loading\'\) \{[\s\S]*?root\.innerHTML = `[\s\S]*?</div>`;\n        return;\n    }', r'''if (gameState === 'loading') {
        root.innerHTML = `
        <div class="loading-screen">
            ${ICONS.loader}
            <h2 class="loading-title animate-pulse">Vaka Oluşturuluyor...</h2>
            <p class="loading-subtitle">Şüpheliler sorgulanıyor, kanıtlar toplanıyor.</p>
        </div>`;
        return;
    }'''),
        # Rest of render() HTML template
        (r'const isRoundEnd = gameState === \'success\' \|\| gameState === \'failure\';\n\n    root\.innerHTML = `[\s\S]*?\$\{buildZoomModal\(\)\}\n    </div>`;', r'''const isRoundEnd = gameState === 'success' || gameState === 'failure';

    root.innerHTML = `
    <div class="game-wrapper selection-amber touch-none">
        <div class="game-bg-pattern"></div>
        
        <div class="game-header">
            <div class="header-left">
                <div class="header-logo">
                    ${ICONS.search}
                    <span class="logo-text hide-mobile">Sabıkalı Patiler</span>
                </div>
                <div class="header-divider hide-mobile"></div>
                <div class="header-case hide-mobile">Vaka: <span class="case-title">${currentCase?.title||''}</span></div>
            </div>
            <div class="header-right">
                <div class="score-box">
                    <span class="score-rank">${getRank(score)}</span>
                    <span class="score-value ${score < 0 ? 'text-red' : 'text-green'}">${score} P</span>
                </div>
                ${gameState === 'investigation' ? `<button id="accuse-btn" class="accuse-btn animate-pulse">Suçla</button>` : ''}
            </div>
        </div>
        
        <div id="game-area" class="game-area touch-none">
            ${gameState === 'investigation' && currentCase ? `
            <div class="case-brief animate-in">
                <h3 class="brief-title">${currentCase.title}</h3>
                <p class="brief-desc">${currentCase.description}</p>
            </div>` : ''}
        </div>

        ${gameState === 'accusation' && currentCase ? `
        <div class="modal-overlay accusation-modal">
            <div class="modal-content accusation-content">
                <button id="cancel-accuse-btn" class="cancel-btn">İPTAL</button>
                <h2 class="modal-title">Suçlu Kim?</h2>
                <p class="modal-subtitle">Yanlış seçim: -50 puan.</p>
                <div class="suspect-grid">
                    ${currentCase.suspects.map(s => `
                    <button data-suspect-select="${s.id}" class="suspect-select-btn ${selectedSuspectId === s.id ? 'selected' : ''}">
                        <div class="suspect-select-photo">
                            <img src="${getImageUrl(s.species)}" alt="${s.name}">
                        </div>
                        <div class="suspect-select-info">
                            <h3 class="suspect-select-name">${s.name}</h3>
                            <p class="suspect-select-species">${s.species}</p>
                        </div>
                        ${selectedSuspectId === s.id ? `<div class="suspect-check-icon">${ICONS.checkCircleSmall}</div>` : ''}
                    </button>`).join('')}
                </div>
                <div class="modal-actions">
                    <button id="confirm-accuse-btn" ${!selectedSuspectId ? 'disabled' : ''} class="confirm-btn ${selectedSuspectId ? 'active' : 'disabled'}">
                        KARARI ONAYLA
                    </button>
                </div>
            </div>
        </div>` : ''}

        ${isRoundEnd && currentCase ? `
        <div class="modal-overlay result-overlay animate-in">
            <div class="modal-content result-content ${gameState === 'success' ? 'result-success' : 'result-failure'}">
                <div class="result-header">
                    ${gameState === 'success' ? ICONS.checkCircle : ICONS.xCircle}
                    <div class="result-title-box">
                        <h2 class="result-title">
                            ${gameState === 'success' ? currentCase.solution.successTitle : currentCase.solution.failureTitle}
                        </h2>
                        <div class="result-badges">
                            <span class="point-badge">${gameState === 'success' ? '+100 Puan' : '-50 Puan'}</span>
                            <span class="result-label">Vaka Sonucu</span>
                        </div>
                    </div>
                </div>
                <div class="result-message">
                    ${gameState === 'success' ? currentCase.solution.successMessage : currentCase.solution.failureMessage}
                </div>
                <div class="result-actions">
                    <button id="next-case-btn" class="next-btn">
                        Sıradaki Vaka ${ICONS.arrowRight}
                    </button>
                </div>
            </div>
        </div>` : ''}

        ${buildZoomModal()}
    </div>`;''')
    ]

    for pattern, repl in replacements:
        html = re.sub(pattern, repl, html, flags=re.MULTILINE)

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Refactoring complete, pure css version written to {new_file}")

if __name__ == '__main__':
    main()
